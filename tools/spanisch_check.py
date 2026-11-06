#!/usr/bin/env python3
"""Prüft das Spanisch der Lernseiten (Hilfe für den Agenten «spanisch-pruefer»).

Aufruf:  python3 -I tools/spanisch_check.py [Seite.html ...]   (ohne Angabe: alle Seiten)
Braucht: apt-get install -y hunspell hunspell-es   (Wörterbuch Spanisch)

Was es macht:
1. Sucht Paare Deutsch / Spanisch: tr('de','es'), both('de','es'), { de/text/…: '…', es: '…' } und im HTML
   <… data-l="de">…</…> gefolgt von <… data-l="es">…</…>. Dazu Spanisch ohne Paar (data-es…-Attribute).
2. Namen: Ein Name (gross geschrieben, kein spanisches Wort, kommt auf der Seite im Deutschen und im Spanischen vor)
   muss im spanischen Text gleich geschrieben sein wie im deutschen. Gemeldet wird:
   - Name steht im Deutschen, fehlt aber im Spanischen desselben Paars,
   - gross geschriebenes Wort im Spanischen, das einem Namen ähnlich ist (z.B. Yuri statt Jurij).
3. Rechtschreibung: Wörter im Spanischen, die das Wörterbuch nicht kennt (ohne Wörter, die auch im Deutschen stehen,
   z.B. englische Wörter, Namen, Scratch-Blöcke). Das ist nur eine Liste zum Anschauen: Das Wörterbuch kennt
   viele Formen nicht (pregúntate, dominada). Entscheiden muss der Mensch bzw. der Agent.
Ändert nichts.
"""
import re, sys, glob, os, html, shutil, subprocess
from html.parser import HTMLParser
from difflib import SequenceMatcher

SPELL = bool(shutil.which('hunspell')) and os.path.exists('/usr/share/hunspell/es_ES.dic')
_CACHE = {}


def unknown_words(ws):
    """Wörter, die das spanische Wörterbuch (hunspell es_ES) nicht kennt."""
    todo = [w for w in set(ws) if w not in _CACHE]
    if todo:
        out = subprocess.run(['hunspell', '-i', 'utf-8', '-d', 'es_ES', '-l'], input='\n'.join(todo),
                             capture_output=True, text=True).stdout.split()
        bad = set(out)
        for w in todo:
            _CACHE[w] = w not in bad
    return {w for w in ws if not _CACHE[w]}

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
WORD = re.compile(r"[A-Za-zÁÉÍÓÚÜÑáéíóúüñÄÖäöß]+")
STR = r"""(?:'((?:[^'\\]|\\.)*)'|"((?:[^"\\]|\\.)*)"|`((?:[^`\\]|\\.)*)`)"""


def clean(t):
    t = re.sub(r"\$\{[^}]*\}", " ", t)          # Template-Ausdrücke
    t = re.sub(r"<[^>]+>", " ", t)               # HTML-Tags
    return html.unescape(t).replace("\\n", " ").replace("\\'", "'")


def strval(m, base=0):
    return next(g for g in m.groups()[base:base + 3] if g is not None) if any(m.groups()[base:base + 3]) else ''


class Pairs(HTMLParser):
    """HTML: data-l="es" mit dem letzten data-l="de" davor (gleiche Tiefe) paaren."""
    VOID = {'br', 'img', 'input', 'meta', 'link', 'hr', 'source', 'col', 'area', 'wbr'}

    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.stack, self.pairs, self.solo, self.last_de, self.skip = [], [], [], {}, 0

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        for k, v in a.items():
            if k.startswith('data-es') and v:
                self.solo.append(v)
        if tag in ('script', 'style'):
            self.skip += 1
        if tag in ('br', 'p', 'li', 'div', 'td', 'th', 'tr') and self.stack:
            self.stack[-1]['text'].append(' ')
        if tag in self.VOID:
            return
        self.stack.append({'tag': tag, 'l': a.get('data-l'), 'en': a.get('lang') == 'en', 'text': []})

    def handle_endtag(self, tag):
        if tag in ('script', 'style'):
            self.skip = max(0, self.skip - 1)
        if tag in self.VOID:
            return
        while self.stack:
            el = self.stack.pop()
            txt = ''.join(el['text'])
            if self.stack:
                self.stack[-1]['text'].append(txt if not el['en'] else ' ')
            depth = len(self.stack)
            if el['l'] == 'de':
                self.last_de[depth] = txt
            elif el['l'] == 'es':
                self.pairs.append((self.last_de.pop(depth, ''), txt, self.getpos()[0]))
            if el['tag'] == tag:
                break

    def handle_data(self, d):
        if self.stack and not self.skip:
            self.stack[-1]['text'].append(d)


def js_pairs(src):
    out = []
    for m in re.finditer(r"\b(?:tr|both)\(\s*" + STR + r"\s*,\s*" + STR, src):
        g = m.groups()
        de = next((x for x in g[0:3] if x is not None), '')
        es = next((x for x in g[3:6] if x is not None), '')
        out.append((de, es, src.count('\n', 0, m.start()) + 1))
    line = lambda pos: src.count('\n', 0, pos) + 1
    first = lambda m, i=0: next((x for x in m.groups()[i:i + 3] if x is not None), '')
    # { de/text/…: '…', es: '…' }  (nur als Schlüssel, nicht «So heisst es:» im Text)
    for m in re.finditer(r"(?:^|[{,])\s*es\s*:\s*" + STR, src, re.M):
        start = src.rfind('{', 0, m.start())
        before = src[max(start, m.start() - 1500):m.start()]
        cand = list(re.finditer(r"\b\w+\s*:\s*" + STR, before))
        out.append((first(cand[-1]) if cand else '', first(m), line(m.start())))
    # { tip: '…', tipEs: '…' } und Listen { words: [...], wordsEs: [...] }
    LIST = r"\[((?:\s*" + STR + r"\s*,?)*)\s*\]"
    def val(txt):
        return ' '.join(x for mm in re.finditer(STR, txt) for x in mm.groups() if x is not None)
    for m in re.finditer(r"\b(\w+)Es\s*:\s*(" + STR + "|" + LIST + ")", src):
        key = m.group(1)
        if key == 'keys':            # Wortteile (amenaz, policia): keine Rechtschreibung
            continue
        start = src.rfind('{', 0, m.start())
        before = src[max(start, m.start() - 3000):m.start()]
        cand = list(re.finditer(r"\b" + key + r"\s*:\s*(" + STR + "|" + LIST + ")", before))
        out.append((val(cand[-1].group(1)) if cand else '', val(m.group(2)), line(m.start())))
    # ['Deutsch', 'Español']
    for m in re.finditer(r"\[\s*" + STR + r"\s*,\s*" + STR + r"\s*\]", src):
        de, es = first(m), first(m, 3)
        if spanish_score(es) > spanish_score(de) + 0.3:
            out.append((de, es, line(m.start())))
    return out


def spanish_score(t):
    """Anteil Wörter, die das spanische Wörterbuch kennt."""
    ws = [w for w in words(t) if len(w) > 2]
    if not ws or not SPELL:
        return 0
    return 1 - len(unknown_words(ws)) / len(ws)


def words(t):
    return WORD.findall(clean(t))


def caps(t):
    """Gross geschriebene Wörter, die nicht am Satzanfang stehen."""
    out = []
    for s in re.split(r"(?<=[.!?¡¿:;«»\"(])\s*|\n", clean(t)):
        ws = WORD.findall(s)
        out += [w for w in ws[1:] if w[0].isupper() and len(w) > 2]
    return out


def is_es_word(w):
    return SPELL and not unknown_words([w]) or (SPELL and not unknown_words([w.lower()]))


LAND = {'Schweiz': 'Suiza', 'Kasachstan': 'Kazajistán', 'Deutschland': 'Alemania', 'Italien': 'Italia',
        'Island': 'Islandia', 'Japan': 'Japón', 'Schottland': 'Escocia', 'England': 'Inglaterra', 'London': 'Londres'}


def check(path):
    src = open(path, encoding='utf-8').read()
    p = Pairs()
    p.feed(src)
    pairs = [(clean(d), clean(e), ln) for d, e, ln in p.pairs + js_pairs(src)]
    solo = [clean(s) for s in p.solo]
    de_all = ' '.join(d for d, _, _ in pairs)
    es_all = ' '.join(e for _, e, _ in pairs) + ' ' + ' '.join(solo)
    de_words = set(words(de_all))
    # Namen: gross, kein spanisches Wort, auf der Seite in beiden Sprachen
    # Name = im Spanischen mitten im Satz gross, steht auch im Deutschen, kein spanisches Wort
    all_words = set(words(de_all + ' ' + es_all))
    names = {w for w in set(caps(es_all)) if w in de_words and not is_es_word(w) and w.lower() not in all_words}
    rep = []
    for de, es, ln in pairs:
        if not es.strip():
            continue
        dw, ew = set(words(de)), set(words(es))
        for n in sorted(names & dw - ew):
            if LAND.get(n, '-') in es:      # Ländernamen werden übersetzt (Schweiz → Suiza)
                continue
            # Genitiv/Plural (Toms, Linas) zählt als gleich
            if not any(x in (n, n + 's', n + 'es') for x in ew):
                rep.append(f"  Zeile {ln}: Name «{n}» fehlt im Spanischen: «{es[:90]}»")
        for w in sorted(set(caps(es)) - dw - names):
            if is_es_word(w):
                continue
            near = [n for n in names if SequenceMatcher(None, w.lower(), n.lower()).ratio() >= 0.7 and not w.startswith(n)]
            if near:
                rep.append(f"  Zeile {ln}: «{w}» im Spanischen, ähnlich wie Name «{near[0]}». Gleicher Name?")
    unknown = {}
    if SPELL:
        for w in words(es_all):
            if len(w) < 3 or w in de_words or w.lower() in (x.lower() for x in names):
                continue
            unknown[w] = unknown.get(w, 0) + 1
        bad = unknown_words(list(unknown))
        unknown = {w: n for w, n in unknown.items() if w in bad and (w == w.lower() or w.lower() in unknown_words([w.lower()]))}
    print(f"\n=== {os.path.basename(path)}: {len(pairs)} Paare, {len(solo)} Spanisch ohne Paar")
    print(f"Namen auf der Seite: {', '.join(sorted(names)) or '–'}")
    print("Namen:" if rep else "Namen: ✅ keine Abweichung gefunden")
    for r in rep:
        print(r)
    if not SPELL:
        print("Rechtschreibung: übersprungen (apt-get install -y hunspell hunspell-es)")
    elif unknown:
        print(f"Rechtschreibung: {len(unknown)} Wörter unbekannt im Wörterbuch (von Auge prüfen, viele sind richtig):")
        print("  " + ', '.join(f"{w}" + (f" ({n}×)" if n > 1 else '') for w, n in sorted(unknown.items())))
    else:
        print("Rechtschreibung: ✅ alles im Wörterbuch")


if __name__ == '__main__':
    files = sys.argv[1:] or sorted(glob.glob(os.path.join(ROOT, '*.html')))
    for f in files:
        check(f)

#!/usr/bin/env python3
"""Vergleicht einen Test mit seiner Lösung: Steht alles auf der gleichen Seite und Zeile?

Die Lösung soll der Test mit eingefüllten Antworten sein. Beim Korrigieren legt die
Lehrperson beide nebeneinander. Darum darf sich im Lösungsdokument nichts verschieben:
keine Aufgabe auf eine andere Seite, keine Zeile nach unten, keine Spalte zur Seite.

Aufruf:
    python3 -I tools/lage_vergleich.py <Test.docx|pdf> <Loesung.docx|pdf> [--toleranz 2.5]

Word-Dateien werden mit LibreOffice in PDF umgewandelt (im Temp-Ordner).
Für jede Seite des Tests werden die Wörter des Tests in der Lösung gesucht
(in gleicher Reihenfolge) und ihre Lage verglichen. Wörter, die nur in der Lösung
stehen (die eingefüllten Antworten), werden nicht geprüft. Seiten, die die Lösung am
Schluss zusätzlich hat (Bewertung, Notenskala), werden nur gezählt.

Ausgabe: pro Seite «OK» oder die Stellen, die sich verschoben haben.
Exit-Code 0 = alles am gleichen Ort, 1 = Verschiebungen gefunden.
"""
import collections
import difflib
import html
import os
import re
import shutil
import subprocess
import sys
import tempfile

PT_MM = 25.4 / 72
BOXES = {c: '☐' for c in '☐☒☑✗✘'}   # leeres und angekreuztes Kästchen gelten als gleich
BLANK = re.compile(r'^[_.…·\-–]+$')   # Lücken-Striche: werden in der Lösung ersetzt, nicht vergleichen


def to_pdf(path, tmp):
    if path.lower().endswith('.pdf'):
        return path
    out = os.path.join(tmp, os.path.basename(path))
    os.makedirs(out, exist_ok=True)
    subprocess.run(['soffice', '--headless', '--convert-to', 'pdf', '--outdir', out, path],
                   check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, timeout=180)
    pdfs = [f for f in os.listdir(out) if f.endswith('.pdf')]
    if not pdfs:
        sys.exit(f'PDF-Umwandlung fehlgeschlagen: {path}')
    return os.path.join(out, pdfs[0])


def words(pdf):
    """Liste von Seiten, jede Seite eine Liste (wort, x, y) in Punkten."""
    xml = subprocess.run(['pdftotext', '-bbox', pdf, '-'], check=True,
                         capture_output=True, text=True).stdout
    pages = []
    for page in re.findall(r'<page[^>]*>(.*?)</page>', xml, re.S):
        ws = []
        for x0, y0, _x1, y1, w in re.findall(
                r'<word xMin="([\d.]+)" yMin="([\d.]+)" xMax="([\d.]+)" yMax="([\d.]+)">(.*?)</word>', page):
            w = html.unescape(w)
            if BLANK.match(w):
                continue
            w = BOXES.get(w, w)
            ws.append((w, float(x0), float(y1)))   # y1 = Grundlinie, stabil bei Schriftgrösse
        pages.append(ws)
    return pages


def context(ws, i, n=6):
    return ' '.join(w for w, _, _ in ws[max(0, i - 1):i + n])


def compare(test_pdf, sol_pdf, tol):
    tp, sp = words(test_pdf), words(sol_pdf)
    problems = 0
    print(f'Test: {len(tp)} Seiten · Lösung: {len(sp)} Seiten')
    if len(sp) < len(tp):
        print(f'❌ Die Lösung hat weniger Seiten als der Test ({len(sp)} statt {len(tp)}).')
        problems += 1
    for p, tws in enumerate(tp):
        nr = p + 1
        if not tws:
            print(f'Seite {nr}: (leer)')
            continue
        if p >= len(sp):
            print(f'❌ Seite {nr}: fehlt in der Lösung.')
            problems += 1
            continue
        sws = sp[p]
        sm = difflib.SequenceMatcher(a=[w for w, _, _ in tws], b=[w for w, _, _ in sws], autojunk=False)
        matched = [0] * len(tws)
        shifts = []          # (Index im Test, dx, dy)
        for a, b, size in sm.get_matching_blocks():
            for k in range(size):
                matched[a + k] = 1
                _, tx, ty = tws[a + k]
                _, sx, sy = sws[b + k]
                shifts.append((a + k, sx - tx, sy - ty))
        missing = [i for i, m in enumerate(matched) if not m]
        moved_v = [s for s in shifts if abs(s[2]) > tol]
        if 0 < len(moved_v) < 3:
            # einzelne Wörter: meist doppelte Wörter, die falsch zugeordnet wurden (z.B. in Tabellen)
            i, _, dy = moved_v[0]
            print(f'ℹ️  Seite {nr}: einzelnes Wort «{tws[i][0]}» {abs(dy) * PT_MM:.1f} mm anders, von Auge prüfen')
            moved_v = []
        # waagrecht nur melden, wenn ein Wort am Zeilenanfang (Spalte) wandert
        line_starts = {i for i in range(len(tws)) if i == 0 or abs(tws[i][2] - tws[i - 1][2]) > 1}
        moved_h = [s for s in shifts if s[0] in line_starts and abs(s[1]) > tol * 2]
        quote = len(shifts) / len(tws)
        if not moved_v and not moved_h and quote > 0.97:
            print(f'✅ Seite {nr}: OK ({len(shifts)} Wörter am gleichen Ort)')
            continue
        if missing and quote <= 0.97 and not moved_v and not moved_h:
            # alle fehlenden Wörter stehen auf der gleichen Seite der Lösung, nur in anderer Lesereihenfolge?
            rest = collections.Counter(w for w, _, _ in sws)
            rest.subtract(w for i, (w, _, _) in enumerate(tws) if matched[i])
            if all(rest[tws[i][0]] > 0 for i in missing):
                print(f'✅ Seite {nr}: OK, nur andere Lesereihenfolge (z.B. «{context(tws, missing[0])}»), keine Verschiebung')
                continue
        problems += 1
        print(f'❌ Seite {nr}: {len(shifts)} von {len(tws)} Wörtern gefunden')
        if moved_v:
            i, _, dy = moved_v[0]
            richtung = 'nach unten' if dy > 0 else 'nach oben'
            print(f'   – ab «{context(tws, i)}» ist der Text {abs(dy) * PT_MM:.1f} mm {richtung} verschoben '
                  f'({len(moved_v)} Wörter betroffen)')
        if moved_h:
            i, dx, _ = moved_h[0]
            print(f'   – Zeilenanfang «{context(tws, i)}» ist {abs(dx) * PT_MM:.1f} mm zur Seite verschoben '
                  f'({len(moved_h)} Zeilen betroffen)')
        if missing and quote <= 0.97:
            print(f'   – nicht auf dieser Seite gefunden, z.B. «{context(tws, missing[0])}» '
                  f'(Text auf eine andere Seite gerutscht oder geändert?)')
    extra = len(sp) - len(tp)
    if extra > 0:
        print(f'ℹ️  Die Lösung hat {extra} Seite(n) mehr (z.B. Bewertung und Notenskala am Schluss).')
    print('Ergebnis:', 'alles am gleichen Ort' if problems == 0 else f'{problems} Stelle(n) prüfen')
    return problems


def main():
    args = [a for a in sys.argv[1:] if not a.startswith('--')]
    tol = 2.5
    if '--toleranz' in sys.argv:
        tol = float(sys.argv[sys.argv.index('--toleranz') + 1])
        args = [a for a in args if a != str(sys.argv[sys.argv.index('--toleranz') + 1])]
    if len(args) != 2:
        sys.exit(__doc__)
    tmp = tempfile.mkdtemp()
    try:
        n = compare(to_pdf(args[0], tmp), to_pdf(args[1], tmp), tol)
    finally:
        shutil.rmtree(tmp, ignore_errors=True)
    sys.exit(1 if n else 0)


if __name__ == '__main__':
    main()

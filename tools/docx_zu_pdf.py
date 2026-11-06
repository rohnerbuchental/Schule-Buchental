#!/usr/bin/env python3
"""Word-Datei als PDF speichern, ohne dass Wingdings-Zeichen zu Buchstaben werden.

Auf dem Server fehlt die Schrift «Wingdings». Die Smileys der Selbsteinschätzung
(Wingdings J, K, L = ☺ 😐 ☹) erscheinen im PDF sonst als «J K L».
Das Skript ersetzt sie nur in einer Kopie durch Emoji-Smileys und macht daraus das PDF.
Die Word-Datei selbst bleibt unverändert.

Aufruf: python3 tools/docx_zu_pdf.py <Datei.docx> [<Ziel.pdf>]
"""
import os, re, shutil, subprocess, sys, tempfile, zipfile

WINGDINGS = {'J': '\U0001F642', 'K': '\U0001F610', 'L': '\U0001F641'}   # 🙂 😐 🙁
EMOJI_FONT = 'Noto Color Emoji'


def fix_xml(xml):
    def run(m):
        r = m.group(0)
        if 'w:ascii="Wingdings"' not in r:
            return r
        r2 = re.sub(r'<w:t([^>]*)>([^<]*)</w:t>',
                    lambda t: '<w:t%s>%s</w:t>' % (t.group(1), ''.join(WINGDINGS.get(c, c) for c in t.group(2))), r)
        return r2.replace('"Wingdings"', '"%s"' % EMOJI_FONT)
    return re.sub(r'<w:r\b[^>]*>.*?</w:r>', run, xml, flags=re.S)


def main():
    src = os.path.abspath(sys.argv[1])
    dst = os.path.abspath(sys.argv[2]) if len(sys.argv) > 2 else os.path.splitext(src)[0] + '.pdf'
    with tempfile.TemporaryDirectory() as tmp:
        copy = os.path.join(tmp, os.path.splitext(os.path.basename(dst))[0] + '.docx')
        with zipfile.ZipFile(src) as zin, zipfile.ZipFile(copy, 'w', zipfile.ZIP_DEFLATED) as zout:
            for item in zin.infolist():
                data = zin.read(item.filename)
                if item.filename.startswith('word/') and item.filename.endswith('.xml'):
                    data = fix_xml(data.decode('utf-8')).encode('utf-8')
                zout.writestr(item, data)
        subprocess.run(['soffice', '--headless', '--convert-to', 'pdf', '--outdir', tmp, copy],
                       check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        shutil.copy(os.path.join(tmp, os.path.splitext(os.path.basename(copy))[0] + '.pdf'), dst)
    print('PDF:', dst)


if __name__ == '__main__':
    main()

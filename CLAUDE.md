# Lernportal Schule Buchental

Statische Lernseiten (eine HTML-Datei pro Thema) für Sek-Schülerinnen und -Schüler.
`index.html` ist die Startseite und verlinkt jede Lernseite als Kachel.
Die Schüler bekommen nur die Startseite: https://rohnerbuchental.github.io/Schule-Buchental/ (GitHub Pages). Neue Seiten darum immer als Kachel in `index.html` eintragen.
Die Lehrperson (Repo-Besitzer) schreibt Deutsch (Schweiz) und will kurze, klare Antworten.

## Seiten
| Datei | Thema |
|---|---|
| `connected_3_scratch_trainingshub.html` | Informatik, Connected 3 «Abheben mit Algorithmen» (Scratch) |
| `Deutsch Novemberschnee.html` | Deutsch, Lektüre «Novemberschnee» |
| `Englisch open_world_2_unit_1.html` | Englisch, Open World 2 Unit 1 |
| `RZG Vulkane Erdbeben Tsunamis.html` | RZG, Dynamik der Erde, Test 2 (Vulkane, Erdbeben, Tsunamis) |

## Regeln für alle Seiten (immer einhalten)
- **Sprache:** Deutsch (Schweiz), immer «ss» statt «ß». Einfache Sätze für Schüler.
- **Zufall:** Alle Antwortmöglichkeiten werden bei jedem Laden gemischt: Radio-Buttons, Checkboxen, Auswahlmenüs, Drag-&-Drop-Bausteine und Tabellenzeilen. Ausnahme: reine Platznummern (1., 2., 3.) mit `data-noshuffle`.
- **Bedienung:** Drag & Drop muss auch auf Tablet und Handy gehen (Antippen, dann aufs Ziel tippen). Nichts darf auf 390 px Breite seitlich überlaufen.
- **Speichern:** Antworten im `localStorage`, jeder Zugriff in `try/catch`.
- **Start:** Seiten starten mit `DOMContentLoaded`, nicht mit `window.onload`. Sonst bleiben die Felder leer, solange Tailwind oder Schriften laden.
- **Bewertung:** Eine Stelle pro Seite (`TASKS` mit `max` und `score()`). Die Prüfen-Knöpfe und die Test-Simulation nutzen beide diese Stelle. Punktetotal nie von Hand eintragen.
- **Noten:** Schweizer Skala. Note = Punkte ÷ Total × 5 + 1, gerundet auf 0.1. Bestanden ab 60 % (Note 4.0).
- **Technik:** Eine Datei pro Seite, Tailwind über `cdn.tailwindcss.com`, Schrift Inter (Google Fonts). Keine weiteren Abhängigkeiten.

## Scratch-Hub: Besonderheiten
- Scratch-Blöcke nur mit den `.sb-*`-Klassen bauen (Scratch-3-Look: `.sb`, `.sb-hat`, `.sb-c`, `.sb-bool`, `.sb-num`, Farben `.sb-motion` usw.). Texte wie im deutschen Scratch 3 («gehe 10er-Schritt», «wiederhole 4 mal»). Keinen «Ende»-Block, den gibt es in Scratch nicht.
- Aufgabe 2 ist ein SVG-Ablaufdiagramm mit Drag & Drop (Felder `fs1`–`fs3`).
- Tab 4 hat nur UND/ODER: 7a leicht, 7b Smarthome, 7c Gartenbewässerung. Die Aufgaben zu «nicht» und zur «Notlandung» hat die Lehrperson bewusst gestrichen; nicht wieder einbauen.
- Test-Simulation: 30 Punkte, bestanden ab 18.

## RZG-Hub: Besonderheiten
- Grundlagen: Dossier «Dynamik der Erde» (Real) mit Lösungen der Lehrperson und Blatt «Lernziele Dynamik der Erde Teil 2» (Ich-kann-Checkliste, LZ1 bis LZ5) mit Musterlösungen, die sich aufs Dossier stützen.
- Die Seite deckt nur Teil 2 ab: Vulkan-Entstehung, Schild-/Schichtvulkan, Ausbruch, Erdbeben, Richterskala, Energie rechnen (×10 Ausschlag / ×32 Energie), Tsunamis. Teil 1 (Aufbau der Erde, Plattentektonik) war schon Test 1, nicht einbauen.
- Lernziel-Nummern auf der Seite wie auf dem Blatt (LZ1 bis LZ5). Jeder Punkt der Checkliste muss geübt werden.
- «Inaktive Vulkane» (Aufgabe 6) ist ein Zusatz aus dem Dossier. Steht nicht auf dem Lernziel-Blatt und kommt im Test nicht vor.
- Die Schüler füllen das Lernziel-Blatt auf Papier aus. Das Lernportal dient danach zum nochmaligen Üben für den Test. Reiter «Lernziel-Blatt» (`BLATT`): alle Ich-kann-Punkte mit Textfeld, Musterlösung zum Aufklappen und Häkchen «Das kann ich». Zählt nicht zu `TASKS`.
- Hilfe-Treppe im Reiter «Lernziel-Blatt» (`HELP`): 1 Tipp mit Wortkasten → 2 Satzanfänge einfügen → 3 Antwort prüfen (sucht Schlüsselwörter, Satzanfänge zählen nicht) → 4 Musterlösung, dazu Knopf «Theorie». Wunsch der Lehrperson: schwächere Schüler brauchen viel Hilfe, bevor sie die Lösung sehen. Bei neuen offenen Aufgaben (auch auf anderen Seiten) diese Hilfe-Stufen einbauen.
- Aufgaben sind Daten in `DEFS` (Blocktypen gaps, rows, mc, checks, dnd, num). `TASKS` wird daraus berechnet.

## Tests (Prüfungen)
- Echte Tests nie ins Repository und nie aufs Lernportal: Das Repo ist öffentlich, die Schüler könnten sie finden.
- Tests als Word-Datei (.docx) direkt an die Lehrperson geben, immer mit separater Lösung inkl. Punkteverteilung und Notenskala.
- Test-Aufgaben dürfen den Übungen ähnlich sein, aber nicht gleich (andere Bilder, Beispiele, Zahlen).

## Lehrplan (`lehrplan/`)
- Kompetenzen Zyklus 3 (Lehrplan Volksschule SG) als Markdown: Deutsch, Englisch, Medien und Informatik, RZG, Bildnerisches Gestalten. Übersicht in `lehrplan/README.md`.
- Nur mit `grep` suchen, z.B. `grep -n "MI.2.2" lehrplan/medien-informatik.md`. Nie ganze Dateien lesen.
- Jede neue Aufgabe bekommt den passenden Code im Kommentar: `<!-- Aufgabe 3: Schleifen | MI.2.2.h -->`. Nur Codes verwenden, die in `lehrplan/` stehen.
- Entscheid Lehrperson: Repo bleibt öffentlich, die Lehrplan-Auszüge dürfen drin sein (Texte sind auf sg.lehrplan.ch frei zugänglich). Weitere Fächer vorerst nicht; bei Bedarf von sg.lehrplan.ch holen.

## Agenten (`.claude/agents/`)
- `aufgaben-ersteller`: baut neue Lernseiten oder Aufgaben nach den Regeln oben und trägt die Kachel in `index.html` ein.
- `regel-pruefer`: prüft Seiten gegen diese Regeln und führt `tools/check.js` aus. Ändert nichts. Nach jeder grösseren Änderung einsetzen.

## Arbeitsablauf
1. Änderungen nur hier im Repository machen. Keine Kopien mit anderen KI-Tools bearbeiten und wieder hochladen, sonst entstehen zwei Versionen.
2. Nicht ganze Dateien lesen: mit `grep -n "<!-- Aufgabe"` die Stelle suchen und nur diesen Abschnitt lesen (spart Tokens).
3. Nach jeder Änderung `node tools/check.js` ausführen (prüft alle Seiten auf JS-Fehler und Überlauf am Handy).
4. Der Lehrperson eine Vorschau als Artifact-Link geben (Tailwind dafür als CSS einbetten).
5. Auf einen Branch committen und pushen, dann Pull Request auf `main`.
6. **Neue Wünsche oder Entscheidungen der Lehrperson hier in dieser Datei festhalten**, damit sie beim nächsten Mal nicht neu erklärt werden müssen.

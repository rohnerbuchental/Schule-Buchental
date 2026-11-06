# Lernportal Schule Buchental

Statische Lernseiten (eine HTML-Datei pro Thema) für Sek-Schülerinnen und -Schüler.
`index.html` ist die Startseite und verlinkt jede Lernseite als Kachel.
Die Schüler bekommen nur die Startseite: https://rohnerbuchental.github.io/Schule-Buchental/ (GitHub Pages). Neue Seiten darum immer als Kachel in `index.html` eintragen.
Die Lehrperson (Repo-Besitzer) schreibt Deutsch (Schweiz) und will kurze, klare Antworten.

**Dieses Repo ist öffentlich** (GitHub Pages geht mit dem Gratis-Konto nur so). Darum steht hier nichts über die Klasse, keine Tests, keine Lösungen, keine Namen.
Alles andere liegt in der **privaten Ablage** (siehe unten).

## Seiten
| Datei | Thema |
|---|---|
| `connected_3_scratch_trainingshub.html` | Informatik, Connected 3 «Abheben mit Algorithmen» (Scratch) |
| `Deutsch Novemberschnee.html` | Deutsch, Lektüre «Novemberschnee» |
| `Englisch open_world_2_unit_1.html` | Englisch, Open World 2 Unit 1 |
| `Englisch open_world_2_unit_2.html` | Englisch, Open World 2 Unit 2 «Weird and wonderful games» (Wörter-Lernpfad, Grammatik-Pfad present continuous) |
| `RZG Vulkane Erdbeben Tsunamis.html` | RZG, Dynamik der Erde, Test 2 (Vulkane, Erdbeben, Tsunamis) |

Besonderheiten jeder Seite stehen in `docs/seiten.md`. Vor der Arbeit an einer Seite nur ihren Abschnitt lesen. Die didaktischen Grundsätze mit Quellen stehen in `docs/didaktik.md`.

## Regeln für alle Seiten (immer einhalten)
- **Sprache:** Deutsch (Schweiz), immer «ss» statt «ß». Einfache Sätze für Schüler.
- **Zufall:** Alle Antwortmöglichkeiten werden bei jedem Laden gemischt: Radio-Buttons, Checkboxen, Auswahlmenüs, Drag-&-Drop-Bausteine und Tabellenzeilen. Ausnahme: reine Platznummern (1., 2., 3.) mit `data-noshuffle`. Wo es Sinn macht, wird auch die Reihenfolge der Teilfragen (a, b, c …) und der Abschnitte in Lückentexten gemischt. Die Buchstaben a), b), c) setzt die Seite danach automatisch, darum nie fest in den Fragetext schreiben.
- **Nochmals üben:** Jede Aufgabe hat den Knopf «🔀 Nochmals üben». Er leert nur diese Aufgabe und mischt sie neu.
- **Hilfe (Wunsch Lehrperson):** Jede Aufgabe hat «💡 Tipp» (Leitfragen oder Vergleich aus dem Alltag; nie die Lösung oder fast den Wortlaut der richtigen Antwort) und «📖 Theorie» (springt zur passenden Theorie). Theorie immer kurz und zugeklappt. Offene Textfragen bekommen die Hilfe-Treppe: 1 Tipp mit Wortkasten → 2 Satzanfänge → 3 Antwort prüfen (Schlüsselwörter) → 4 Musterlösung.
- **Bedienung:** Drag & Drop muss auch auf Tablet und Handy gehen (Antippen, dann aufs Ziel tippen). Nichts darf auf 390 px Breite seitlich überlaufen.
- **Speichern:** Antworten im `localStorage`, jeder Zugriff in `try/catch`.
- **Start:** Seiten starten mit `DOMContentLoaded`, nicht mit `window.onload`.
- **Bewertung:** Eine Stelle pro Seite (`TASKS` mit `max` und `score()`). Die Prüfen-Knöpfe und die Test-Simulation nutzen beide diese Stelle. Punktetotal nie von Hand eintragen.
- **Noten:** Schweizer Skala. Note = Punkte ÷ Total × 5 + 1, gerundet auf 0.1. Bestanden ab 60 % (Note 4.0).
- **Technik:** Eine Datei pro Seite, Tailwind über `cdn.tailwindcss.com`, Schrift Inter (Google Fonts). Keine weiteren Abhängigkeiten.
- **Niveau:** Vor neuen Aufgaben das Niveau-Profil des Fachs in der privaten Ablage lesen (`Niveau-Profil.md`).
- **Nicht überladen (Wunsch Lehrperson):** Wenige, klare Aufgaben, die genau das üben, was im Test kommt. Lieber eine einfache Seite als viele Spiele. Spiel-Elemente nur leicht (Fortschritt, Medaille).
- **Angstfrei (Wunsch Lehrperson, sehr wichtig):** Kein Zeitdruck, keine Rangliste, Fehler kosten nichts (Aufgabe kommt nochmals), «Weiss ich nicht» erlaubt. Sprache «Noch nicht ganz» statt «Falsch», Gelb statt Rot. Probetests sind Übung.
- **Begründet mit Quellen (Wunsch Lehrperson):** Jede Übungsform folgt `docs/didaktik.md` (Abrufen üben, verteiltes Üben, sofortige Rückmeldung, erst erkennen dann selber bilden, wenig auf einmal). Eine neue Übungsform nur mit Quelle; die Begründung dort nachtragen. Der Lehrperson bei neuen Aufgaben kurz sagen, welches Prinzip dahinter steht.
- **Für Lernende, die schnell aufgeben (Wunsch Lehrperson):** Vor jeder neuen Aufgabe recherchieren (WebSearch), welche Übungsform für dieses Lernziel bei schwächeren Lernenden am besten belegt ist, und die Checkliste in `docs/didaktik.md` (Abschnitt 1b) abarbeiten: leichter Einstieg, kleine Etappen, sichtbarer Fortschritt, Hilfe vor Lösung, eine Sache auf einen Blick, etwa 80 % Erfolg beim Üben.

## Private Ablage (alles, was nicht öffentlich sein darf)
- Privates Repo `rohnerbuchental/Schule-Buchental-Material`, geklont nach `/home/user/schule-buchental-material` (bei Bedarf mit `add_repo` verbinden, dann `register_repo_root`).
- Dort liegen: Tests, Lösungen, Lösungshefte, Arbeitsblätter, Schreibanlässe, Planungen, Vorlagen der Lehrperson, das Niveau der Klasse.
- **Für alles ausser dem Lernportal gelten die Regeln in der `CLAUDE.md` der privaten Ablage.** Dort auch `OFFEN.md` (Stand, offene Punkte; nach einem /clear dort weitermachen) und `Niveau-Profil.md`.
- Nie Tests, Lösungen, Einschätzungen zur Klasse oder Namen in dieses Repo: GitHub Pages veröffentlicht jede Datei.
- Claude arbeitet auf GitHub mit dem Konto `mercilessmarshmallow` (Collaborator im privaten Repo).

## Lehrplan (`lehrplan/`)
- Kompetenzen Zyklus 3 (Lehrplan Volksschule SG) als Markdown: Deutsch, Englisch, Medien und Informatik, RZG, Bildnerisches Gestalten. Übersicht in `lehrplan/README.md`.
- Nur mit `grep` suchen, z.B. `grep -n "MI.2.2" lehrplan/medien-informatik.md`. Nie ganze Dateien lesen.
- Jede neue Aufgabe bekommt den passenden Code im Kommentar: `<!-- Aufgabe 3: Schleifen | MI.2.2.h -->`. Nur Codes verwenden, die in `lehrplan/` stehen.
- Die Lehrplan-Auszüge dürfen hier stehen (frei zugänglich auf sg.lehrplan.ch).

## Agenten (`.claude/agents/`)
- `aufgaben-ersteller`: baut neue Lernseiten oder Aufgaben nach den Regeln oben und trägt die Kachel in `index.html` ein.
- `regel-pruefer`: prüft Seiten gegen diese Regeln und führt `tools/check.js` aus. Ändert nichts. Nach jeder grösseren Änderung einsetzen.
- `test-ersteller`: macht einen Papiertest als Word mit separater Lösung und Notenskala. Arbeitet im Scratchpad; Ergebnis in die private Ablage.
- `niveau-pruefer`: prüft Test oder Arbeitsblatt auf das Niveau der Klasse und auf genug Luft zwischen den Aufgaben. Ändert nichts.
- `loesungs-pruefer`: vergleicht Test oder Arbeitsblatt mit der Lösung (`tools/lage_vergleich.py` und von Auge). Ändert nichts.

## Arbeitsablauf
1. Änderungen am Lernportal nur hier im Repository machen. Keine Kopien mit anderen KI-Tools bearbeiten und wieder hochladen.
2. Nicht ganze Dateien lesen: mit `grep -n "<!-- Aufgabe"` die Stelle suchen und nur diesen Abschnitt lesen (spart Tokens).
3. Nach jeder Änderung `node tools/check.js` ausführen (JS-Fehler, Überlauf am Handy). `check.js` blockiert Tailwind; bei Layout-Änderungen zusätzlich mit lokal gebautem Tailwind (tailwindcss@3 im Scratchpad) auf 390 px prüfen, mit allen Tipp-/Lösungsboxen offen.
4. Der Lehrperson eine Vorschau als Artifact-Link geben (Tailwind dafür als CSS einbetten).
5. Auf einen Branch committen und pushen, dann Pull Request auf `main`.
6. **Neue Wünsche der Lehrperson festhalten:** zum Lernportal hier (oder in `docs/seiten.md`), alles andere in der privaten Ablage (`CLAUDE.md`, `Niveau-Profil.md`, `OFFEN.md`).

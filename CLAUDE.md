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
- **Zufall:** Alle Antwortmöglichkeiten werden bei jedem Laden gemischt: Radio-Buttons, Checkboxen, Auswahlmenüs, Drag-&-Drop-Bausteine und Tabellenzeilen. Ausnahme: reine Platznummern (1., 2., 3.) mit `data-noshuffle`. Wo es Sinn macht, wird auch die Reihenfolge der Teilfragen (a, b, c …) und der Abschnitte in Lückentexten gemischt. Die Buchstaben a), b), c) setzt die Seite danach automatisch, darum nie fest in den Fragetext schreiben. So kann man die gleiche Aufgabe gut zweimal machen.
- **Nochmals üben:** Jede Aufgabe hat den Knopf «🔀 Nochmals üben». Er leert nur diese Aufgabe und mischt sie neu.
- **Hilfe (Wunsch Lehrperson, für schwächere Schüler):** Jede Aufgabe hat «💡 Tipp» (Leitfragen oder Vergleich aus dem Alltag; nie die Lösung oder fast den Wortlaut der richtigen Antwort) und «📖 Theorie» (springt zur passenden Theorie). Theorie immer kurz und zugeklappt, zum Aufklappen bei Bedarf: Die Schüler sollen nicht von Text erschlagen werden (Wunsch Lehrperson). Offene Textfragen bekommen die Hilfe-Treppe: 1 Tipp mit Wortkasten → 2 Satzanfänge → 3 Antwort prüfen (Schlüsselwörter) → 4 Musterlösung.
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
- Jede Aufgabe hat Prüfen, «💡 Tipp» und «🔀 Nochmals üben». «📖 Theorie» bei allen Aufgaben: Reiter 1–3 haben je eine kurze Theorie-Box zum Aufklappen (`theory-basics`, `theory-loops`, `theory-custom`), 7a–7c springen zur UND/ODER-Erklärung. Teilfragen von 1, 3, 4, 5, 8 werden gemischt; Ablaufdiagramm, Quadrat-Reihenfolge und Skripte nicht. Die Aufgaben stehen auf der Seite in der Reihenfolge 1, 2, 3, 4, 6, 5, 8, 7a, 7b, 7c.
- Skript-Bereiche sind höchstens so breit wie die Karte und scrollen innen (sonst Überlauf auf dem Handy).

## Deutsch-Hub (Novemberschnee): Besonderheiten
- Aufgaben 1–8 über die ganze Seite durchnummeriert. 1, 2, 3, 5, 7 geben Punkte (34 P., aus `TASKS`). 4, 6, 8 sind offene Fragen mit Hilfe-Treppe und Musterlösung, ohne Punkte. Keine Test-Simulation.
- Gespeichert unter `ns_…` (offene Texte: `ns_open`).
- Von der Lehrperson bestätigt: Meinungsfrage 6 «Ist Lina mitschuldig?» bleibt. In Aufgabe 8 stehen die Beispiele (147, KESB, Schlupfhuus …) nur in der Musterlösung, nicht in der Frage.

## Englisch-Hub (Open World 2, Unit 1): Besonderheiten
- `TASKS` hat einen Eintrag pro 5er-Block (Übungen, total 210) und pro Probetest-Teil A/B/C (30 P., bestanden ab 18). Probetest-Teile kann man einzeln prüfen (von der Lehrperson gewünscht); die Lösung zeigt erst «Prüfung abgeben».
- Sätze und die Wörter in `[ … / … ]` werden gemischt. Tipps auf Deutsch, Beispiele auf Englisch.

## RZG-Hub: Besonderheiten
- Grundlagen: Dossier «Dynamik der Erde» (Real) mit Lösungen der Lehrperson und Blatt «Lernziele Dynamik der Erde Teil 2» (Ich-kann-Checkliste, LZ1 bis LZ5) mit Musterlösungen, die sich aufs Dossier stützen.
- Die Seite deckt nur Teil 2 ab: Vulkan-Entstehung, Schild-/Schichtvulkan, Ausbruch, Erdbeben, Richterskala, Energie rechnen (×10 Ausschlag / ×32 Energie), Tsunamis. Teil 1 (Aufbau der Erde, Plattentektonik) war schon Test 1, nicht einbauen.
- Lernziel-Nummern auf der Seite wie auf dem Blatt (LZ1 bis LZ5). Jeder Punkt der Checkliste muss geübt werden.
- «Inaktive Vulkane» (Aufgabe 6) ist ein Zusatz aus dem Dossier. Steht nicht auf dem Lernziel-Blatt und kommt im Test nicht vor. Darum `extra: true`: wird geübt und geprüft, zählt aber nicht in der Test-Simulation (73 P., bestanden ab 44).
- Die Schüler füllen das Lernziel-Blatt auf Papier aus. Das Lernportal dient danach zum nochmaligen Üben für den Test. Reiter «Lernziel-Blatt» (`BLATT`): alle Ich-kann-Punkte mit Textfeld, Musterlösung zum Aufklappen und Häkchen «Das kann ich». Zählt nicht zu `TASKS`.
- Hilfe-Treppe im Reiter «Lernziel-Blatt» (`HELP`): 1 Tipp mit Wortkasten → 2 Satzanfänge einfügen → 3 Antwort prüfen (sucht Schlüsselwörter, Satzanfänge zählen nicht) → 4 Musterlösung, dazu Knopf «Theorie». Wunsch der Lehrperson: schwächere Schüler brauchen viel Hilfe, bevor sie die Lösung sehen. Bei neuen offenen Aufgaben (auch auf anderen Seiten) diese Hilfe-Stufen einbauen.
- Aufgaben sind Daten in `DEFS` (Blocktypen gaps, rows, mc, checks, dnd, num). `TASKS` wird daraus berechnet.

## Tests (Prüfungen)
- Echte Tests nie ins Repository und nie aufs Lernportal: Das Repo ist öffentlich, die Schüler könnten sie finden.
- Tests als Word-Datei (.docx) direkt an die Lehrperson geben, immer mit separater Lösung inkl. Punkteverteilung und Notenskala. Danach in der privaten Ablage speichern (siehe unten).
- **Lösung = Test oder Arbeitsblatt mit Antworten am gleichen Ort** (Wunsch Lehrperson, sehr wichtig, gilt für alle neuen Tests und Arbeitsblätter): Das Lösungsblatt sieht genau gleich aus wie das Blatt der Schüler, mit der gleichen Struktur. Die Antworten stehen in Rot genau in den Lücken, damit die Lehrperson beim Korrigieren nichts suchen muss. Keine Aufgabe rutscht auf eine andere Seite. Bei Tests kommen Bewertung, Kompetenz-Grenzen und Notenskala als letzte Seite dazu. Vorbild: Lösung Englischtest Unit 1 in der privaten Ablage (so ist es richtig, nicht mehr ändern). Bestehende Dokumente nicht nachträglich umbauen. Danach `loesungs-pruefer` einsetzen.
- Test-Aufgaben dürfen den Übungen ähnlich sein, aber nicht gleich (andere Bilder, Beispiele, Zahlen).
- Lückentexte mit Auswahl (z.B. Konjunktionen): Jede Lücke darf nur eine richtige Lösung haben. Vor dem Abgeben jede Lücke mit allen Wörtern der Auswahl durchprobieren. Passt noch ein anderes Wort, die Lücke umschreiben (Wunsch Lehrperson: Englischtest Unit 1, Aufgabe 4 Nr. 9, dort passte auch «because» statt «so that»). Lösungen der Lehrperson ebenso prüfen und Alternativen in der Lösung als «auch richtig» angeben.
- Kompetenznachweise Englisch (10 Punkte pro Kompetenz): erreicht ab 6, gut ab 8, sehr gut ab 9 Punkten (Entscheid Lehrperson; «sehr gut» soll wirklich sehr gut sein, darum nicht tiefer).

## Lösungshefte (Wunsch Lehrperson)
- Lösungen zu Dossiers kommen nicht aufs Lernportal. Sie gehen als Word (zum Anpassen) und PDF (zum Austeilen) direkt an die Lehrperson und kommen in die private Ablage.
- Layout zum Selbstkorrigieren: Titelseite «So korrigierst du», ein farbiges Band pro Kapitel, Aufgaben mit der gleichen Nummer wie im Dossier, «✔» für die richtige Antwort, gelbe Kästchen «☐ Das muss drin sein» bei Antworten in eigenen Worten, «✎ Eigene Antwort», wo es kein Richtig oder Falsch gibt.
- Gleiche Struktur in allen Lösungsheften (Wunsch Lehrperson): Jede «Musterantwort:» hat darunter immer das gelbe Kästchen «Das muss drin sein». In Tabellen sind die Lösungswörter immer fett und blau.
- Fehler in den Lösungen der Lehrperson nicht stillschweigend übernehmen: korrigieren und der Lehrperson melden.

## Klasse und Schreibanlässe (Deutsch)
- Die Klasse der Lehrperson ist eine **Realklasse mit eher schwachen Schülern**: Anweisungen immer ganz einfach (kurze Sätze, klare Schritte, Hilfen wie Satzanfänge, Ideen und Wortkasten). Schwierigere Aufgaben macht nur die Sek-Parallelklasse.
- Die Schüler sind sehr schwach: Das Deutsch-Lehrmittel überfordert die meisten, auch in Version G. Aufträge darum stark kürzen und vereinfachen (weniger Aufgaben, mehr Zeit pro Schritt, Vorlagen, Wortkasten, Satzanfänge).
- **Planung Deutsch:** pro Woche 2 Lektionen Unterricht und 1 SOL-Auftrag (selbständiges Arbeiten). Lehrmittel: Buch und Themenheft (Version G) von Klett und Balmer. Planung und Beurteilung kompetenzorientiert nach Lehrplan 21 SG, Beurteilung in 4 Stufen (nicht erreicht – erreicht – gut – sehr gut). Kapitel B «Bedeutende Persönlichkeiten»: Malala ist erledigt. Poetry-Slam (W2) macht die Klasse nicht. Grobplanung B und W1 liegt in der privaten Ablage unter `Deutsch Planung/`.
- Schreibanlässe auf der Word-Vorlage der Lehrperson (eine Seite): «Schreibanlass N: Datum», Titel, Auftrag, Hilfe-Kasten «So gehst du vor» (Einleitung – Hauptteil – Schluss mit Anzahl Sätzen und Satzanfängen), danach die Checkliste der Lehrperson unverändert. Umfang immer 10–20 Sätze, Rhythmus 2 Wochen.
- Schreibanlässe sind Unterrichtsmaterial, nicht fürs Lernportal: als Word (und PDF) direkt an die Lehrperson.
- Zu jedem Schreibanlass gehört ein **Korrektur-Prompt für die KI** auf Seite 2 des Word-Dokuments (grauer Kasten, darüber «So geht es: Kopiere den ganzen Text … füge deinen eigenen Text darunter ein»). Aufbau wie der Prompt der Lehrperson: «Hier ist mein Text. Der Auftrag war: Schreibanlass N – Titel», Textsorte, Umfang (10 bis 20 Sätze), Aufgabe, Kriterien passend zum Auftrag; danach immer gleich: korrigieren ohne Stil zu ändern und Änderungen fett, wichtigster Fehlerschwerpunkt, Regel in max. 2 einfachen Sätzen, Tabelle mit bis zu 3 Beispielen (falsch / richtig), inhaltliche Rückmeldung in genau 1 Satz, einfache Sprache für 14-Jährige. Immer den Satz «Wir schreiben Schweizer Hochdeutsch: «ss» statt «ß» ist richtig und kein Fehler.» einbauen.

## Private Ablage (Material, das nicht aufs Lernportal gehört)
- Tests, Lösungen, Lösungshefte, Schreibanlässe und die Originale/Vorlagen der Lehrperson liegen im **privaten Repo `rohnerbuchental/Schule-Buchental-Material`**. Nie ins öffentliche Repo `Schule-Buchental`: GitHub Pages veröffentlicht jede Datei darin.
- Claude arbeitet auf GitHub mit dem Konto `mercilessmarshmallow` (zweites Konto der Lehrperson). Es ist Collaborator im privaten Repo; ohne das meldet GitHub beim Push «repository not found».
- Zu Beginn einer Sitzung bei Bedarf mit `add_repo` verbinden und nach `/home/user/schule-buchental-material` klonen. Ordner pro Fach/Thema, z.B. `RZG Dynamik der Erde/Test Teil 2/`. Neben jedem Dokument unter `_quelle/` das Erstell-Skript und die Bilder ablegen, damit man es später anpassen kann. Übersicht in der `README.md` dort.
- Direkt auf `main` committen und pushen (reines Archiv, keine Pull Requests nötig).
- Die Lehrperson hat zusätzlich in ihrem OneDrive den Ordner «Schule Buchental Material» (Unterordner «RZG Dynamik der Erde», «Deutsch Schreibanlässe», «Vorlagen»). Word/PDF über den OneDrive-Connector hochzuladen ist nicht praktikabel; dort legt die Lehrperson die Dateien selbst ab.

## Lehrplan (`lehrplan/`)
- Kompetenzen Zyklus 3 (Lehrplan Volksschule SG) als Markdown: Deutsch, Englisch, Medien und Informatik, RZG, Bildnerisches Gestalten. Übersicht in `lehrplan/README.md`.
- Nur mit `grep` suchen, z.B. `grep -n "MI.2.2" lehrplan/medien-informatik.md`. Nie ganze Dateien lesen.
- Jede neue Aufgabe bekommt den passenden Code im Kommentar: `<!-- Aufgabe 3: Schleifen | MI.2.2.h -->`. Nur Codes verwenden, die in `lehrplan/` stehen.
- Entscheid Lehrperson: Repo bleibt öffentlich, die Lehrplan-Auszüge dürfen drin sein (Texte sind auf sg.lehrplan.ch frei zugänglich). Weitere Fächer vorerst nicht; bei Bedarf von sg.lehrplan.ch holen.

## Agenten (`.claude/agents/`)
- `aufgaben-ersteller`: baut neue Lernseiten oder Aufgaben nach den Regeln oben und trägt die Kachel in `index.html` ein.
- `regel-pruefer`: prüft Seiten gegen diese Regeln und führt `tools/check.js` aus. Ändert nichts. Nach jeder grösseren Änderung einsetzen.
- `loesungs-pruefer`: vergleicht Test oder Arbeitsblatt mit der Lösung (`tools/lage_vergleich.py` und von Auge): gleiche Seiten, gleiche Struktur, Antworten in den Lücken? Ändert nichts. Nach jeder neuen Lösung einsetzen.
- `test-ersteller`: macht aus einer Lernseite (und den Unterlagen der Lehrperson) einen Papiertest als Word mit separater Lösung und Notenskala. Arbeitet im Scratchpad, nie im öffentlichen Repo; das Ergebnis kommt danach in die private Ablage.

## Arbeitsablauf
1. Änderungen nur hier im Repository machen. Keine Kopien mit anderen KI-Tools bearbeiten und wieder hochladen, sonst entstehen zwei Versionen.
2. Nicht ganze Dateien lesen: mit `grep -n "<!-- Aufgabe"` die Stelle suchen und nur diesen Abschnitt lesen (spart Tokens).
3. Nach jeder Änderung `node tools/check.js` ausführen (prüft alle Seiten auf JS-Fehler und Überlauf am Handy). Achtung: `check.js` blockiert Tailwind und sieht darum nicht jeden Überlauf. Bei Layout-Änderungen zusätzlich mit lokal gebautem Tailwind (tailwindcss@3 im Scratchpad) auf 390 px prüfen, mit allen Tipp-/Lösungsboxen offen.
4. Der Lehrperson eine Vorschau als Artifact-Link geben (Tailwind dafür als CSS einbetten).
5. Auf einen Branch committen und pushen, dann Pull Request auf `main`.
6. **Neue Wünsche oder Entscheidungen der Lehrperson hier in dieser Datei festhalten**, damit sie beim nächsten Mal nicht neu erklärt werden müssen.

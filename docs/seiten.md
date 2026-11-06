# Besonderheiten der einzelnen Lernseiten

Vor der Arbeit an einer Seite nur ihren Abschnitt lesen (`grep -n "^## " docs/seiten.md`).

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

## Englisch-Hub Unit 2: Besonderheiten
- **Wunsch Lehrperson: einfach, nicht überladen.** Die Seite übt genau das, was im Wörtertest kommt: Deutsch → Englisch und Englisch → Deutsch. Keine weiteren Spiele dazubauen.
- Aufbau: 1 Teil wählen (Teil 1 = Language Companion S. 12, 26 Wörter; Teil 2 = S. 13 inkl. Focus, 30 Wörter) · 2 Üben (ein Wort nach dem anderen, 10 pro Runde, Richtung wählbar, falsche Wörter kommen am Schluss nochmals) · 3 Wörtertest (10 × Deutsch → Englisch, 10 × Englisch → Deutsch, Note).
- Spiel-Elemente nur leicht: Fortschrittsbalken «Das kannst du schon» pro Richtung (letzte Antwort richtig), Serie 🔥, Medaille am Rundenende und beim Test.
- Wörter in `WORD_TEXT` (eine Zeile «englisch | deutsch»). `EXTRA`: weitere englische Schreibweisen (`alt`), Zusatz zur Frage (`hint`), `noType` = langer Ausdruck, nur Englisch → Deutsch. `SAME`: gleiche Bedeutung, beide richtig. `FAMILY`: im Test nie in Teil A und B zugleich. `DE_ALT`: weitere richtige deutsche Antworten; dazu Knopf «meine Antwort bedeutet dasselbe» bei Englisch → Deutsch.
- Prüfung: Gross/Klein egal, ä = ae = a, ß = ss, Artikel und «to» am Anfang egal.
- Gespeichert unter `ow2u2_words` (Teil, Richtung, «kann ich» pro Wort, beste Test-Medaille, Test-Antworten). Der Stand gilt nur auf dem Gerät und im Browser, wo geübt wurde.

## RZG-Hub: Besonderheiten
- Grundlagen: Dossier «Dynamik der Erde» mit Lösungen der Lehrperson und Blatt «Lernziele Dynamik der Erde Teil 2» (Ich-kann-Checkliste, LZ1 bis LZ5) mit Musterlösungen, die sich aufs Dossier stützen.
- Die Seite deckt nur Teil 2 ab: Vulkan-Entstehung, Schild-/Schichtvulkan, Ausbruch, Erdbeben, Richterskala, Energie rechnen (×10 Ausschlag / ×32 Energie), Tsunamis. Teil 1 (Aufbau der Erde, Plattentektonik) war schon Test 1, nicht einbauen.
- Lernziel-Nummern auf der Seite wie auf dem Blatt (LZ1 bis LZ5). Jeder Punkt der Checkliste muss geübt werden.
- «Inaktive Vulkane» (Aufgabe 6) ist ein Zusatz aus dem Dossier. Steht nicht auf dem Lernziel-Blatt und kommt im Test nicht vor. Darum `extra: true`: wird geübt und geprüft, zählt aber nicht in der Test-Simulation (73 P., bestanden ab 44).
- Die Schüler füllen das Lernziel-Blatt auf Papier aus. Das Lernportal dient danach zum nochmaligen Üben für den Test. Reiter «Lernziel-Blatt» (`BLATT`): alle Ich-kann-Punkte mit Textfeld, Musterlösung zum Aufklappen und Häkchen «Das kann ich». Zählt nicht zu `TASKS`.
- Hilfe-Treppe im Reiter «Lernziel-Blatt» (`HELP`): 1 Tipp mit Wortkasten → 2 Satzanfänge einfügen → 3 Antwort prüfen (sucht Schlüsselwörter, Satzanfänge zählen nicht) → 4 Musterlösung, dazu Knopf «Theorie». Wunsch der Lehrperson: viel Hilfe, bevor die Lösung kommt. Bei neuen offenen Aufgaben (auch auf anderen Seiten) diese Hilfe-Stufen einbauen.
- Aufgaben sind Daten in `DEFS` (Blocktypen gaps, rows, mc, checks, dnd, num). `TASKS` wird daraus berechnet.

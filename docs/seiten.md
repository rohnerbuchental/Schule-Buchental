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
- **Wunsch Lehrperson: einfach, nicht überladen, schnell zum Ziel.** Im Wörtertest kommt Deutsch → Englisch und Englisch → Deutsch. Reiter «Wörter»: nur Lernpfad und Wörtertest. Reiter «Grammatik»: nur der Grammatik-Pfad. Keine weiteren Spiele dazubauen.
- Teil 1 = Language Companion S. 12 (26 Wörter), Teil 2 = S. 13 inkl. Focus (30 Wörter).
- **Lernpfad** (wie Quizlet «Lernen»): Jedes Wort hat 4 Stufen: 1 Englisch → Deutsch auswählen, 2 Deutsch → Englisch auswählen, 3 Englisch → Deutsch schreiben, 4 Deutsch → Englisch schreiben. Richtig = eine Stufe höher, falsch = kommt nach 2 anderen Wörtern nochmals. Immer nur 7 Wörter gleichzeitig (`ACTIVE_N`); gemeistert ⭐ = alle Stufen. Lange Ausdrücke (`noType`) ohne Stufe 4. Richtig = automatisch weiter (Auswahl nach 0.7 s, Schreiben nach 1.1 s). Ohne Fehler 104 Antworten für Teil 1 (ca. 10 Minuten). **Wiederholen** (successive relearning, `REVIEW_DAYS` = 1 und 3 Tage): Gemeisterte Wörter kommen je einmal zum Schreiben; vergessen = zurück auf Stufe 3. Begründung mit Quellen: `docs/didaktik.md`.
- Auswahl-Ablenker: nie aus `SAME` (ähnliche Bedeutung) oder `FAMILY` (Wortfamilie). Schreiben: `SAME_TYPE` gilt gegenseitig als richtig, `DE_ALT` = weitere richtige deutsche Antworten, dazu im Lernpfad (nicht im Test) der Knopf «meine Antwort bedeutet dasselbe». Mehrere Bedeutungen («Wettbewerb, Wettkampf») sind richtig, wenn jede stimmt.
- **Wörtertest:** 10 × Deutsch → Englisch (ohne `noType`) und 10 × Englisch → Deutsch, 20 P., bestanden ab 12. Kein Selbst-Korrigieren. Teil B zeigt nie ein Wort aus `SAME_TYPE` oder `FAMILY` eines Teil-A-Worts.
- Prüfung: **Gross-/Kleinschreibung zählt** (Wunsch Lehrperson, wie im Test). **«Fast richtig!»** (Wunsch Lehrperson, `missInfo`, `gMiss`): wenn nur Gross/Klein, nur ein Buchstabe (Abstand 1, ab 4 Buchstaben) oder nur die Endung anders ist (z.B. brilliant statt brilliantly, «is visit»). Mit kurzem Hinweis (Nomen gross / -ly / -ing / genau abschreiben). Zählt noch nicht als richtig, das Wort kommt nochmals; «meine Antwort bedeutet dasselbe» erscheint dann nicht. Im Wörtertest: «Fast richtig!», aber 0 Punkte. Sonst egal: ä = ae = a, ß = ss, Artikel und «to» am Anfang, Akzente. Gilt auch für das Schreiben im Grammatik-Pfad.
- Angstfrei und für Lernende, die schnell aufgeben: «Noch nicht ganz» statt «Falsch», Gelb statt Rot. Fortschrittsbalken nach Stufen (wächst mit jedem richtigen Schritt). Nach `ETAPPE_N` = 10 Antworten «Etappe geschafft» mit «Weiter üben» oder «Für heute fertig». Beim Schreiben zuerst «Hilfe: erster Buchstabe». Wörtertest zugeklappt, bis «Wörtertest starten» (`testOpen`), dann «nur zum Üben».
- Mehr Bestätigung (Wunsch Lehrperson): wechselndes Lob (`PRAISE`), bei 5/10/15 richtig in Folge «🔥 N richtig hintereinander», gemeistertes Wort: Stern fliegt zum Zähler oben, «⭐ Meine Sammlung» (zugeklappt, gemeisterte Wörter als Karten, heute neue mit gelbem Rand, antippen = anhören). Etappe nennt die heute neu gemeisterten Wörter. «Diese Woche geübt» Mo–So mit ✓ (`days`, nur auf diesem Gerät, keine Serie, die auf 0 fällt).
- Gespeichert unter `ow2u2_lernpfad` (Teil, Stufe pro Wort, Wiederholungen `rev`, aktive Wörter, beste Test-Medaille, Test-Antworten). Der Stand gilt nur auf dem Gerät und im Browser, wo geübt wurde. «Nochmals üben» beim Lernpfad fragt vorher nach.
- **Reiter:** «🔤 Wörter» und «🧩 Grammatik» (`switchTab`, gemerkt in `STATE.tab`).
- **Grammatik-Pfad** (present continuous für Abmachungen, CB 2–3, LC L2.1): 4 Stufen mit eigenen Sätzen (`G_ITEMS`, nichts aus dem Lehrmittel): 1 am / is / are auswählen (10), 2 Verb + ing auswählen (10), 3 Satz bauen durch Antippen der Bausteine (7, Zeitangabe darf vorne oder hinten stehen), 4 «am / is / are + Verb-ing» schreiben (8, «'m / 's / 're» gilt auch). Pro Stufe ein Beispiel (`example`), das in keiner Aufgabe vorkommt; auch Kopfkarte, Theorie und Platzhalter nutzen nur Verben, die in keiner Aufgabe vorkommen (read, fly, ride, leave). Sätze bewusst anders als die Coursebook-Übungen CB 2–3. Satz bauen: Bausteine klein (ausser I und Namen), Gross-Anfang und «.»/«?» setzt die Seite; «Weiss ich nicht» vorhanden. Schreiben: Subjekt davor und Satzzeichen erlaubt («I'm meeting.»), ohne Apostroph («m meeting») falsch. Kopf zeigt ⭐ Wörter oder 🧩 Grammatik je nach Reiter; «Diese Woche geübt» in beiden Reitern. Hilfe: erstes Wort. Falsche Sätze kommen nach 2 anderen wieder. Stufe fertig = alle Sätze einmal richtig. Danach Wiederholung nach 1 und 3 Tagen (4 Sätze schreiben). Etappen, Lob und Übungstage wie im Lernpfad. Gespeichert in `STATE.gram`.

## RZG-Hub: Besonderheiten
- Grundlagen: Dossier «Dynamik der Erde» mit Lösungen der Lehrperson und Blatt «Lernziele Dynamik der Erde Teil 2» (Ich-kann-Checkliste, LZ1 bis LZ5) mit Musterlösungen, die sich aufs Dossier stützen.
- Die Seite deckt nur Teil 2 ab: Vulkan-Entstehung, Schild-/Schichtvulkan, Ausbruch, Erdbeben, Richterskala, Energie rechnen (×10 Ausschlag / ×32 Energie), Tsunamis. Teil 1 (Aufbau der Erde, Plattentektonik) war schon Test 1, nicht einbauen.
- Lernziel-Nummern auf der Seite wie auf dem Blatt (LZ1 bis LZ5). Jeder Punkt der Checkliste muss geübt werden.
- «Inaktive Vulkane» (Aufgabe 6) ist ein Zusatz aus dem Dossier. Steht nicht auf dem Lernziel-Blatt und kommt im Test nicht vor. Darum `extra: true`: wird geübt und geprüft, zählt aber nicht in der Test-Simulation (73 P., bestanden ab 44).
- Die Schüler füllen das Lernziel-Blatt auf Papier aus. Das Lernportal dient danach zum nochmaligen Üben für den Test. Reiter «Lernziel-Blatt» (`BLATT`): alle Ich-kann-Punkte mit Textfeld, Musterlösung zum Aufklappen und Häkchen «Das kann ich». Zählt nicht zu `TASKS`.
- Hilfe-Treppe im Reiter «Lernziel-Blatt» (`HELP`): 1 Tipp mit Wortkasten → 2 Satzanfänge einfügen → 3 Antwort prüfen (sucht Schlüsselwörter, Satzanfänge zählen nicht) → 4 Musterlösung, dazu Knopf «Theorie». Wunsch der Lehrperson: viel Hilfe, bevor die Lösung kommt. Bei neuen offenen Aufgaben (auch auf anderen Seiten) diese Hilfe-Stufen einbauen.
- Aufgaben sind Daten in `DEFS` (Blocktypen gaps, rows, mc, checks, dnd, num). `TASKS` wird daraus berechnet.

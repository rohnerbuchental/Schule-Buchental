---
name: aufgaben-ersteller
description: Erstellt eine neue Lernseite (oder neue Aufgaben auf einer bestehenden Seite) nach dem Muster des Lernportals und fügt die Kachel in index.html ein. Nutzen, wenn die Lehrperson ein neues Thema, Lehrmittel oder Kapitel wünscht.
tools: Read, Grep, Glob, Bash, Edit, Write
---

Du erstellst Lernseiten für Sek-Schülerinnen und -Schüler der Schule Buchental. Halte dich streng an `CLAUDE.md`.

## Vor dem Start
- Lies `CLAUDE.md`.
- Nimm `RZG Vulkane Erdbeben Tsunamis.html` als Vorlage. Sie ist datengesteuert: Aufgaben stehen als Daten in `DEFS` (Blocktypen gaps, rows, mc, checks, dnd, num mit `head`, `tip`), `TASKS` wird daraus berechnet, Mischen über `shuffleTask`, Hilfe-Treppe über `BLATT`/`HELP`. Lies nur die nötigen Abschnitte mit `grep -n` und `sed -n`.
- Fehlen Angaben (Fach, Lehrmittel, Kapitel, Niveau, Punktzahl der Test-Simulation), frag kurz nach, statt zu raten.

## Regeln für die neue Seite
- Eine einzige HTML-Datei. Tailwind über `cdn.tailwindcss.com`, Schrift Inter. Keine weiteren Abhängigkeiten.
- Deutsch (Schweiz), immer «ss». Kurze, einfache Sätze. Bei Fremdsprachen: Aufgabentext auf Deutsch, Inhalt in der Fremdsprache.
- Alle Antwortmöglichkeiten werden bei jedem Laden gemischt. `data-noshuffle` nur bei reinen Platznummern.
- Wo es Sinn macht, auch die Reihenfolge der Teilfragen und der Lückentext-Abschnitte mischen. Buchstaben a), b), c) nicht in den Fragetext schreiben, die Seite setzt sie.
- Jede Aufgabe bekommt einen `tip` (Hinweis, verrät die Lösung nicht; einfache Sprache, gern ein Vergleich aus dem Alltag), den Knopf «📖 Theorie» und «🔀 Nochmals üben».
- Offene Textfragen: Textfeld + Hilfe-Treppe (Tipp mit Wortkasten, Satzanfänge, Antwort prüfen mit Schlüsselwörtern, Musterlösung). Zählen nicht zu `TASKS`.
- Drag & Drop immer auch mit Antippen + Ziel antippen. Nichts läuft auf 390 px seitlich über (lange Wörter umbrechen, Tabellen in `overflow-x-auto`).
- Antworten im `localStorage` speichern, jeder Zugriff in `try/catch`. Eigener Schlüssel-Präfix pro Seite.
- Start mit `DOMContentLoaded`, nie `window.onload`.
- Bewertung nur an einer Stelle: `TASKS` mit `max` und `score()`. Prüfen-Knöpfe und Test-Simulation nutzen beide `TASKS`. Total immer aus `TASKS` berechnen.
- Note = Punkte ÷ Total × 5 + 1, gerundet auf 0.1. Bestanden ab 60 % (Note 4.0).
- Jede Aufgabe mit Kommentar `<!-- Aufgabe N: Titel | Code -->` markieren, z.B. `<!-- Aufgabe 3: Schleifen | MI.2.2.h -->`. Den Code mit `grep` in `lehrplan/` suchen (nie ganze Dateien lesen) und nur Codes verwenden, die dort stehen. Bevorzugt Punkte mit **GA** (Grundanspruch).

## Startseite
- Neue Kachel in `index.html` im gleichen Stil wie die bestehenden `<a … class="group bg-white rounded-2xl …">`. Leerzeichen im Dateinamen als `%20` im Link.
- Neue Seite in der Tabelle «Seiten» in `CLAUDE.md` eintragen.

## Abschluss
1. `node tools/check.js` ausführen, bis alles ✅ ist.
2. `grep -n "ß"` auf der neuen Seite muss leer sein.
3. Kurz melden: Dateiname, Anzahl Aufgaben, Punktetotal, was die Lehrperson noch prüfen soll.

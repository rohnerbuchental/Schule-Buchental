# AGENTS.md

Startdatei für jeden Chat in diesem Repo.

## 0. Zuerst (Pflicht, vor der ersten Sachantwort)

1. Dieses Repo ist öffentlich. Hier steht nichts Persönliches und keine kontoweite Regel.
2. Chat im Konto von Jonas: zusätzlich mercilessmarshmallow/Zentral mit add_repo anhängen, flach klonen und **KONTO.md** darin lesen und befolgen. In der ersten Antwort nennen: «KONTO.md, Stand JJJJ-MM-TT, gelesen». Klappt das nicht: nur lesen, nichts ändern, Jonas melden.
3. Alle anderen: Es gilt nur diese Datei. Das zentrale Repo ist privat und wird nicht gesucht.
4. Nie in dieses Repo: Personendaten, Mailadressen, Pfade auf Geräten, Inhalt aus Zentral.

## 1. Das Projekt

Lernportal Schule Buchental: statische Lernseiten (eine HTML-Datei pro Thema) für Sek-Schülerinnen und -Schüler, veröffentlicht mit GitHub Pages. Die Schüler bekommen nur die Startseite https://rohnerbuchental.github.io/Schule-Buchental/ (`index.html`), die jede Lernseite als Kachel verlinkt. Neue Seiten darum immer als Kachel in `index.html` eintragen.

Tests, Lösungen, Arbeitsblätter, Planungen und das Niveau der Klasse liegen in der privaten Ablage der Lehrperson (privates Repo, im Konto von Jonas über das Verzeichnis in Zentral erreichbar). Für alles ausser dem Lernportal gelten deren Regeln.

Seiten:

| Datei | Thema |
|---|---|
| `connected_3_scratch_trainingshub.html` | Informatik, Connected 3 «Abheben mit Algorithmen» (Scratch), Lernpfad in 4 Teilen |
| `Deutsch Novemberschnee.html` | Deutsch, Lektüre «Novemberschnee» (abgeschlossen, Kachel entfernt 12.11.2026, Datei bleibt) |
| `Englisch open_world_2_unit_1.html` | Englisch, Open World 2 Unit 1 (abgeschlossen, Kachel entfernt 11.11.2026, Datei bleibt) |
| `Englisch open_world_2_unit_2.html` | Englisch, Open World 2 Unit 2 (Wörter-Lernpfad, 3 Grammatik-Lernpfade) |
| `Informatik Computer-Grundlagen.html` | Informatik, Exkurs Computer-Grundlagen, 2 Lektionen, Missionen M1–M7. Kachel seit 24.11.2026 |
| `Informatik Word-Fuehrerschein.html` | Informatik, Word-Führerschein. Vorschau seit 18.11.2026, Kachel erst nach Freigabe |
| `RZG Vulkane Erdbeben Tsunamis.html` | RZG, Dynamik der Erde, Lernpfad in 4 Teilen |

## 2. Wo was liegt (nur bei Bedarf lesen)

| Aufgabe | Datei |
|---|---|
| Regeln für alle Seiten, Lehrplan-Codes, Agenten, Arbeitsablauf: vor jeder Arbeit an einer Seite ganz lesen | docs/regeln.md |
| Besonderheiten jeder Seite und Stand Spanisch (nur den Abschnitt der Seite lesen) | docs/seiten.md |
| Didaktische Grundsätze mit Quellen | docs/didaktik.md |
| Lehrplan Zyklus 3 (nur mit `grep`) | lehrplan/ |
| Prüf- und Erstell-Agenten | .claude/agents/ |
| Prüfskripte (`check.js` nach jeder Änderung) | tools/ |
| Übungsdateien für die Seiten | dateien/ |
| Entscheide | docs/entscheide/LIESMICH.md |


## 3. Projektregeln

- **Nur ändern, was die Lehrperson ausdrücklich sagt** (gilt für alles: Lernseiten, jede Aufgabe). Bestehende Aufgaben nie von sich aus ändern, auch nicht wegen Funden eines Prüf-Agenten oder eigener Ideen: nur als nummerierte Vorschläge melden und auf «ja» warten. Eine Frage der Lehrperson ist kein Auftrag: zuerst antworten.
- **Öffentlich:** GitHub Pages veröffentlicht jede Datei. Nie Tests, Lösungen, Einschätzungen zur Klasse oder Namen in dieses Repo.
- **Arbeit über Pull Requests:** eigener Branch, Pull Request auf `main`, mit Vorschau als Artifact-Link. Zusammenführen nur Jonas.
- Alle Regeln für die Seiten (Zufall, Hilfe, angstfrei, Lernpfad, Belohnung, Spanisch, Technik) stehen in `docs/regeln.md`. Neue Wünsche zum Lernportal dort oder in `docs/seiten.md` festhalten.
- **Schul-Cockpit** (https://claude.ai/artifact/Nj9SU88azU74reChteRpQQ): am Ende jeder Arbeit die eigene Fach-Zeile mit `ArtifactData` nachführen: Sammlung `faecher`, Dokument `deutsch` | `englisch` | `informatik` | `rzg` | `bg` | `bo` | `allgemein`; zuerst `get`, dann `update` mit `if_version`. Felder: `stand` (1 Satz), `deinTeil` (Liste), `naechstes` (1 Satz), `aktualisiert` (JJJJ-MM-TT). Nie Schülernamen.
- Chattitel-Emoji: 📖 Deutsch, 🇬🇧 Englisch, 💻 Informatik, 🌋 RZG, 🎨 BG, 🧭 Berufliche Orientierung, 🗂️ Allgemein, 🏫 Lernportal (fächerübergreifend).

## 4. Gelernte Fehler

- noch keine

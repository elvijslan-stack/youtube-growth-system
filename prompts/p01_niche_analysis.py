PROMPT_ID = "01_niche_analysis"
FOLDER = "01_niche_analysis"
FILENAME = "niche_analysis"

PROMPT = """
EQF
[EQF v2.0 — EXECUTION QUALITY FRAMEWORK]

ROLLE:
Du bist ein YouTube-Nischen-Analyst mit Zugriff auf aktuelle CPM-Benchmarks
(2025–2026). Du lieferst ausschließlich verifizierbare, datenbasierte
Einschätzungen — keine generischen Ratschläge.

KONTEXT:
Ich baue ein faceless YouTube-Growth-System. Ziel sind Nischen mit
(a) hohem CPM, (b) niedriger bis mittlerer Wettbewerbsdichte,
(c) Evergreen-Nachfrage (Content bleibt 12+ Monate suchbar).
AdSense ist NICHT der Hauptumsatz — es ist die Baseline. Der eigentliche
Hebel liegt in Affiliate, Sponsorships und digitalen Produkten.

AUFGABE:
Analysiere die Top-10-YouTube-Nischen, die alle drei Kriterien gleichzeitig
erfüllen. Für jede Nische liefere exakt:

1. Nischenname
2. Durchschnittlicher CPM (USD, Spanne, US-Audience-Basis)
3. Content-Schwierigkeit (Skala 1–5, mit Begründung: Rechercheaufwand,
   Produktionskomplexität, Faktenrisiko)
4. Monetarisierungspfade jenseits von AdSense (mind. 3 konkrete Wege pro
   Nische, mit Beispielprodukten/-anbietern)
5. 3-Wort-Kanal-Konzept (prägnant, wiedererkennbar, sofort verständlich)

AUSGABEFORMAT:
Markdown-Tabelle + darunter je Nische ein 3-Zeilen-Block mit den Details.
Keine Einleitung, keine Zusammenfassung am Ende. Nur die Analyse.

EINSCHRÄNKUNGEN:
- CPM-Zahlen müssen aus öffentlich zugänglichen Creator-Benchmarks
  2025/2026 stammen. Wenn eine Zahl umstritten ist, nenne die Spanne und
  markiere die Unsicherheit.
- „Niedrige Konkurrenz" bedeutet: nicht die ersten 20 generischen
  „Personal Finance"-Kanäle, sondern spezifische Unter-Nischen mit
  unterversorgter Suche.
- Evergreen = das Thema verliert nicht in 6–12 Monaten seine Suchnachfrage
  (keine Trend-Hypes wie „GPT-5 Launch").
- 3-Wort-Konzepte müssen als Kanalname funktionieren
  (z. B. „Legal Explained Simply" → 3 Wörter).

START.
EQF
"""

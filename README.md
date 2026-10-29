# 🚀 YouTube Growth System

Ein lokales, datengetriebenes Pipeline-System zur automatisierten Erstellung von YouTube-Wachstums-Assets. 
Es generiert fertige Markdown-Dateien für Nischen-Analyse, Kanal-Identität, Content-Roadmaps, Video-Scripts, SEO, Monetarisierung und Cross-Platform-Repurposing — **ohne API-Kosten, ohne Prompts, rein lokal.**

---

## 📦 Features (Die 7 Steps)

Das System ist in 7 aufeinander aufbauende Module unterteilt:

| Step | Modul | Output (Markdown) | Beschreibung |
|------|-------|-------------------|--------------|
| **01** | Nischen-Analyse | `niche_analysis.md` | Top-10 Nischen (High CPM, Low Comp, Evergreen) inkl. Monetarisierung. |
| **02** | Kanal-Identität | `channel_identities.md` | 5 Kanalnamen, Tagline, Zielgruppen-Persona, Content-Pillars, Unique Mechanism. |
| **03** | 90-Tage-Roadmap | `content_roadmap.md` | 12 Video-Titel pro Nische, Upload-Schedule, SEO/Viral-Phasen. |
| **04** | Video-Scripts | `video_script_*.md` | Volle 7-Min-Scripts (Hook → Agitation → Solution → 3 Insights → CTA → Tease). |
| **05** | SEO & Thumbnails | `seo_thumbnail_*.md` | SEO-Titel (<60 Zeichen), 3 Thumbnail-Konzepte, Timestamps, 10 Tags. |
| **06** | Monetarisierung | `monetization_*.md` | Affiliate-Programme, Digital Products, Sponsorship-Pitch, Lead-Magnets. |
| **07** | Repurposing | `repurpose_pack_*.md` | Twitter-Thread, LinkedIn-Post, 3 Shorts-Hooks, Newsletter, Pinterest. |

---

## 📂 Ordnerstruktur

```text
youtube-growth-system/
├── data/                    # Reine Daten (Dicts & Listen)
│   ├── niches.py            # Step 01
│   ├── identities.py        # Step 02
│   ├── roadmap.py           # Step 03
│   ├── scripts.py           # Step 04
│   ├── seo.py               # Step 05
│   ├── monetization.py      # Step 06
│   └── repurpose.py         # Step 07
├── core/                    # Renderer (Daten → Markdown)
│   ├── render.py
│   ├── render_identity.py
│   ├── render_roadmap.py
│   ├── render_script.py
│   ├── render_seo.py
│   ├── render_monetization.py
│   └── render_repurpose.py
├── output/                  # Generierte Markdown-Dateien
├── main.py                  # CLI-Einstiegspunkt
└── README.md
```
## ⚙️ Setup & Ausführung

**Voraussetzungen:** Python 3.9+ (keine externen Packages nötig, nutzt nur die Python-Standardbibliothek).

> **Hinweis für macOS-Nutzer:** Falls `python3` bei dir nicht funktioniert, nutze `/usr/bin/python3` oder lege dir einen Alias an:  
> `alias py3='/usr/bin/python3'`

### Einzelne Steps ausführen

```bash
# Step 01-03 (Nischen, Identität, Roadmap für alle 10 Nischen auf einmal)
python3 main.py 01
python3 main.py 02
python3 main.py 03

# Step 04-07 (Scripts, SEO, Monetization, Repurposing — pro Nische & Video)
python3 main.py 04 --niche 1 --video 1
python3 main.py 05 --niche 1 --video 1
python3 main.py 06 --niche 1 --subs 2500
python3 main.py 07 --niche 1 --video 1
```
### CLI-Parameter

* `--niche (1–10)`: Wählt die Nische aus (Standard: alle).
* `--video (1–12)`: Wählt das Video aus der Roadmap (Standard: 1).
* `--subs (Zahl)`: Für Step 06 — setzt den aktuellen Subscriber-Stand, um das richtige Monetarisierungs-Tier (T0–T3) zu triggern (Standard: 1000).

---

## 🛠️ Anpassung (Customization)

Das System ist so gebaut, dass du keinen Code ändern musst, um neue Inhalte hinzuzufügen:

* **Neue Nische hinzufügen:** Füge einen neuen Eintrag in `data/niches.py` (und den entsprechenden Folge-Dateien) mit dem nächsten `rank` (z.B. 11) hinzu.
* **Titel ändern:** Öffne `data/roadmap.py` und passe die Strings in den Tupeln an.
* **Eigene Scripts schreiben:** In `data/scripts.py` unter `FLAGSHIP_SCRIPTS` kannst du handgeschriebene Gold-Standard-Scripts hinterlegen.

---

## 🚀 Workflow-Tipp

1. Führe Step 01 und 02 aus, um deine Nische zu validieren.
2. Führe Step 03 aus, um alle 12 Video-Titel zu generieren.
3. Gehe die Liste durch und wähle dein Flagship-Video (Video 1).
4. Führe Step 04–07 für genau dieses Video aus, um alle Assets (Skript, SEO, Pitch, Social Posts) für den Launch in der Hand zu haben.

---

## 👤 Author & License

Entwickelt von **Elvijs Landmans** ([@elvijslan-stack](https://github.com/elvijslan-stack)).

Dieses Projekt ist unter der **MIT-Lizenz** lizenziert — frei nutzbar, anpassbar und weiterverwendbar. Siehe die [`LICENSE`](./LICENSE)-Datei für Details.

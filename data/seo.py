"""SEO & Thumbnail Strategy — Nischen-Profile + Overrides."""

NICHE_SEO = {
    1: {
        "palette": "Dunkelblau (#0F172A) + Neon-Grün (#22C55E) Akzent",
        "face_rule": "Screencast-Screenshot + Sprecher-PIP unten links",
        "text_style": "fett, sans-serif, alles-caps, max. 4 Wörter",
        "thumb_concepts": [
            {
                "visual": "Split-Screen: links Notion-Board mit 10 Einträgen (rot umrandet), rechts Airtable mit 1 Eintrag (grün). Pfeil dazwischen.",
                "overlay": "10 TOOLS → 1",
                "ab": "A/B: Pfeil-Farbe (grün vs rot) und Overlay-Position (mitte vs unten-links)",
            },
            {
                "visual": "Zapier-Dashboard mit grünem 'Success'-Badge, daneben ein rotes 'Error'-Badge. Freisteller-Zeigefinger zeigt drauf.",
                "overlay": "0 MANUELLE TASKS",
                "ab": "A/B: Badge-Reihenfolge (Success links vs Error links) und Overlay-Größe (70% vs 50% Breite)",
            },
            {
                "visual": "Drei App-Icons (Notion, Zapier, Metabase) in einer Reihe, mit ↓ '3-LAYER'-Label darüber. Dunkler Gradient-Hintergrund.",
                "overlay": "3-LAYER STACK",
                "ab": "A/B: Icons einzeln vs als Gruppe, Label oben vs unten",
            },
        ],
        "ab_matrix": [
            "Text-Overlay: alles-caps vs sentence-case",
            "Farb-Akzent: neon-grün vs neon-orange",
            "Sprecher-PIP: sichtbar vs nur Screencast",
        ],
        "tags_pool": [
            "saas automation", "notion automation", "zapier tutorial",
            "airtable tips", "b2b saas ops", "small saas founder",
            "make.com tutorial", "workflow automation", "n8n tutorial",
            "saas operations", "startup ops", "founder automation",
            "notion template", "airtable vs notion", "zapier vs make",
            "saas tutorial 2026", "automate saas", "ops stack",
        ],
        "section_labels": {
            "hook": "Hook — der Stack in 60 Sekunden",
            "agitation": "Warum deine Ops dich auffressen",
            "solution": "Die 3-Layer-Walkthrough",
            "insights": "3 Regeln, die alles ändern",
            "cta": "Template laden (kostenlos)",
            "tease": "Nächstes Video",
        },
        "description_intro": (
            "In diesem Video zeige ich dir das komplette Ops-System, das ich in "
            "meiner eigenen SaaS fahre — 4 Tools, 1 Regel, 0 manuelle Tasks. "
            "Du kannst es morgen nachbauen, ohne eine Zeile Code zu schreiben."
        ),
        "hashtags": ["#saas", "#automation", "#notion", "#zapier", "#startup"],
    },
    2: {
        "palette": "Cremeweiß (#F5F1E8) + dunkles Marineblau (#0B2545) Akzent",
        "face_rule": "Dokument-Freisteller + Hände beim Ausfüllen, kein Gesicht",
        "text_style": "serif bold, sentence-case, max. 4 Wörter",
        "thumb_concepts": [
            {
                "visual": "Freisteller einer Klageschrift mit rotem 'FILED'-Stempel. Ein Stift daneben.",
                "overlay": "NO LAWYER NEEDED",
                "ab": "A/B: Stempel rot vs grün, Hintergrund creme vs hellgrau",
            },
            {
                "visual": "Split-Screen: links Anwaltsrechnung $4.200 (rot), rechts Filing-Gebühr $75 (grün).",
                "overlay": "$4,200 vs $75",
                "ab": "A/B: Zahlen-Reihenfolge (Anwalt links vs rechts), Overlay als Kreis vs Rechteck",
            },
            {
                "visual": "Gerichtsgebäude-Silhouette im Hintergrund, davor ein 5-teiliger Aktenordner mit Häkchen.",
                "overlay": "5-PIECE CASE FILE",
                "ab": "A/B: Silhouette sichtbar vs weg, Ordner groß vs klein",
            },
        ],
        "ab_matrix": [
            "Gesicht: Hände sichtbar vs nur Dokumente",
            "Text-Farbe: Marineblau vs schwarz",
            "Stempel-Effekt: rotiert vs gerade",
        ],
        "tags_pool": [
            "small claims court", "pro se legal", "file small claims",
            "small claims lawsuit", "legal self defense", "diy legal",
            "consumer rights", "tenant rights", "court without lawyer",
            "small claims process", "small claims forms", "small claims evidence",
            "small claims filing", "sue landlord", "sue contractor",
            "small claims california", "small claims texas", "small claims 2026",
        ],
        "section_labels": {
            "hook": "Hook — was dich der Anwalt kostet",
            "agitation": "Warum die meisten hier aufgeben",
            "solution": "Filing-Walkthrough Schritt für Schritt",
            "insights": "3 Dinge, die Richter wirklich lesen",
            "cta": "Vorlagen laden",
            "tease": "Nächstes Video",
        },
        "description_intro": (
            "Ich habe 3 Verfahren allein durchgezogen — ohne Anwalt. In diesem "
            "Video zeige ich dir den kompletten Filing-Prozess für Small Claims, "
            "inklusive der 5 Aktenstücke, die den Unterschied machen."
        ),
        "hashtags": ["#smallclaims", "#prose", "#legal", "#court", "#diy"],
    },
    3: {
        "palette": "Weiß (#FFFFFF) + Teal (#0E7490) + Coral (#F97316) Akzent",
        "face_rule": "Notizbuch-Freisteller + bunte Marker, kein Gesicht",
        "text_style": "sans-serif bold, sentence-case, max. 4 Wörter",
        "thumb_concepts": [
            {
                "visual": "Kalender mit '90-TAGE'-Weg, jede Woche ein grüner Haken, Endpunkt: 'CPC ✅'",
                "overlay": "90 DAYS → CPC",
                "ab": "A/B: Kalender-Motiv vs Notizbuch, Haken grün vs blau",
            },
            {
                "visual": "Freisteller-Zeugnis 'CPC — PASSED' mit Konfetti, im Hintergrund Bücher-Stapel.",
                "overlay": "PASSED FIRST TRY",
                "ab": "A/B: Zeugnis groß vs klein, Konfetti ja vs nein",
            },
            {
                "visual": "Split: links Gehalt $32K (grau), rechts $58K (teal, bold). Pfeil aufwärts.",
                "overlay": "$32K → $58K",
                "ab": "A/B: Zahl links/rechts getauscht, Pfeil-Form (Linie vs Block)",
            },
        ],
        "ab_matrix": [
            "Hintergrund: weiß vs pastell-teal",
            "Zahlen-Stil: Handschrift vs bold sans-serif",
            "Emotion: erleichtert vs fokussiert (Icon statt Gesicht)",
        ],
        "tags_pool": [
            "medical coding", "cpc certification", "medical coder",
            "icd-10 coding", "medical billing", "aapc exam",
            "medical coding salary", "coding career", "medical coding 2026",
            "cpc exam prep", "medical coding course", "ccs certification",
            "remote medical coder", "medical coding roadmap", "medical coding tips",
            "certification prep", "exam pass tips", "career changer",
        ],
        "section_labels": {
            "hook": "Hook — 90-Tage-Roadmap",
            "agitation": "Warum 9 Monate Standard sind",
            "solution": "12-Wochen-Sprint im Detail",
            "insights": "3 Regeln für den ersten Versuch",
            "cta": "Notion-Roadmap laden",
            "tease": "Nächstes Video",
        },
        "description_intro": (
            "Ich habe CPC in 42 Tagen bestanden — mit Vollzeitjob. In diesem "
            "Video ist die komplette 90-Tage-Roadmap, Tag für Tag, plus die "
            "3 Regeln, die über Bestehen oder Durchfallen entscheiden."
        ),
        "hashtags": ["#medicalcoding", "#cpc", "#certification", "#career", "#icd10"],
    },
    4: {
        "palette": "Grau (#374151) + Signalrot (#DC2626) + Warmgelb (#FBBF24)",
        "face_rule": "Walkthrough-Foto + roter Kreis um das Problem, kein Gesicht",
        "text_style": "bold sans-serif, caps, max. 3 Wörter",
        "thumb_concepts": [
            {
                "visual": "Fundament-Riss mit rotem Kreis und Pfeil. Vergrößerungsglas-Effekt.",
                "overlay": "$40K PROBLEM",
                "ab": "A/B: Kreis rot vs gelb, Vergrößerung ja vs nein",
            },
            {
                "visual": "Dach-Schaden mit rotem Pfeil von oben. Nachbarhaus daneben sauber.",
                "overlay": "DEAL BREAKER",
                "ab": "A/B: Dach sichtbar vs Nahaufnahme, Pfeil schmal vs dick",
            },
            {
                "visual": "Split: links Moisture-Meter mit 22% (rot), rechts 8% (grün). Hand hält das Gerät.",
                "overlay": "22% vs 8%",
                "ab": "A/B: Hand sichtbar vs nur Gerät, Zahlen groß vs klein",
            },
        ],
        "ab_matrix": [
            "Roter Kreis: dünn vs dick",
            "Overlay-Position: oben vs mitte",
            "Foto-Filter: klar vs kontrastreich",
        ],
        "tags_pool": [
            "home inspection", "house inspection", "home inspector",
            "first time home buyer", "real estate due diligence", "foundation cracks",
            "roof inspection", "moisture meter", "thermal camera home",
            "home buyer tips", "property inspection", "deal breaker",
            "home inspection 2026", "home buyer mistakes", "inspection checklist",
            "pre purchase inspection", "home inspection tools", "home inspection walkthrough",
        ],
        "section_labels": {
            "hook": "Hook — 10 Flaggen, 80% der Kosten",
            "agitation": "Warum Erstkäufer das übersehen",
            "solution": "Die 200-Punkte-Walkthrough",
            "insights": "3 Dinge, die Realtors nie sagen",
            "cta": "Checkliste laden",
            "tease": "Nächstes Video",
        },
        "description_intro": (
            "Von 10 Häusern, die ich inspiziere, haben 9 mindestens eine rote "
            "Flagge, die der Käufer übersehen hätte. In diesem Video zeige ich "
            "die 10 wichtigsten und wie du sie in 10 Minuten selbst findest."
        ),
        "hashtags": ["#homeinspection", "#realestate", "#firsttimebuyer", "#property", "#diy"],
    },
    5: {
        "palette": "Industrie-Silber (#9CA3AF) + Maschinen-Orange (#EA580C) Akzent",
        "face_rule": "Maschinen-Nahaufnahme + Orange-Pfeil auf den Prozess-Schritt",
        "text_style": "bold condensed sans, caps, max. 4 Wörter",
        "thumb_concepts": [
            {
                "visual": "Spritzguss-Maschine mit aufgeschäumtem Kunststoff-Teil, Freisteller, Pfeil zeigt auf Form.",
                "overlay": "HOW IT'S MADE",
                "ab": "A/B: Maschine komplett vs nur Form, Pfeil orange vs weiß",
            },
            {
                "visual": "5-Stufen-Diagramm als Querstreifen mit Icons: Input → Form → Join → Finish → QC.",
                "overlay": "5 STAGES",
                "ab": "A/B: Diagramm horizontal vs vertikal, Icons farbig vs monochrom",
            },
            {
                "visual": "CNC-Fräser mit Funken, Freisteller, Toleranz-Wert '0.001mm' eingeblendet.",
                "overlay": "0.001mm",
                "ab": "A/B: Funken ja vs nein, Zahl groß vs klein",
            },
        ],
        "ab_matrix": [
            "Hintergrund: Werkstatt-Foto vs Studio-Gradient",
            "Pfeil-Stil: dick vs dünn",
            "Farbe: Orange vs Gelb",
        ],
        "tags_pool": [
            "injection molding", "cnc machining", "how it's made", "factory tour",
            "manufacturing process", "industrial engineering", "machining explained",
            "metal casting", "pcb manufacturing", "aluminum can production",
            "factory explained", "engineering explained", "manufacturing 2026",
            "industrial process", "production line", "how things are made",
            "spritzguss", "cnc basics",
        ],
        "section_labels": {
            "hook": "Hook — die 6-Wochen-Kette",
            "agitation": "Warum keiner den Prozess zeigt",
            "solution": "5-Stage-Walkthrough",
            "insights": "3 Dinge, die nur Fabrik-Chefs wissen",
            "cta": "PDF-Poster laden",
            "tease": "Nächstes Video",
        },
        "description_intro": (
            "Jedes Alu-Dose, jedes Auto-Teil, jeder Chip — alles folgt dem "
            "gleichen 5-Stage-Modell. In diesem Video zerlege ich den Prozess "
            "einer echten Fabrik in 8 Minuten, ohne Fachchinesisch."
        ),
        "hashtags": ["#manufacturing", "#engineering", "#howitsmade", "#factory", "#industrial"],
    },
    6: {
        "palette": "Weiß (#FFFFFF) + Navy (#1E3A8A) + Grün (#16A34A) Akzent",
        "face_rule": "QuickBooks-Screenshot + Sprecher-PIP oben rechts",
        "text_style": "sans-serif bold, sentence-case, max. 4 Wörter",
        "thumb_concepts": [
            {
                "visual": "QuickBooks-Dashboard mit grünem 'Reconciled'-Haken, daneben Excel mit roten Fehlern.",
                "overlay": "CLOSE IN 15 MIN",
                "ab": "A/B: Dashboard links vs rechts, Haken groß vs klein",
            },
            {
                "visual": "Split-Screen: links Chaos-Belege-Stapel, rechts aufgeräumtes Chart of Accounts.",
                "overlay": "CHAOS → CLEAN",
                "ab": "A/B: Pfeil sichtbar vs nur Split, Stapel groß vs klein",
            },
            {
                "visual": "Kosten-Vergleich: Steuerberater $1.800 (rot) vs DIY $0 (grün), mit Häkchen.",
                "overlay": "$1,800 vs $0",
                "ab": "A/B: Zahlen-Stil (bold vs handschrift), Hintergrund weiß vs hellblau",
            },
        ],
        "ab_matrix": [
            "Screenshot: QBO vs Xero",
            "Overlay: Sentence-case vs UPPER",
            "PIP: mit Gesicht vs ohne",
        ],
        "tags_pool": [
            "quickbooks online", "xero accounting", "bookkeeping", "small business accounting",
            "chart of accounts", "month end close", "bookkeeping basics",
            "quickbooks vs xero", "small business bookkeeping", "accounting for beginners",
            "bookkeeping 2026", "diy bookkeeping", "quickbooks tutorial",
            "xero tutorial", "bookkeeper vs diy", "bookkeeping template",
            "tax ready books", "small business finance",
        ],
        "section_labels": {
            "hook": "Hook — QBO vs Xero Test",
            "agitation": "Warum Bücher 3 Monate hinterher sind",
            "solution": "15-Minuten-Close-Routine",
            "insights": "3 Dinge, die Steuerberater nicht sagen",
            "cta": "Template laden",
            "tease": "Nächstes Video",
        },
        "description_intro": (
            "Ich habe 40 Firmen-Bücher aufgeräumt — die häufigsten 3 Fehler sind "
            "in 90% von ihnen. In diesem Video zeige ich das 15-Minuten-Close-System, "
            "mit dem dein Monatsabschluss nie wieder zum Projekt wird."
        ),
        "hashtags": ["#bookkeeping", "#quickbooks", "#xero", "#smallbusiness", "#accounting"],
    },
    7: {
        "palette": "Cremeweiß (#FEF3C7) + Anthrazit (#1F2937) + Rot (#DC2626) Akzent",
        "face_rule": "Policy-Dokument mit rotem Kreis um den entscheidenden Satz",
        "text_style": "serif bold, sentence-case, max. 4 Wörter",
        "thumb_concepts": [
            {
                "visual": "Policy-Dokument mit rotem Kreis um eine fett markierte Exclusion-Klausel.",
                "overlay": "THE FINE PRINT",
                "ab": "A/B: Kreis rot vs gelb, Dokument sichtbar vs Text-Only",
            },
            {
                "visual": "Split: 'Term Life' mit $30/mo grün, 'Whole Life' mit $340/mo rot.",
                "overlay": "$30 vs $340",
                "ab": "A/B: Zahlen getauscht, Farbe grün/rot vs blau/orange",
            },
            {
                "visual": "Familien-Silhouette (anonym), daneben Police-Umschlag mit 'DENIED'-Stempel.",
                "overlay": "CLAIM DENIED",
                "ab": "A/B: Silhouette ja vs nein, Stempel groß vs klein",
            },
        ],
        "ab_matrix": [
            "Dokument: Seitenverhältnis quadratisch vs A4",
            "Overlay-Farbe: Anthrazit vs Rot",
            "Stempel-Rotation: -5° vs 0°",
        ],
        "tags_pool": [
            "life insurance", "term life insurance", "whole life insurance",
            "disability insurance", "insurance comparison", "policy audit",
            "insurance explained", "life insurance 2026", "term vs whole",
            "insurance fine print", "claim denied", "umbrella insurance",
            "insurance tips", "buy life insurance", "insurance basics",
            "insurance mistakes", "insurance agent truth", "insurance shopping",
        ],
        "section_labels": {
            "hook": "Hook — 340$ zu viel pro Monat",
            "agitation": "Warum Agenten das Falsche verkaufen",
            "solution": "Die 3-Quote-Regel",
            "insights": "3 Sätze, die Claims entscheiden",
            "cta": "Checkliste laden",
            "tease": "Nächstes Video",
        },
        "description_intro": (
            "Der durchschnittliche Familienvater zahlt 340$ zu viel pro Monat — "
            "weil er 3 Sätze im Vertrag nie gelesen hat. In diesem Video zeige "
            "ich die 3 Sätze und die 3-Quote-Regel, die das behebt."
        ),
        "hashtags": ["#insurance", "#lifeinsurance", "#personalfinance", "#financetips", "#policy"],
    },
    8: {
        "palette": "Weltkarte-Hintergrund + Weiß (#FFFFFF) + Ozeanblau (#0891B2) Akzent",
        "face_rule": "Karten-Ausschnitt + Finanz-Dashboard, kein Gesicht",
        "text_style": "sans-serif bold, caps, max. 3 Wörter",
        "thumb_concepts": [
            {
                "visual": "Weltkarte mit rotem Pfeil USA → Portugal. Über dem Pfeil ein '$12K'-Label.",
                "overlay": "TAX MOVE",
                "ab": "A/B: Pfeil gerade vs gebogen, Karte sichtbar vs weg",
            },
            {
                "visual": "Drei Konto-Karten (Earn, Grow, Home) nebeneinander, jede mit eigener Währung.",
                "overlay": "3-ACCOUNT RULE",
                "ab": "A/B: Karten-Farbe uniform vs verschieden, Layout horizontal vs vertikal",
            },
            {
                "visual": "IRS-Formular mit 'FEIE' hervorgehoben, daneben grüner 'APPROVED'-Stempel.",
                "overlay": "THE 2 EXCEPTIONS",
                "ab": "A/B: Formular voll sichtbar vs nah, Stempel groß vs klein",
            },
        ],
        "ab_matrix": [
            "Karten-Stil: politisch vs minimalistisch",
            "Pfeil: gerade vs mit Flaggen",
            "Overlay: Zahl + Wort vs nur Wort",
        ],
        "tags_pool": [
            "expat taxes", "us expat", "digital nomad taxes", "expat investing",
            "foreign tax credit", "feie", "us expat taxes", "expat finance",
            "expat broker", "interactive brokers expat", "wise vs revolut",
            "expat 2026", "retire abroad", "expat portfolio", "cross border tax",
            "portugal expat", "spain expat", "expat money",
        ],
        "section_labels": {
            "hook": "Hook — die 2 Steuer-Ausnahmen",
            "agitation": "Warum Expats 12K zu viel zahlen",
            "solution": "Die 3-Account-Regel",
            "insights": "3 Fehler, die Portfolio kosten",
            "cta": "Country-Checkliste",
            "tease": "Nächstes Video",
        },
        "description_intro": (
            "Als US-Bürger im Ausland schuldest du dem IRS Geld — außer du nutzt "
            "die 2 Ausnahmen. In diesem Video zeige ich das 3-Account-System, "
            "mit dem Expats in 3 Ländern sauber wirtschaften können."
        ),
        "hashtags": ["#expat", "#digitalnomad", "#taxes", "#expats", "#crossborder"],
    },
    9: {
        "palette": "Schwarz (#0F0F0F) + Matrix-Grün (#22C55E) + Cyan (#06B6D4) Akzent",
        "face_rule": "Terminal-Screenshot + Stack-Badge-Grafik, kein Gesicht",
        "text_style": "monospace bold, caps, max. 4 Wörter",
        "thumb_concepts": [
            {
                "visual": "Zertifikat-Freisteller mit 'SEC+ PASSED' + grüner Haken. Hintergrund: Matrix-Code.",
                "overlay": "PASSED IN 42D",
                "ab": "A/B: Hintergrund Matrix vs Studio-Schwarz, Zertifikat hell vs dunkel",
            },
            {
                "visual": "Ladder-Grafik: Helpdesk → SOC → Analyst, jede Stufe mit einem Zert-Badge.",
                "overlay": "THE CERT LADDER",
                "ab": "A/B: Ladder sichtbar vs nur Zert-Badges, Pfeile grün vs cyan",
            },
            {
                "visual": "Split: links Bewerbungen 100 (grau), rechts '3 Interviews' (grün, groß).",
                "overlay": "100 → 3",
                "ab": "A/B: Zahlen-Reihenfolge, Hintergrund dunkel vs grau",
            },
        ],
        "ab_matrix": [
            "Terminal: echtes Terminal vs abstrakt",
            "Farbe: grün vs cyan",
            "Badge-Stil: rund vs eckig",
        ],
        "tags_pool": [
            "security+ certification", "comptia security+", "cysa+", "oscp",
            "soc analyst", "cybersecurity careers", "cybersecurity certifications",
            "tryhackme", "hackthebox", "security+ exam prep", "cybersecurity 2026",
            "soc analyst salary", "home lab cybersecurity", "cyber career path",
            "security+ study plan", "cybersecurity for beginners", "cert roadmap",
            "cyber interview prep",
        ],
        "section_labels": {
            "hook": "Hook — Security+ in 60 Tagen",
            "agitation": "Warum Certs alleine keinen Job bringen",
            "solution": "Die Cert-Ladder-Methode",
            "insights": "3 Schritte zur ersten Cyber-Rolle",
            "cta": "Cert-Ladder-Grafik",
            "tease": "Nächstes Video",
        },
        "description_intro": (
            "Ich habe 100 Bewerbungen im Cyber-Bereich geschickt — 97 wurden "
            "abgelehnt. In diesem Video zeige ich die 3 Schritte, die den "
            "Unterschied machen, plus die Cert-Ladder für die nächsten 12 Monate."
        ),
        "hashtags": ["#cybersecurity", "#securityplus", "#soc", "#career", "#comptia"],
    },
    10: {
        "palette": "Weiß (#FFFFFF) + Dunkelgrün (#065F46) + Gold (#CA8A04) Akzent",
        "face_rule": "Policy-Dokument + Häkchen-Stempel, kein Gesicht",
        "text_style": "sans-serif bold, sentence-case, max. 4 Wörter",
        "thumb_concepts": [
            {
                "visual": "Policy-Dokument-Stapel mit Häkchen über jedem, im Hintergrund Kalender mit '6 WOCHEN'.",
                "overlay": "6-WEEK SPRINT",
                "ab": "A/B: Stapel komplett vs 1 Dokument, Häkchen einzeln vs gesamt",
            },
            {
                "visual": "GDPR-Klage-Schreiben mit rotem '$40K FINE'-Overlay, oben rechts ein ⚠️-Icon.",
                "overlay": "$40K FINE",
                "ab": "A/B: Warn-Icon rot vs gelb, Overlay groß vs klein",
            },
            {
                "visual": "Compliance-Checkliste 12 Punkte, 6 abgehakt grün, 6 offen grau.",
                "overlay": "12 POLICIES",
                "ab": "A/B: Häkchen grün vs schwarz, Checkliste horizontal vs vertikal",
            },
        ],
        "ab_matrix": [
            "Dokument-Stil: gedruckt vs digital",
            "Overlay-Farbe: grün vs rot",
            "Stempel: rund vs eckig",
        ],
        "tags_pool": [
            "gdpr", "hipaa", "smb compliance", "privacy policy", "compliance template",
            "gdpr 2026", "hipaa 2026", "small business compliance", "compliance audit",
            "policy template", "dpo", "compliance sprint", "compliance for smb",
            "gdpr basics", "hipaa basics", "cookie policy", "audit prep", "compliance under 500",
        ],
        "section_labels": {
            "hook": "Hook — 6 Wochen statt 6 Monate",
            "agitation": "Warum Berater 15K verlangen",
            "solution": "Der 6-Wochen-Sprint",
            "insights": "3 Policies, die Audits entscheiden",
            "cta": "12-Policy-Bundle",
            "tease": "Nächstes Video",
        },
        "description_intro": (
            "Die meisten SMBs brauchen kein Compliance-Programm — sie brauchen "
            "6 Wochen. In diesem Video zerlege ich den 6-Wochen-Audit-Sprint, "
            "mit dem du für unter 500€/Monat audit-fähig wirst."
        ),
        "hashtags": ["#gdpr", "#hipaa", "#compliance", "#smallbusiness", "#smb"],
    },
}


# Manuelle SEO-Overrides pro (niche, video) — überschreiben Auto-Generierung
SEO_OVERRIDES = {
    (1, 1): {
        "seo_title": "How I Automated 90% of My SaaS Ops (Notion + Zapier)",
        "tags": [
            "saas automation", "notion automation", "zapier tutorial",
            "airtable tips", "saas ops", "small saas founder",
            "workflow automation", "automate saas", "ops stack",
            "saas tutorial 2026",
        ],
    },
    (2, 1): {
        "seo_title": "How to File Small Claims (California, 2026 Full Guide)",
        "tags": [
            "small claims court", "small claims california", "pro se legal",
            "file small claims", "legal self defense", "diy legal",
            "small claims filing", "small claims 2026", "court without lawyer",
            "small claims process",
        ],
    },
    (3, 1): {
        "seo_title": "CPC Certification in 90 Days — Full Roadmap (2026)",
        "tags": [
            "cpc certification", "medical coding", "medical coder",
            "aapc exam", "medical coding roadmap", "coding career",
            "medical coding 2026", "cpc exam prep", "medical coding salary",
            "certification prep",
        ],
    },
    (9, 1): {
        "seo_title": "Security+ in 60 Days — The Only Roadmap You Need",
        "tags": [
            "security+ certification", "comptia security+", "security+ exam prep",
            "cybersecurity careers", "cert roadmap", "soc analyst",
            "cybersecurity 2026", "cybersecurity for beginners", "security+ study plan",
            "cyber career path",
        ],
    },
}


def shorten_title(title: str, max_len: int = 58) -> str:
    if len(title) <= max_len:
        return title
    for sep in [":", " — ", " - ", "?"]:
        if sep in title:
            head = title.split(sep)[0].strip()
            if 15 <= len(head) <= max_len:
                return head
    words = title.split()
    out: list[str] = []
    for w in words:
        candidate = " ".join(out + [w])
        if len(candidate) <= max_len:
            out.append(w)
        else:
            break
    return " ".join(out) + "…"

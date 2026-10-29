"""Growth & Repurposing Engine — Plattform-Priorität + Format-Templates pro Nische."""

REPURPOSE = {
    1: {
        "platforms": [
            ("YouTube", "Evergreen-Suche · 70% organisches Traffic · Kernformat"),
            ("Email", "Operator-Liste · 28% Open Rate · höchster Lifetime-Value"),
            ("Twitter/X", "SaaS-Twitter aktiv · Threads 8–12× normale Posts"),
            ("LinkedIn", "SaaS-Founder-Publikum · 4× organische Reichweite"),
            ("Pinterest", "Niedrig · Screencasts funktionieren visuell schlecht"),
        ],
        "shorts_hooks": [
            ("Die 3-Layer-Regel in 45 Sekunden", "Whiteboard-Stil, kein Tool nennen, nur das Modell — endet mit 'Video in Beschreibung'"),
            ("Ich habe 6 Monate keinen Task angefasst", "POV-Perspektive, Stack im Hintergrund sichtbar, Sprecher spricht gegen Kamera"),
            ("Zapier rettet dein Ops-System nicht", "Contrarian-Hook, Beweis folgt Sekunde 5–20, CTA am Ende"),
        ],
        "email_subjects": [
            "3 Layer, 0 manuelle Tasks",
            "Der Stack, den ich auf YouTube nie komplett zeige",
            "15 Stunden → 90 Minuten pro Woche",
        ],
        "pinterest": {
            "board": "SaaS Ops Templates & Automation",
            "description": "SaaS-Ops mit 4 Tools und 1 Regel. Airtable als Intake, Zapier/Make als Automate, Metabase als Measure. Der komplette 3-Layer-Stack für Solo-Founder — ohne Ops-Hire. Schritt-für-Schritt-Walkthrough im Video. #saas #automation #notion #zapier #startup",
        },
        "linkedin_opener": (
            "Ich habe 6 Monate keinen manuellen Task in meiner SaaS angefasst.\n\n"
            "Kein Copy-Paste zwischen Tools. Kein Ticket-Routing. Kein Excel-Dashboard.\n\n"
            "Die Regel dahinter ist simpler, als die meisten Ops-Beratungen vermuten lassen."
        ),
    },
    2: {
        "platforms": [
            ("YouTube", "Suche-intent-getrieben · Pro-Se-Publikum sucht aktiv"),
            ("Email", "Höchste Lead-Conversion · Nutzer wollen Vorlagen"),
            ("Twitter/X", "Legal-Twitter klein, aber hohe Conversion-Rate"),
            ("LinkedIn", "Niedrig — Pro-Se nicht LinkedIn-Publikum"),
            ("Pinterest", "Mittel — Vorlagen-Pins performen (State-by-State)"),
        ],
        "shorts_hooks": [
            ("Der Richter liest 3 Minuten pro Fall", "Direkt in Kamera, Beweis in Sekunde 3, CTA am Ende"),
            ("4.200 $ Anwalt vs 75 $ Filing-Gebühr", "Split-Screen-Visual, keine Erklärung — nur die Zahl"),
            ("Die 5 Aktenstücke, die du brauchst", "Whiteboard-Stil, jedes Piece mit Icon"),
        ],
        "email_subjects": [
            "Ich habe 3 Verfahren ohne Anwalt geführt",
            "Die 5-Piece-Akte, die Richter wirklich lesen",
            "4.200 $ gespart — so ging es",
        ],
        "pinterest": {
            "board": "Small Claims Court Templates",
            "description": "Small Claims selbst filing — 5-Piece-Case-File-System, State-spezifische Vorlagen, Zustell-Guides und Beweis-Chronologie. Ohne Anwalt, ohne $4.200 Rechnung. Für Mieter, Käufer und kleine Auftraggeber. #smallclaims #prose #legal #court #diy",
        },
        "linkedin_opener": (
            "Ich habe 3 Gerichtsverfahren allein durchgezogen — ohne Anwalt.\n\n"
            "Der erste hätte mich 4.200 Dollar gekostet.\n\n"
            "Der Unterschied war nicht das Recht. Es war die Akte."
        ),
    },
    3: {
        "platforms": [
            ("YouTube", "Career-Changer suchen aktiv · 70% Search-Traffic"),
            ("Pinterest", "Sehr stark — Career-Advice-Pins, hoher Traffic aus Suche"),
            ("Email", "Kurs-Käufer-Publikum · 32% Open Rate"),
            ("Twitter/X", "Niedrig — Career-Nische nicht Twitter-stark"),
            ("LinkedIn", "Mittel — Career-Changer folgen dort aktiv"),
        ],
        "shorts_hooks": [
            ("CPC in 42 Tagen bestanden — mit Vollzeitjob", "POV, Kalender im Hintergrund, Erfolgs-Story in 45s"),
            ("Du brauchst keine 70.000 Codes", "Contrarian, Whiteboard mit 60 Codes als Zahl"),
            ("Die 90-Tage-Sprint-Regel", "Screencast Notion-Roadmap, Wochen abhakbar"),
        ],
        "email_subjects": [
            "CPC in 42 Tagen — Tag für Tag",
            "Warum 9 Monate der Standard sind",
            "12 Wochen bis zur Prüfung",
        ],
        "pinterest": {
            "board": "Medical Coding Career Path",
            "description": "CPC-Zertifizierung in 90 Tagen — 12-Wochen-Roadmap, Prüfungs-Simulator und Job-Hunt-Playbook. Für Career-Changer ohne klinischen Hintergrund, die remote-fähige $45–65K-Jobs suchen. Tag-für-Tag-Plan im Video. #medicalcoding #cpc #career #certification #icd10",
        },
        "linkedin_opener": (
            "Ich habe CPC in 42 Tagen bestanden — mit einem Vollzeitjob.\n\n"
            "Der durchschnittliche Career-Changer braucht 9 Monate.\n\n"
            "Der Unterschied ist nicht mehr Zeit. Es ist ein Plan."
        ),
    },
    4: {
        "platforms": [
            ("YouTube", "Suche-intent · Erstkäufer suchen aktiv · sehr hohe Watch-Time"),
            ("Pinterest", "Sehr stark — Walkthrough-Bilder, Checklisten-Pins"),
            ("Email", "Käufer mit akutem Bedarf · 35% Open Rate"),
            ("LinkedIn", "Niedrig — Erstkäufer nicht LinkedIn-Publikum"),
            ("Twitter/X", "Niedrig — kein Kernformat"),
        ],
        "shorts_hooks": [
            ("10 Rote Flaggen in 10 Minuten", "Screencast-Foto, rote Kreise erscheinen nacheinander"),
            ("Das hat den Deal gekillt", "Talking head, kein Setup, nur Story"),
            ("40.000 $ Foundation in 10 Minuten gefunden", "Split-Screen: Bild des Risses vs. Rechnung"),
        ],
        "email_subjects": [
            "10 rote Flaggen, 80% der Kosten",
            "Die 200-Punkte-Checkliste",
            "40.000 $ Reparatur in 10 Minuten erkannt",
        ],
        "pinterest": {
            "board": "Home Inspection Checklists",
            "description": "200-Punkte-Inspektions-Checkliste für Erstkäufer und angehende Inspectors. Foundation, Dach, Feuchtigkeit — 3 Kategorien, 80% der Kosten. Komplette Walkthrough-Methode im Video. #homeinspection #realestate #firsttimebuyer #property #checklist",
        },
        "linkedin_opener": (
            "Von 10 Häusern, die ich inspiziere, haben 9 mindestens eine rote Flagge, die der Käufer übersehen hätte.\n\n"
            "Ein Käufer hat 40.000 Dollar Reparatur gespart, weil ich in 10 Minuten angerufen habe.\n\n"
            "Das war kein Zufall. Das war eine Checkliste."
        ),
    },
    5: {
        "platforms": [
            ("YouTube", "Suche + Empfehlungs-Traffic · hohe Completion · B2B-Premium-CPMs"),
            ("Pinterest", "Sehr stark — Diagramm-Pins performen in Engineering-Suche"),
            ("Twitter/X", "Mittel — Engineering-Twitter aktiv, Threads performen"),
            ("Email", "Mittel — Engineering-Kurse brauchen Nurturing"),
            ("LinkedIn", "Mittel — B2B-Industrial, aber langsamer Aufbau"),
        ],
        "shorts_hooks": [
            ("Jede Alu-Dose war 6 Wochen in Produktion", "Produktions-Footage, Zeitraffer, Ende mit Prozess-Diagramm"),
            ("5 Stufen, jedes Produkt — jede Fabrik", "Whiteboard, 5 Icons erscheinen nacheinander"),
            ("0.001 mm entscheiden Milliarden", "Nahaufnahme CNC, Toleranz-Zahl erscheint"),
        ],
        "email_subjects": [
            "5 Stufen — jedes physische Produkt",
            "Die Kette hinter deiner Alu-Dose",
            "Warum China nicht wegen Lohn dominiert",
        ],
        "pinterest": {
            "board": "Manufacturing Process Diagrams",
            "description": "Die 5-Stage-Production-Lens — Input, Form, Join, Finish, QC. Jede Fabrik folgt dieser Kette. Poster mit allen 20 Prozessen, PDF-Version im Video. Für Maschinenbau-Studenten und Ingenieure. #manufacturing #engineering #howitsmade #industrial #factory",
        },
        "linkedin_opener": (
            "Jede Alu-Dose, die du in der Hand hältst, war 6 Wochen in einem Prozess.\n\n"
            "Kein Witz. Sechs Wochen.\n\n"
            "Und dieser Prozess folgt einem Modell, das fast niemand kennt."
        ),
    },
    6: {
        "platforms": [
            ("YouTube", "Suche-intent · Steuer-Termine als Trigger · hohe Conversion"),
            ("Email", "Höchste Affiliate-Conversion · 30% Open Rate"),
            ("Pinterest", "Stark — Template-Pins für Small-Business-Bookkeeping"),
            ("LinkedIn", "Mittel — SMB-Owner sind dort, aber langsamer Aufbau"),
            ("Twitter/X", "Niedrig — SMB nicht Twitter-Publikum"),
        ],
        "shorts_hooks": [
            ("Die 15-Minuten-Close-Regel", "Screencast Template, Monats-Routine abhakbar"),
            ("QuickBooks vs Xero — 30 Tage Test", "Split-Screen, Zahlen unterlegt"),
            ("Do you actually need a bookkeeper?", "Talking head, ruhig, contrarian"),
        ],
        "email_subjects": [
            "15 Minuten pro Woche — fertig",
            "QBO vs Xero — 30 Tage Test",
            "Der $1.800 Buchhalter vs $0 DIY",
        ],
        "pinterest": {
            "board": "Small Business Bookkeeping",
            "description": "Month-End-Close in 4 Wochen × 15 Minuten. Chart of Accounts, Close-Routine, Tax-Ready-Books — komplette Templates für Small-Business-Owner, die DIY buchen. Schritt-für-Schritt im Video. #bookkeeping #quickbooks #xero #smallbusiness #accounting",
        },
        "linkedin_opener": (
            "Die meisten Small-Business-Owner hassen Buchhaltung, weil sie glauben, sie müssen sie verstehen.\n\n"
            "Müssen sie nicht. Sie müssen nur das System verstehen.\n\n"
            "Das ist der Unterschied."
        ),
    },
    7: {
        "platforms": [
            ("YouTube", "Suche-intent · Versicherung-CPM im Top-3 · hohe Kaufabsicht"),
            ("Email", "Sehr hohe Conversion · Lead-Nurturing kritisch"),
            ("Pinterest", "Mittel — Infografiken zu Policy-Vergleichen funktionieren"),
            ("Twitter/X", "Niedrig — Finance-Twitter zu breit"),
            ("LinkedIn", "Niedrig — Versicherung selten LinkedIn-Thema"),
        ],
        "shorts_hooks": [
            ("340 $ zu viel pro Monat — 3 Sätze", "Dokument-Freisteller, roter Kreis auf Exclusion-Klausel"),
            ("Term vs Whole — die ehrliche Rechnung", "Split-Screen, Zahlen groß, kein Gesicht"),
            ("Der Claim, der abgelehnt wurde", "Talking head, ruhig, Story-fokussiert"),
        ],
        "email_subjects": [
            "Die 3 Sätze, die Claims entscheiden",
            "340 $ zu viel pro Monat",
            "3-Quote-Regel für jede Police",
        ],
        "pinterest": {
            "board": "Insurance Policy Comparisons",
            "description": "Term vs Whole Life, Disability, Umbrella — ehrlicher Vergleich mit echten Zahlen. Die 3 Sätze, die Claims entscheiden, plus 3-Quote-Checkliste für deine eigene Police. Neutral, keine Agentur-Brille. #insurance #lifeinsurance #policy #personalfinance #financetips",
        },
        "linkedin_opener": (
            "Der durchschnittliche Familienvater zahlt 340 Dollar zu viel pro Monat für Versicherungen.\n\n"
            "Weil er 3 Sätze im Vertrag nie gelesen hat.\n\n"
            "Diese 3 Sätze kenne ich inzwischen auswendig."
        ),
    },
    8: {
        "platforms": [
            ("YouTube", "Evergreen-Suche · höchste Kaufkraft · Finanz-CPM Top-1%"),
            ("Email", "Expat-Listen extrem wertvoll · 40%+ Open Rate"),
            ("Pinterest", "Stark — Country-Guides und Infografiken"),
            ("Twitter/X", "Mittel — Finance-Twitter aktiv, aber laut"),
            ("LinkedIn", "Mittel — Expats als Founder/Remote-Worker dort aktiv"),
        ],
        "shorts_hooks": [
            ("Die 2 Ausnahmen für US-Expats", "Whiteboard, 2 Icons, IRS-Formular im Hintergrund"),
            ("Portugal vs Spanien — Steuer-Vergleich", "Split-Screen, Zahlen groß"),
            ("3-Konto-Regel für Expats", "Screencast IBKR, 3 Konten markiert"),
        ],
        "email_subjects": [
            "Die 2 Steuer-Ausnahmen für Expats",
            "Portugal vs Spanien — die Wahrheit",
            "12.000 $ zu viel Steuern — jedes Jahr",
        ],
        "pinterest": {
            "board": "Expat Finance & Cross-Border Tax",
            "description": "3-Konto-Regel für Expats: Earn, Grow, Home — jedes mit eigener Währung und Zweck. FEIE, Foreign Tax Credit, Broker-Setups für 12 Länder. Country-Tax-Checkliste als PDF im Video. #expat #digitalnomad #taxes #crossborder #financetips",
        },
        "linkedin_opener": (
            "Wenn du als US-Bürger im Ausland lebst, schuldest du dem IRS Geld.\n\n"
            "Außer du nutzt die 2 Ausnahmen.\n\n"
            "Die meisten Expats zahlen 12.000 Dollar zu viel im ersten Jahr."
        ),
    },
    9: {
        "platforms": [
            ("YouTube", "Suche-intent · Career-Changer aktiv · Cert-Voucher-Conversions"),
            ("Pinterest", "Stark — Career-Path-Pins, Roadmap-Grafiken"),
            ("Email", "Kurs-Publikum · 30% Open Rate"),
            ("Twitter/X", "Mittel — Cyber-Twitter sehr aktiv, Threads performen"),
            ("LinkedIn", "Mittel — SOC-Rollen werden dort gesucht"),
        ],
        "shorts_hooks": [
            ("Security+ in 60 Tagen — die Roadmap", "Screencast Notion-Roadmap, Wochen abhakbar"),
            ("Ich habe 100 Bewerbungen geschickt", "Split-Screen 100 → 3, contrarian"),
            ("Die Cert-Ladder-Methode", "Diagramm mit 3 Stufen, Cert-Badge je Stufe"),
        ],
        "email_subjects": [
            "Security+ in 60 Tagen — Tag für Tag",
            "97 von 100 Bewerbungen abgelehnt — hier ist warum",
            "Die Cert-Ladder, die wirklich funktioniert",
        ],
        "pinterest": {
            "board": "Cybersecurity Career Paths",
            "description": "Cert-Ladder-Methode: jede Zertifizierung wird erst nach konkretem Job-Titel empfohlen. Security+, CySA+, OSCP — mit Gehalts-Zahlen und Study-Plänen. Home-Lab-Setup unter 300€. #cybersecurity #securityplus #comptia #career #certification",
        },
        "linkedin_opener": (
            "Ich habe 100 Bewerbungen im Cyber-Bereich geschickt.\n\n"
            "97 wurden abgelehnt.\n\n"
            "Hier ist, was den Unterschied gemacht hat."
        ),
    },
    10: {
        "platforms": [
            ("YouTube", "Suche-intent · Audit-Trigger · Compliance-CPMs Top-5"),
            ("Email", "B2B-SMB-Publikum · 25% Open Rate · hoher LTV"),
            ("LinkedIn", "Sehr stark — SMB-Owner und Ops-Leads aktiv"),
            ("Twitter/X", "Niedrig — Compliance nicht Twitter-Thema"),
            ("Pinterest", "Mittel — Policy-Templates funktionieren"),
        ],
        "shorts_hooks": [
            ("6 Wochen statt 6 Monate Compliance", "Screencast Checkliste, Wochen abhakbar"),
            ("Die 12 Pflicht-Policies", "Whiteboard, 12 Icons erscheinen in 20 Sekunden"),
            ("40.000 Euro GDPR-Strafe — und der Fix", "Talking head, Dokument sichtbar"),
        ],
        "email_subjects": [
            "6 Wochen statt 6 Monate",
            "Die 12 Policies, die zählen",
            "40.000 Euro Strafe — hier ist der Fix",
        ],
        "pinterest": {
            "board": "GDPR & HIPAA Templates for SMBs",
            "description": "6-Wochen-Compliance-Sprint für SMBs: 12 Pflicht-Policies, GDPR + HIPAA, Audit-Readiness für unter 500€/Monat. Templates, Checklisten und Gap-Analyse — Schritt-für-Schritt im Video. #gdpr #hipaa #compliance #smallbusiness #smb",
        },
        "linkedin_opener": (
            "Ein Kunde hat mich nach einer 40.000-Euro-GDPR-Strafe angerufen.\n\n"
            "In 6 Wochen waren wir compliant.\n\n"
            "Hier ist das System."
        ),
    },
}

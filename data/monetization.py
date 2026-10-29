"""Monetization Stack pro Nische — Affiliate, Produkte, Pitch, Lead-Magnet, Tier-Modell."""

# Tier-Definitionen (Subscriber-Buckets → Tier-Key)
TIERS = [
    {"key": "T0", "label": "0–1K Abonnenten", "min": 0, "max": 1_000},
    {"key": "T1", "label": "1K–10K Abonnenten", "min": 1_000, "max": 10_000},
    {"key": "T2", "label": "10K–100K Abonnenten", "min": 10_000, "max": 100_000},
    {"key": "T3", "label": "100K+ Abonnenten", "min": 100_000, "max": 10_000_000},
]


def tier_for_subs(subs: int) -> str:
    for t in TIERS:
        if t["min"] <= subs < t["max"]:
            return t["key"]
    return "T3"


MONETIZATION = {
    1: {
        "niche": "B2B SaaS Tutorials & Workflow Automation",
        "lead_magnet": {
            "name": "3-Layer Ops Stack Template",
            "format": "Notion-Duplikat + 5 vorkonfigurierte Zapier-Zaps",
            "value_promise": "Dein Ops-Setup in 30 Minuten importierbar",
            "email_hook": "Trag deine E-Mail ein — Template landet sofort im Postfach, kein Verkaufs-Trichter.",
        },
        "affiliate": [
            {"tool": "Notion", "type": "Recurring 50% für 12 Monate", "rpm_range": "40–80 €/Monat aktiv", "link_hint": "notion.so/affiliate"},
            {"tool": "Zapier", "type": "20–30% recurring", "rpm_range": "50–120 €/Monat aktiv", "link_hint": "zapier.com/partner"},
            {"tool": "Make (Integromat)", "type": "Tiered CPA", "rpm_range": "30–90 €/Monat aktiv", "link_hint": "make.com/partners"},
            {"tool": "Airtable", "type": "CPA 20–50 €", "rpm_range": "20–50 €/Conversion", "link_hint": "airtable.com/affiliate"},
            {"tool": "N8N Cloud", "type": "20–30% recurring", "rpm_range": "20–60 €/Monat aktiv", "link_hint": "n8n.io/affiliate"},
        ],
        "products": [
            {"name": "Ops Stack Pro Pack", "format": "Notion + Zap Templates + 3 Case Studies", "price": "49–99 €", "launch_at": "T1"},
            {"name": "Automation Audit (done-with-you)", "format": "60-Min Call + Notion-Audit", "price": "299 €", "launch_at": "T2"},
            {"name": "SaaS Ops Cohort", "format": "4-Wochen Live-Kurs", "price": "699–1.299 €", "launch_at": "T2"},
            {"name": "Fractional Ops Retainer", "format": "monatliche Begleitung, 2 Calls", "price": "1.500–3.000 €/Monat", "launch_at": "T3"},
        ],
        "sponsorships": {
            "rate_per_1k_views": "25–60 €",
            "target_brands": ["Notion", "Zapier", "Make", "Airtable", "N8N", "Pipedream", "Retool"],
            "pitch_angle": "Operator-Publikum, 70% Solo-Founder/Head-of-Ops, 85% US/EU, niedrige Frequenz, hohe Watch-Time.",
        },
        "tiers": {
            "T0": {"monthly_range": "0–150 €", "focus": "E-Mail-Liste aufbauen, 0 Verkaufsdruck", "plays": ["Lead-Magnet pushen", "1 Affiliate pro Video", "Community aufbauen (Discord/Skool)"]},
            "T1": {"monthly_range": "150–800 €", "focus": "Affiliate + erstes Mini-Produkt", "plays": ["2 Affiliate-CTAs pro Video", "Pro Pack launchen", "E-Mail-Sequenz mit 5 Mails"]},
            "T2": {"monthly_range": "800–4.000 €", "focus": "Produkt + Cohort + erste Sponsorships", "plays": ["Cohort starten", "Erste Sponsorships pitchen", "Funnel mit Lead-Magnet → Pro Pack → Cohort"]},
            "T3": {"monthly_range": "4.000–20.000 €", "focus": "Retainer + wiederkehrende Sponsorships", "plays": ["Fractional Ops Retainer", "Q-Sponsorship-Deals", "Community-Mitgliedschaft 39 €/Monat"]},
        },
        "revenue_model_note": "AdSense macht bei diesen CPMs <15% des Umsatzes aus. Fokus: Affiliate (recurring) > Produkt > Sponsorship.",
    },
    2: {
        "niche": "Small Claims Court & Consumer Legal Self-Defense",
        "lead_magnet": {
            "name": "5-Piece Case File Starter",
            "format": "5 PDF-Vorlagen + 1 Erklär-Video (10 Min)",
            "value_promise": "Deine Klage strukturiert in 20 Minuten",
            "email_hook": "Trag deine E-Mail ein — Vorlagen sofort, kein Upsell im Anhang.",
        },
        "affiliate": [
            {"tool": "LegalZoom", "type": "CPA 40–80 $", "rpm_range": "40–80 $/Conversion", "link_hint": "legalzoom.com/affiliate"},
            {"tool": "Rocket Lawyer", "type": "CPA 30–70 $", "rpm_range": "30–70 $/Conversion", "link_hint": "rocketlawyer.com/affiliate"},
            {"tool": "Nolo (Bücher/Templates)", "type": "8–15%", "rpm_range": "3–15 $/Conversion", "link_hint": "nolo.com/affiliate"},
            {"tool": "FindLaw Anwaltssuche", "type": "CPL 20–60 $", "rpm_range": "20–60 $/Lead", "link_hint": "findlaw.com/affiliate"},
            {"tool": "E-Notary / DocuSign", "type": "CPA 15–40 $", "rpm_range": "15–40 $/Conversion", "link_hint": "docusign.com/partners"},
        ],
        "products": [
            {"name": "State Filing Pack", "format": "State-spezifische Klage + Zustell-Guide", "price": "19–39 €", "launch_at": "T1"},
            {"name": "Full Case File Bundle", "format": "Alle 5 Vorlagen + Chronologie + Beweis-Guide", "price": "49–99 €", "launch_at": "T1"},
            {"name": "Case Review (done-with-you)", "format": "60-Min Video-Call, Akten-Audit", "price": "199–349 €", "launch_at": "T2"},
            {"name": "Pro Se Bootcamp", "format": "4-Wochen Live-Kurs", "price": "499–899 €", "launch_at": "T3"},
        ],
        "sponsorships": {
            "rate_per_1k_views": "30–70 €",
            "target_brands": ["LegalZoom", "Rocket Lawyer", "Nolo", "FindLaw", "LawDepot"],
            "pitch_angle": "Pro-Se-Publikum mit akutem Problem, 100% Kaufabsicht, US-only — höchste Conversion-Rate im Legal-Segment.",
        },
        "tiers": {
            "T0": {"monthly_range": "0–200 €", "focus": "Lead-Magnet + 1 Affiliate", "plays": ["Lead-Magnet oben in Beschreibung", "LegalZoom als Primary-CTA", "Pro-Se-Community aufbauen"]},
            "T1": {"monthly_range": "200–1.000 €", "focus": "Filing Pack launchen", "plays": ["State-Filing Pack 29 €", "2 Affiliates pro Video", "5-Mail-Welcome-Sequenz"]},
            "T2": {"monthly_range": "1.000–5.000 €", "focus": "Case Review + Bundle", "plays": ["Case Review 249 € als Upsell", "Bundle-Bundle", "Erste Sponsorships (LegalZoom, FindLaw)"]},
            "T3": {"monthly_range": "5.000–25.000 €", "focus": "Bootcamp + Sponsorships", "plays": ["Bootcamp 599 €", "Q-Sponsorship mit LegalZoom", "Compliance-Software-Affiliate (DocuSign etc.)"]},
        },
        "revenue_model_note": "Legal hat 100% Purchase-Intent — Affiliate-Conversions 5–10× höher als bei Finance-Content. Fokus: Lead-Gen + High-Ticket Case Review.",
    },
    3: {
        "niche": "Medical Coding & Billing Careers",
        "lead_magnet": {
            "name": "90-Tage-CPC-Roadmap",
            "format": "Notion-Template + PDF-Export (12 Wochen, abhakbar)",
            "value_promise": "Tag-für-Tag-Plan bis zur CPC-Prüfung",
            "email_hook": "Trag deine E-Mail ein — Notion-Link ist sofort da, kein Verkaufs-Trichter.",
        },
        "affiliate": [
            {"tool": "AAPC Kurse", "type": "CPA 50–200 $", "rpm_range": "50–200 $/Enrollment", "link_hint": "aapc.com/affiliate"},
            {"tool": "AAPC Membership", "type": "CPA 15–40 $", "rpm_range": "15–40 $/Conversion", "link_hint": "aapc.com/membership"},
            {"tool": "CareerStep", "type": "CPA 40–120 $", "rpm_range": "40–120 $/Enrollment", "link_hint": "careerstep.com/affiliate"},
            {"tool": "Medical Coding Academy", "type": "20–40%", "rpm_range": "100–400 $/Enrollment", "link_hint": "via Impact/ShareASale"},
            {"tool": "Pocket Prep (CPC)", "type": "20–30%", "rpm_range": "10–30 $/Conversion", "link_hint": "pocketprep.com/affiliate"},
        ],
        "products": [
            {"name": "CPC Exam Prep Bundle", "format": "200 Practice Qs + Cheat-Sheet", "price": "29–79 €", "launch_at": "T1"},
            {"name": "Coding Career Starter Kit", "format": "Resume + Interview-Prep + Job-Board", "price": "49–99 €", "launch_at": "T1"},
            {"name": "CPC Review Cohort", "format": "6-Wochen Live-Gruppe, 2 Calls/Woche", "price": "399–799 €", "launch_at": "T2"},
            {"name": "1:1 Exam Coaching", "format": "3 Calls à 60 Min", "price": "299–499 €", "launch_at": "T2"},
        ],
        "sponsorships": {
            "rate_per_1k_views": "20–45 €",
            "target_brands": ["AAPC", "CareerStep", "Pocket Prep", "Medical Coding Academy", "Ultimate Medical Academy"],
            "pitch_angle": "Career-Changer mit Kaufabsicht, 60% Frauen 28–45, 90% US, hohe Completion-Rate bei Kursen.",
        },
        "tiers": {
            "T0": {"monthly_range": "0–200 €", "focus": "Roadmap + AAPC-Affiliate", "plays": ["Roadmap als E-Mail-Gate", "AAPC als Primary-CTA", "TikTok/Shorts für Reach"]},
            "T1": {"monthly_range": "200–1.200 €", "focus": "Exam Prep Bundle", "plays": ["Bundle 49 €", "2 Affiliates pro Video", "6-Mail-Welcome-Serie (Learn → Prepare → Book)"]},
            "T2": {"monthly_range": "1.200–6.000 €", "focus": "Cohort + 1:1 Coaching", "plays": ["Review-Cohort 599 €", "1:1 Coaching upsell", "CareerStep Sponsorship"]},
            "T3": {"monthly_range": "6.000–25.000 €", "focus": "Skalierte Cohorts + Sponsorships", "plays": ["2 Cohorts parallel", "Q-Sponsorship AAPC", "Alumni-Community 29 €/Monat"]},
        },
        "revenue_model_note": "Bildungs-Affiliate zahlt pro Enrollment, nicht pro Klick — bei 10K Abonnenten 3–5 Enrollments/Monat = 500–1.500 € passiv.",
    },
    4: {
        "niche": "Home Inspection & Property Due Diligence",
        "lead_magnet": {
            "name": "200-Punkte-Inspektions-Checkliste",
            "format": "PDF (12 Seiten, abhakbar, mobil-optimiert)",
            "value_promise": "Der komplette Inspector-Walkthrough als PDF",
            "email_hook": "Trag deine E-Mail ein — PDF landet sofort im Postfach, keine Verkaufs-Mails danach.",
        },
        "affiliate": [
            {"tool": "Thermal-Kameras (FLIR, Hikmicro)", "type": "3–8%", "rpm_range": "10–60 $/Conversion", "link_hint": "Amazon Associates / Hersteller-Programme"},
            {"tool": "Moisture-Meter (Protimeter)", "type": "3–6%", "rpm_range": "5–25 $/Conversion", "link_hint": "Amazon Associates"},
            {"tool": "Inspector-Academy", "type": "CPA 30–80 $", "rpm_range": "30–80 $/Lead", "link_hint": "inspectoracademy.com/affiliate"},
            {"tool": "InterNACHI Kurse", "type": "10–20%", "rpm_range": "20–60 $/Enrollment", "link_hint": "nachi.org/affiliate"},
            {"tool": "HomeLight / Realtor-Tools", "type": "CPL 20–50 $", "rpm_range": "20–50 $/Lead", "link_hint": "homelight.com/partners"},
        ],
        "products": [
            {"name": "Inspector Starter Kit", "format": "Checkliste + 3 Formulare + Foto-Guide", "price": "29–59 €", "launch_at": "T1"},
            {"name": "Buyer Due-Diligence Pack", "format": "5 Checklisten + Verhandlungs-Guide", "price": "39–79 €", "launch_at": "T1"},
            {"name": "Inspector-Business-Kurs", "format": "8-Wochen-Kurs (Marketing + Pricing + Legal)", "price": "399–799 €", "launch_at": "T2"},
            {"name": "Report-Review-Service", "format": "1:1 Beratung, 30 Min, Foto-Upload", "price": "99–199 €", "launch_at": "T2"},
        ],
        "sponsorships": {
            "rate_per_1k_views": "15–40 €",
            "target_brands": ["Inspector-Academy", "InterNACHI", "FLIR", "HomeLight", "Rocket Mortgage"],
            "pitch_angle": "Käufer mit akutem Bedarf + angehende Inspectors als Fachkräfte — Dual-Audience, hohe Kaufbereitschaft.",
        },
        "tiers": {
            "T0": {"monthly_range": "0–150 €", "focus": "Checkliste + Amazon-Affiliate", "plays": ["Checkliste als E-Mail-Gate", "Amazon-Links in Beschreibung", "Shorts aus Walkthrough-Clips"]},
            "T1": {"monthly_range": "150–1.000 €", "focus": "Starter Kit + Inspector-Academy", "plays": ["Kit 39 €", "2 Affiliates pro Video", "Inspector-Academy als CTA"]},
            "T2": {"monthly_range": "1.000–5.000 €", "focus": "Kurs + Report-Review", "plays": ["Business-Kurs 599 €", "Report-Review 149 €", "Erste Sponsorships"]},
            "T3": {"monthly_range": "5.000–20.000 €", "focus": "Kurse + Sponsorships + Community", "plays": ["2 Kurse parallel", "Inspector-Community 39 €/Monat", "Q-Sponsorship"]},
        },
        "revenue_model_note": "Amazon-Affiliate trägt hier die Baseline, aber Inspector-Academy + eigene Kurse machen 80% des Umsatzes.",
    },
    5: {
        "niche": "Industrial Engineering & Manufacturing Explained",
        "lead_magnet": {
            "name": "5-Stage-Production-Lens-Poster",
            "format": "PDF-Poster (A2, druckbar) + kompakte Erklär-PDF",
            "value_promise": "Das Modell hinter jeder Fabrik — auf einem Poster",
            "email_hook": "Trag deine E-Mail ein — Poster ist sofort im Postfach, kein Upsell.",
        },
        "affiliate": [
            {"tool": "Fusion 360 / CAD", "type": "20–30%", "rpm_range": "50–150 €/Conversion", "link_hint": "autodesk.com/affiliate"},
            {"tool": "SolidWorks Kurse", "type": "CPA 30–100 €", "rpm_range": "30–100 €/Enrollment", "link_hint": "SolidWorks-Partner"},
            {"tool": "Engineering-Bücher (Amazon)", "type": "3–5%", "rpm_range": "2–10 €/Conversion", "link_hint": "Amazon Associates"},
            {"tool": "Coursera Engineering", "type": "20–30%", "rpm_range": "20–80 €/Enrollment", "link_hint": "coursera.org/affiliate"},
            {"tool": "Keyence / Sensorik", "type": "Lead-Gen 50–200 €", "rpm_range": "50–200 €/Lead", "link_hint": "direkt via Partner"},
        ],
        "products": [
            {"name": "Every-Process Cheat-Sheet Pack", "format": "20 Prozesse × 1 Seite PDF", "price": "19–39 €", "launch_at": "T1"},
            {"name": "Engineering Explained Course", "format": "10 Videos, 90 Min gesamt", "price": "79–149 €", "launch_at": "T2"},
            {"name": "CAD-Simulation Templates", "format": "Fusion 360 + SolidWorks Vorlagen", "price": "49–99 €", "launch_at": "T2"},
            {"name": "Engineering Career Accelerator", "format": "6-Wochen-Kurs", "price": "399–699 €", "launch_at": "T3"},
        ],
        "sponsorships": {
            "rate_per_1k_views": "30–70 €",
            "target_brands": ["Autodesk", "SolidWorks", "Keyence", "Siemens", "Bosch Rexroth"],
            "pitch_angle": "B2B-Industrial mit hohen CPMs — Sponsors zahlen 3–5× Standard-Raten für Ingenieurs-Publikum.",
        },
        "tiers": {
            "T0": {"monthly_range": "0–200 €", "focus": "Poster + Amazon", "plays": ["Poster als Gate", "CAD-Affiliate in jedem Video", "Reddit/Engineering-Foren"]},
            "T1": {"monthly_range": "200–1.500 €", "focus": "Cheat-Sheet + CAD-Templates", "plays": ["Cheat-Pack 29 €", "Fusion 360 Affiliate", "5-Mail-Sequenz"]},
            "T2": {"monthly_range": "1.500–8.000 €", "focus": "Course + Sponsorships", "plays": ["Course 99 €", "Erste Autodesk/Keyence Sponsorships", "YouTube-SEO auf Long-Tail"]},
            "T3": {"monthly_range": "8.000–30.000 €", "focus": "Career-Kurs + Q-Sponsorships", "plays": ["Career Accelerator 599 €", "Q-Deals mit 2 Herstellern", "Alumni-Community"]},
        },
        "revenue_model_note": "Industrial B2B zahlt Premium-CPMs — Sponsorships übersteigen hier oft Affiliate + Produkte kombiniert.",
    },
    6: {
        "niche": "Accounting & Bookkeeping for Small Business",
        "lead_magnet": {
            "name": "Month-End-Close-Template",
            "format": "Excel + Notion (beide identisch, parallel)",
            "value_promise": "Monatsabschluss in 4 Wochen × 15 Minuten",
            "email_hook": "Trag deine E-Mail ein — Template-Link sofort, keine Sales-Sequenz.",
        },
        "affiliate": [
            {"tool": "QuickBooks Online", "type": "CPA 50–150 $", "rpm_range": "50–150 $/Conversion", "link_hint": "quickbooks.intuit.com/affiliate"},
            {"tool": "Xero", "type": "CPA 30–100 $", "rpm_range": "30–100 $/Conversion", "link_hint": "xero.com/partner"},
            {"tool": "FreshBooks", "type": "CPA 40–120 $", "rpm_range": "40–120 $/Conversion", "link_hint": "freshbooks.com/affiliate"},
            {"tool": "Bench (Bookkeeping-Service)", "type": "CPA 100–200 $", "rpm_range": "100–200 $/Lead", "link_hint": "bench.co/affiliate"},
            {"tool": "TaxAct / TaxSlayer", "type": "CPA 15–40 $", "rpm_range": "15–40 $/Conversion", "link_hint": "via Impact"},
        ],
        "products": [
            {"name": "Bookkeeping Starter Kit", "format": "Chart of Accounts + Close-Routine + Templates", "price": "39–79 €", "launch_at": "T1"},
            {"name": "Small-Biz Books Audit", "format": "1:1 Review, 60 Min", "price": "149–299 €", "launch_at": "T2"},
            {"name": "DIY Bookkeeping Course", "format": "8 Videos, 90 Min", "price": "99–199 €", "launch_at": "T2"},
            {"name": "Bookkeeper-Founder Community", "format": "monatlich, Q&A + Templates", "price": "29 €/Monat", "launch_at": "T3"},
        ],
        "sponsorships": {
            "rate_per_1k_views": "25–55 €",
            "target_brands": ["QuickBooks", "Xero", "FreshBooks", "Bench", "Wave"],
            "pitch_angle": "SMB-Owner mit Finanz-Schmerz, hohe Kaufabsicht, 90% US — Intuit/Intacct zahlen Top-Raten.",
        },
        "tiers": {
            "T0": {"monthly_range": "0–200 €", "focus": "Template + QBO-Affiliate", "plays": ["Template als Gate", "QBO-Link in jedem Video", "Steuer-Saison-Content"]},
            "T1": {"monthly_range": "200–1.500 €", "focus": "Starter Kit + Xero", "plays": ["Kit 59 €", "QBO vs Xero Vergleich", "5-Mail-Sequenz"]},
            "T2": {"monthly_range": "1.500–7.000 €", "focus": "Course + Audit", "plays": ["Course 149 €", "Audit 249 € als Upsell", "Erste Sponsorships"]},
            "T3": {"monthly_range": "7.000–30.000 €", "focus": "Community + Q-Sponsor", "plays": ["Community 29 €/Monat", "Q-Sponsorship mit QBO/Xero", "Live-Kohorten"]},
        },
        "revenue_model_note": "QBO-Affiliate ist der Gold-Standard — 100–200 $ pro Signup, 10 Signups/Monat = 1.000–2.000 € passiv.",
    },
    7: {
        "niche": "Insurance Deep Dives (Life / Disability / Umbrella)",
        "lead_magnet": {
            "name": "3-Quote-Policy-Checkliste",
            "format": "PDF (2 Seiten, druckbar) + 3 Fine-Print-Sätze",
            "value_promise": "Deine Police in 15 Minuten prüfen",
            "email_hook": "Trag deine E-Mail ein — PDF sofort, keine Sales-Mails danach.",
        },
        "affiliate": [
            {"tool": "Policygenius", "type": "CPA 30–100 $", "rpm_range": "30–100 $/Lead", "link_hint": "policygenius.com/affiliate"},
            {"tool": "Ladder (Term Life)", "type": "CPA 40–80 $", "rpm_range": "40–80 $/Conversion", "link_hint": "ladderlife.com/affiliate"},
            {"tool": "Haven Life", "type": "CPA 30–70 $", "rpm_range": "30–70 $/Conversion", "link_hint": "havenlife.com/affiliate"},
            {"tool": "Bestow", "type": "CPA 25–60 $", "rpm_range": "25–60 $/Conversion", "link_hint": "bestow.com/affiliate"},
            {"tool": "Breeze (Disability)", "type": "CPA 30–90 $", "rpm_range": "30–90 $/Conversion", "link_hint": "meetbreeze.com/affiliate"},
        ],
        "products": [
            {"name": "Policy-Audit-Template", "format": "Excel + PDF (3-Sätze-Check)", "price": "19–39 €", "launch_at": "T1"},
            {"name": "Family Coverage Playbook", "format": "PDF + 3 Fallbeispiele", "price": "29–69 €", "launch_at": "T1"},
            {"name": "1:1 Policy Review", "format": "30 Min Video, 3-Quotes-Bewertung", "price": "99–199 €", "launch_at": "T2"},
            {"name": "Insurance-Decision-Course", "format": "6 Videos, 45 Min", "price": "79–149 €", "launch_at": "T2"},
        ],
        "sponsorships": {
            "rate_per_1k_views": "30–70 €",
            "target_brands": ["Policygenius", "Ladder", "Haven Life", "Bestow", "Breeze"],
            "pitch_angle": "Familien mit akutem Versicherungs-Bedarf, 90% US, hohe Kaufabsicht — Versicherungs-CPM ist Top-3 im Finance-Segment.",
        },
        "tiers": {
            "T0": {"monthly_range": "0–250 €", "focus": "Checkliste + Policygenius", "plays": ["Checkliste als Gate", "Policygenius als Primary-CTA", "Shorts aus 3-Sätze-Hooks"]},
            "T1": {"monthly_range": "250–1.500 €", "focus": "Audit-Template + Ladder", "plays": ["Audit 29 €", "2 Affiliates pro Video", "5-Mail-Sequenz"]},
            "T2": {"monthly_range": "1.500–8.000 €", "focus": "1:1 Review + Course", "plays": ["Review 149 €", "Course 99 €", "Erste Sponsorships (Policygenius)"]},
            "T3": {"monthly_range": "8.000–35.000 €", "focus": "Skalierte Reviews + Q-Sponsor", "plays": ["Skalierte Reviews (VA-stützt)", "Q-Sponsorship Ladder/Policygenius", "Community 29 €/Monat"]},
        },
        "revenue_model_note": "Versicherungs-Affiliate ist nicht recurring, aber pro Conversion 30–100 $ — bei 10K Abonnenten 5–10 Signups/Monat = 200–800 € passiv.",
    },
    8: {
        "niche": "Wealth Management for Expats & Cross-Border",
        "lead_magnet": {
            "name": "3-Account-Setup-Guide (12 Länder)",
            "format": "PDF (24 Seiten) + Excel-Rechner",
            "value_promise": "Dein Expat-Finanz-Setup in 30 Minuten geplant",
            "email_hook": "Trag deine E-Mail ein — PDF ist sofort da, keine Verkaufs-Sequenz.",
        },
        "affiliate": [
            {"tool": "Interactive Brokers", "type": "CPA 50–200 $", "rpm_range": "50–200 $/Account", "link_hint": "interactivebrokers.com/affiliate"},
            {"tool": "Wise", "type": "CPA 10–40 $", "rpm_range": "10–40 $/Conversion", "link_hint": "wise.com/affiliate"},
            {"tool": "Revolut", "type": "CPA 10–30 $", "rpm_range": "10–30 $/Signup", "link_hint": "revolut.com/affiliate"},
            {"tool": "Expat Tax Services (TFX)", "type": "CPA 50–150 $", "rpm_range": "50–150 $/Lead", "link_hint": "taxesforexpats.com/affiliate"},
            {"tool": "Schwab International", "type": "CPA 100–250 $", "rpm_range": "100–250 $/Account", "link_hint": "schwab.com/affiliate"},
        ],
        "products": [
            {"name": "Expat Setup Playbook", "format": "PDF + Excel-Rechner (12 Länder)", "price": "39–79 €", "launch_at": "T1"},
            {"name": "Country-Tax-Bundle", "format": "5 Länder-Tiefen-Guides", "price": "79–149 €", "launch_at": "T1"},
            {"name": "Expat-Finance-Audit", "format": "60-Min Call, Portfolio + Steuer", "price": "199–399 €", "launch_at": "T2"},
            {"name": "Expat-Finance-Course", "format": "8 Wochen, live", "price": "599–1.299 €", "launch_at": "T3"},
        ],
        "sponsorships": {
            "rate_per_1k_views": "35–80 €",
            "target_brands": ["Interactive Brokers", "Wise", "Revolut", "TFX", "Schwab"],
            "pitch_angle": "High-Income-Expats mit $80K+ Einkommen, 3+ Länder-Setup — Finanz-CPMs im Top-1%-Segment.",
        },
        "tiers": {
            "T0": {"monthly_range": "0–250 €", "focus": "Guide + Wise/Revolut", "plays": ["Guide als Gate", "Wise-Affiliate", "Reddit-Expat-Communities"]},
            "T1": {"monthly_range": "250–1.800 €", "focus": "Setup-Playbook + IBKR", "plays": ["Playbook 59 €", "IBKR-Affiliate", "5-Mail-Sequenz mit Länder-Filter"]},
            "T2": {"monthly_range": "1.800–10.000 €", "focus": "Audit + Country-Bundle", "plays": ["Audit 299 €", "Country-Bundle 99 €", "Erste Sponsorships"]},
            "T3": {"monthly_range": "10.000–40.000 €", "focus": "Course + Q-Sponsor", "plays": ["Course 899 €", "Q-Sponsorship IBKR/Schwab", "Community 39 €/Monat"]},
        },
        "revenue_model_note": "Expat-Audience hat höchste Kaufkraft aller Nischen — Affiliate-Conversions von IBKR/Schwab sind selten, aber 100–250 $ pro Account.",
    },
    9: {
        "niche": "Cybersecurity Careers & Certifications",
        "lead_magnet": {
            "name": "Cert-Ladder-Grafik (Job-Mapping)",
            "format": "PDF + PNG (druckbar, 1 Seite)",
            "value_promise": "Jede Cert → Job-Titel → Gehalt — auf einen Blick",
            "email_hook": "Trag deine E-Mail ein — Grafik sofort, kein Verkaufs-Trichter.",
        },
        "affiliate": [
            {"tool": "CompTIA Store", "type": "8–15%", "rpm_range": "30–60 $/Cert-Voucher", "link_hint": "comptia.org/affiliate"},
            {"tool": "TryHackMe", "type": "30–50%", "rpm_range": "10–30 $/Signup", "link_hint": "tryhackme.com/affiliate"},
            {"tool": "HackTheBox", "type": "20–40%", "rpm_range": "20–50 $/Signup", "link_hint": "hackthebox.com/affiliate"},
            {"tool": "Cybrary", "type": "20–30%", "rpm_range": "20–50 $/Signup", "link_hint": "cybrary.it/affiliate"},
            {"tool": "Coursera (Google Cyber)", "type": "20–45%", "rpm_range": "20–50 $/Enrollment", "link_hint": "coursera.org/affiliate"},
        ],
        "products": [
            {"name": "Cert-Roadmap-Bundle", "format": "5 Roadmaps + Study-Pläne", "price": "29–59 €", "launch_at": "T1"},
            {"name": "Home-Lab-Setup-Guide", "format": "PDF + Video-Walkthrough (30 Min)", "price": "19–39 €", "launch_at": "T1"},
            {"name": "SOC-Interview-Prep", "format": "50 Qs + Antworten + Mock-Interviews", "price": "49–99 €", "launch_at": "T2"},
            {"name": "Cyber-Career-Cohort", "format": "6 Wochen, live, mit Mentor", "price": "399–799 €", "launch_at": "T3"},
        ],
        "sponsorships": {
            "rate_per_1k_views": "25–55 €",
            "target_brands": ["CompTIA", "TryHackMe", "HackTheBox", "Cybrary", "Pluralsight"],
            "pitch_angle": "Career-Changer mit klarem Ziel (SOC-Rolle), 80% unter 35, 70% US, 40% Frauen — Cert-Käufer mit hoher Completion-Rate.",
        },
        "tiers": {
            "T0": {"monthly_range": "0–200 €", "focus": "Ladder + TryHackMe", "plays": ["Ladder als Gate", "TryHackMe-Affiliate", "Reddit r/cybersecurity"]},
            "T1": {"monthly_range": "200–1.500 €", "focus": "Roadmap-Bundle + Home-Lab", "plays": ["Bundle 49 €", "Home-Lab 29 €", "5-Mail-Sequenz"]},
            "T2": {"monthly_range": "1.500–8.000 €", "focus": "Interview-Prep + Cohort-Start", "plays": ["Interview-Prep 79 €", "Cohort 599 €", "CompTIA Sponsorship"]},
            "T3": {"monthly_range": "8.000–35.000 €", "focus": "Skalierte Cohorts + Q-Sponsor", "plays": ["2 Cohorts parallel", "Q-Sponsorship TryHackMe/Cybrary", "Alumni-Community 29 €/Monat"]},
        },
        "revenue_model_note": "Cybersecurity hat niedrigere Affiliate-Payouts als Finance, aber höhere Course-Completion — Cohort-Modell ist der Haupt-Hebel.",
    },
    10: {
        "niche": "Compliance, GDPR & HIPAA for SMBs",
        "lead_magnet": {
            "name": "12-Policy-Checkliste (GDPR + HIPAA)",
            "format": "PDF + Notion-Duplikat (12 Policies, sortiert nach Priorität)",
            "value_promise": "Audit-Fähigkeit in 6 Wochen — abhakbar",
            "email_hook": "Trag deine E-Mail ein — Checkliste ist sofort da, keine Sales-Mails.",
        },
        "affiliate": [
            {"tool": "Vanta", "type": "CPA 100–300 $", "rpm_range": "100–300 $/Demo", "link_hint": "vanta.com/partners"},
            {"tool": "Drata", "type": "CPA 100–250 $", "rpm_range": "100–250 $/Demo", "link_hint": "drata.com/partners"},
            {"tool": "Termly (Policy-Generator)", "type": "30–50%", "rpm_range": "20–50 $/Signup", "link_hint": "termly.io/affiliate"},
            {"tool": "iubenda", "type": "30%", "rpm_range": "20–40 $/Signup", "link_hint": "iubenda.com/affiliate"},
            {"tool": "Secureframe", "type": "CPA 80–200 $", "rpm_range": "80–200 $/Demo", "link_hint": "secureframe.com/partners"},
        ],
        "products": [
            {"name": "12-Policy-Bundle", "format": "GDPR + HIPAA Templates (12 Docs)", "price": "79–199 €", "launch_at": "T1"},
            {"name": "Audit-Readiness-Checkliste", "format": "PDF + Notion (6-Wochen-Plan)", "price": "29–59 €", "launch_at": "T1"},
            {"name": "1:1 Compliance-Audit", "format": "90 Min, Gap-Analyse", "price": "249–499 €", "launch_at": "T2"},
            {"name": "6-Wochen-Compliance-Cohort", "format": "Live-Gruppe, 6 Calls", "price": "599–1.299 €", "launch_at": "T3"},
        ],
        "sponsorships": {
            "rate_per_1k_views": "30–70 €",
            "target_brands": ["Vanta", "Drata", "Termly", "iubenda", "Secureframe"],
            "pitch_angle": "SMB-Owner mit akutem Audit-Trigger, 85% US/EU, hohe Conversion — Compliance-Software zahlt Top-CPMs.",
        },
        "tiers": {
            "T0": {"monthly_range": "0–200 €", "focus": "Checkliste + Termly", "plays": ["Checkliste als Gate", "Termly-Affiliate", "LinkedIn-Posts parallel"]},
            "T1": {"monthly_range": "200–1.500 €", "focus": "Policy-Bundle + Audit-Checkliste", "plays": ["Bundle 129 €", "Checkliste 39 €", "5-Mail-Sequenz"]},
            "T2": {"monthly_range": "1.500–8.000 €", "focus": "1:1 Audit + Vanta/Drata", "plays": ["Audit 349 €", "Vanta-Affiliate (Demo-CPA)", "Erste Sponsorships"]},
            "T3": {"monthly_range": "8.000–35.000 €", "focus": "Cohort + Q-Sponsor", "plays": ["Cohort 899 €", "Q-Sponsorship Vanta/Drata", "Compliance-Community 39 €/Monat"]},
        },
        "revenue_model_note": "Compliance-Software-Affiliate (Vanta/Drata) zahlt pro Demo-Lead — bei B2B-SMB-Publikum 3–5 Leads/Monat = 300–1.000 € passiv.",
    },
}

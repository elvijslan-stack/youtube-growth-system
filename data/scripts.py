"""Video-Script-System — Nischen-Profile + Template-Overrides."""

# Jedes Profil liefert: Tonalität, Hook-Formeln, Pain-Points,
# Insight-Winkel, CTA-Varianten, Tease-Mapping zu Roadmap-Videos.
# Der Renderer kombiniert Profil + Video-Titel zu einem vollen Script.

NICHE_PROFILES = {
    1: {
        "tone": "direkt, operative, kein Marketing-Sprech, Screencast-nah",
        "hooks": [
            "Ich habe seit 6 Monaten keinen manuellen Task mehr angefasst. Hier ist der Stack, der das möglich macht — in 7 Minuten komplett.",
            "Die meisten SaaS-Founder verbrennen 15 Stunden pro Woche in Ops. Ich zeige dir, wie ich das in 90 Minuten pro Woche gepresst habe.",
            "3 Tools. 1 Regel. 0 manuelle Tasks. Das ist die Ops, die ich wirklich fahre — keine Theorie.",
        ],
        "pains": [
            "Jeder neue Kunde = 20 Minuten Onboarding-Handarbeit",
            "Support-Tickets, die eigentlich nur Routing-Fehler sind",
            "Dashboards, die niemand aktuell hält",
            "Rechnungen, die manuell aus 4 Tools zusammengezogen werden",
        ],
        "insights": [
            "Die 3-Layer-Regel: Intake, Automate, Measure — niemals alle drei im selben Tool",
            "Zapier ist Klebstoff, nicht Gehirn — Logik gehört in Airtable oder N8N",
            "Der eigentliche Wert ist nicht die Automation — es ist der Monitor darüber",
            "Ein 20-Euro-Tool ersetzt keinen Prozess, aber es ersetzt 3 Stunden pro Woche",
            "Onboarding ist der einzige Ops-Teil, den der Kunde direkt spürt — dort lohnt sich Automatisierung zuerst",
            "Wenn du es nicht in Notion dokumentieren kannst, ist es nicht automatisiert",
            "Trigger + Bedingung + Aktion, nicht mehr — alles darüber ist ein Feature-Creep",
        ],
        "ctas": [
            "Lade das Template im ersten Kommentar — Stack ist komplett drin, du importierst in 30 Sekunden.",
            "Das Template mit allen Zaps + Notion-DB ist kostenlos verlinkt. Du kannst morgen mit Layer 1 starten.",
        ],
        "tease_pattern": "Im nächsten Video zerlege ich {next_title} — und zeige, welches Tool bei mir gewonnen hat.",
    },
    2: {
        "tone": "nüchtern, juristisch präzise, aber ohne Kanzlei-Ton",
        "hooks": [
            "Ich habe 3 Gerichtsverfahren allein durchgezogen — ohne Anwalt. Das erste hätte mich 4.200 Dollar gekostet. Das ist der komplette Filing-Prozess.",
            "Der Richter hat einmal gesagt: 'Die meisten hier verlieren nicht wegen des Rechts, sondern wegen der Akte.' Diese Akte baue ich mit dir heute.",
            "Ein Small-Claims-Fall ist 80 Prozent Papierarbeit und 20 Prozent Auftritt. Ich zeige dir das Papier.",
        ],
        "pains": [
            "Der erste Gedanke ist immer: Anwalt kostet mehr als der Streitwert",
            "Unklarheit über das zuständige Gericht und Filing-Gebühren",
            "Beweise liegen als Screenshots und lose PDFs im Handy",
            "Zustellung an Gegner, der die Annahme verweigert",
        ],
        "insights": [
            "Das 5-Piece-Case-File: Klage, Beweise, Chronologie, Zustellnachweis, Forderungsaufstellung — fehlt eins, verlierst du Struktur",
            "Der Richter liest max. 3 Minuten pro Fall — deine erste Seite entscheidet",
            "Zustellung ist nicht dein Problem — das Gericht hat Optionen, die du nicht kennst",
            "Beweise nach Datum ordnen, nicht nach Wichtigkeit — Richter denken chronologisch",
            "Die Forderungsaufstellung ist dein bester Hebel für Verhandlung",
            "Ein Vergleich vor dem Termin bringt oft mehr als ein Urteil — und spart Gebühren",
            "Small Claims sind öffentlich — das allein bewegt viele Gegner zur Zahlung",
        ],
        "ctas": [
            "Alle Vorlagen (Klage, Chronologie, Zustellungs-Nachweis) sind im ersten Kommentar verlinkt — kostenlos, State-spezifisch.",
            "Das Case-File-Bundle als PDF ist unten verlinkt. Du kannst heute Abend den ersten Entwurf fertig haben.",
        ],
        "tease_pattern": "Nächstes Video: {next_title} — die Beweise, die vor Gericht wirklich zählen.",
    },
    3: {
        "tone": "ermutigend, faktenbasiert, prüfungsfokussiert, kein Hype",
        "hooks": [
            "Ich habe CPC in 42 Tagen bestanden, mit einem Vollzeitjob. Die Roadmap, die ich dafür genutzt habe, ist in diesem Video komplett — Tag für Tag.",
            "Der durchschnittliche Career-Changer braucht 9 Monate bis zur CPC. Ich habe es in 90 Tagen geschafft. Das ist der Unterschied zwischen Plan und keinem Plan.",
            "Es gibt genau 4 Dinge, die über Bestehen oder Durchfallen entscheiden. Die meisten lernen die anderen 40.",
        ],
        "pains": [
            "Tausende ICD-10-Codes, aber kein System, welches zuerst",
            "Kurse kosten 3.000 Dollar und liefern trotzdem keine Prüfungs-Sicherheit",
            "Prüfungstermin rückt näher, aber Progress ist unsichtbar",
            "Kein Plan, wie man nach der Zertifizierung wirklich einen Job findet",
        ],
        "insights": [
            "Die 90-Tage-Sprint-Regel: 12 Wochen, jede Woche eine prüfbare Aufgabe — sichtbar abgehakt, sonst bleibt es beim 'irgendwann'",
            "Du brauchst keine 70.000 Codes — du brauchst 60, die im Prüfungsformat zirkulieren",
            "Practice Exams schlagen Reading — 2:1 Verhältnis im letzten Drittel",
            "Der Unterschied zwischen CPC und CCS ist nicht das Wissen, sondern die Karriere-Richtung",
            "Der Job-Markt ist nach der Zertifizierung offener als vorher — aber nur, wenn die Zertifizierung sichtbar wird",
            "Ein guter Resume ist 60 Prozent Zertifizierung, 40 Prozent Praxis-Sprache",
            "Remote-Jobs sind da draußen — aber nur für die, die die Prüfung als Filter nicht fürchten",
        ],
        "ctas": [
            "Die komplette 12-Wochen-Roadmap als Notion-Template ist im ersten Kommentar verlinkt — abhakbar, wöchentlich.",
            "Prüfungs-Simulator und Lernplan sind unten. Du kannst morgen mit Woche 1 starten.",
        ],
        "tease_pattern": "Nächstes Video: {next_title} — und welches Cert dich wirklich weiterbringt.",
    },
    4: {
        "tone": "praktisch, visuell, aus der Perspektive eines Inspektors",
        "hooks": [
            "Von 10 Häusern, die ich inspiziere, haben 9 mindestens eine rote Flagge, die der Käufer übersehen hätte. Diese 10 Flaggen zeige ich dir heute.",
            "Ein Käufer hat mal 40.000 Dollar Reparatur gespart, weil ich in 10 Minuten angerufen habe. Das war kein Zufall — das war eine Checkliste.",
            "Foundation, Dach, Feuchtigkeit — 3 Kategorien, 80 Prozent der Kosten. Das ist der Filter.",
        ],
        "pains": [
            "Erstkäufer verlassen sich komplett auf den Realtor — Interessenskonflikt",
            "Inspector-Berichte sind 60 Seiten und werden nie gelesen",
            "Augenscheinliche Kosmetik verdeckt strukturelle Probleme",
            "Bilder aus dem Handy reichen nicht als Verhandlungsbasis",
        ],
        "insights": [
            "Die 200-Punkte-Walkthrough-Methode: nummeriert, kategorisiert, abhakbar — sonst ist es Zufall",
            "Foundation-Risse sind selten das Problem — Feuchtigkeit darin ist es",
            "Ein Moisture-Meter für 40 Euro findet mehr als ein 400-Euro-Bericht",
            "Realtors sagen dir 'das ist normal' — dein Prüfpunkt ist, ob es normal ist oder typisch",
            "Das Dach siehst du nie vom Boden — frag nach Drohnen-Fotos oder geh selbst rauf, wenn sicher",
            "Thermal-Kameras sind kein Gimmick — sie zeigen Feuchtigkeit hinter Farbe",
            "Die Verhandlung beginnt nicht bei der Inspektion — sie beginnt beim ersten Bericht, den du liest",
        ],
        "ctas": [
            "Die komplette 200-Punkte-Checkliste als PDF ist im ersten Kommentar — kostenlos.",
            "Das Checklisten-Bundle mit 5 Kategorien + Foto-Template ist unten verlinkt.",
        ],
        "tease_pattern": "Nächstes Video: {next_title} — mit echten Fällen aus echten Inspektionen.",
    },
    5: {
        "tone": "erklärend, animations-nah, kindgerecht aber nicht kindisch",
        "hooks": [
            "Jede Alu-Dose, die du in der Hand hältst, war 6 Wochen in einem Prozess. Das ist die komplette Kette — in 8 Minuten.",
            "Das ist eine Spritzgussmaschine. Sie formt 90 Prozent aller Plastikteile, die du täglich anfasst. So funktioniert sie.",
            "Es gibt 5 Stufen, die jedes physische Produkt durchläuft. Egal ob Auto, Chip oder Turnschuh. Das ist das Modell.",
        ],
        "pains": [
            "Ingenieurs-Videos sind entweder zu trocken oder zu oberflächlich",
            "Man sieht Produkte, aber nie den Prozess dahinter",
            "YouTube-Dokus sind oft 40 Minuten für 5 Minuten Inhalt",
            "Schulen lehren Formeln, aber nicht, wie eine Fabrik aussieht",
        ],
        "insights": [
            "Die 5-Stage-Production-Lens: Input, Form, Join, Finish, QC — jede Fabrik folgt exakt dieser Kette",
            "Spritzguss ist nicht Gießen — es ist Pressen unter Druck, und der Unterschied ist entscheidend",
            "CNC ist keine Fabrik, es ist eine Familie von Werkzeugen — Fräsen, Drehen, Bohren haben unterschiedliche Logik",
            "Fast jede Fabrik hat einen Engpass, der nicht die Maschine ist, sondern der Mensch davor",
            "Die Ingenieursfehler, die du siehst, kommen meist aus der QC-Phase, nicht aus der Produktion",
            "Kleinste Toleranzen entscheiden über Milliarden — Mikrometer sind der eigentliche Business-Case",
            "Der wahre Grund, warum China dominiert, ist nicht Lohn — es ist die Prozess-Tiefe",
        ],
        "ctas": [
            "Die 5-Stage-Lens als PDF-Poster ist im ersten Kommentar verlinkt — druckbar.",
            "Alle 20 Fertigungsprozesse als Übersicht sind unten. Downloadbar, sortiert, abhakbar.",
        ],
        "tease_pattern": "Nächstes Video: {next_title} — und warum das mehr Maschinen sind, als du denkst.",
    },
    6: {
        "tone": "klar, beruhigend, ohne Steuerberater-Floskeln",
        "hooks": [
            "Die meisten Small-Business-Owner hassen Buchhaltung, weil sie glauben, sie müssen sie verstehen. Sie müssen nur das System verstehen. Das ist das Video.",
            "Ich habe 40 Firmen-Bücher aufgeräumt. Die häufigsten 3 Fehler sind in 90 Prozent von ihnen. Die zeige ich dir jetzt.",
            "QuickBooks und Xero versprechen beide das Gleiche. Ich habe 30 Tage mit beiden gearbeitet — hier ist der ehrliche Vergleich.",
        ],
        "pains": [
            "Steuer-Termin kommt, Bücher sind 3 Monate zurück",
            "QBO-Monatsabo gezahlt, aber 80 Prozent der Features nicht genutzt",
            "Der Steuerberater schickt eine Rechnung, die höher ist als der eigentliche Gewinn",
            "Die Angst, etwas falsch zu machen, lähmt die gesamte Buchhaltung",
        ],
        "insights": [
            "Die 15-Minuten-Close-Regel: eine wöchentliche Routine eliminiert den Monats-Schock",
            "QuickBooks gewinnt bei US-Steuer-Compliance, Xero bei Multi-Currency — wähle nach, was du wirklich brauchst",
            "Der Chart of Accounts ist 90 Prozent des Problems — fang klein an, wachse später",
            "Ein Steuerberater ist kein Buchhalter — die Rollen zu trennen spart 30-40 Prozent Kosten",
            "Das Month-End-Close ist ein Ritual, kein Projekt — 4 Wochen × 15 Minuten = fertig",
            "Wenn du drei Monate nicht gebucht hast, ist das Aufräumen teurer als laufend zu bleiben — immer",
            "Der teuerste Fehler im ersten Jahr ist nicht eine falsche Buchung — es ist die fehlende Dokumentation",
        ],
        "ctas": [
            "Das Month-End-Close-Template als Notion + Excel ist im ersten Kommentar — startklar.",
            "Der Buchhaltungs-Template-Bundle mit Chart of Accounts + Close-Routine ist unten.",
        ],
        "tease_pattern": "Nächstes Video: {next_title} — der Vergleich, den Buchhalter nicht machen wollen.",
    },
    7: {
        "tone": "ruhig, aufklärerisch, fine-print-fokussiert",
        "hooks": [
            "Der durchschnittliche Familienvater zahlt 340 Dollar zu viel pro Monat für Versicherungen, weil er 3 Sätze im Vertrag nie gelesen hat. Diese 3 Sätze zeige ich dir.",
            "Versicherungen sind kein Betrug — aber sie sind auch nicht dafür gebaut, dir zu helfen. Sie sind dafür gebaut, den Erwartungswert zu erfüllen. Das ist der Unterschied.",
            "Term vs Whole Life ist die häufigste Frage, die falsch beantwortet wird — von beiden Seiten. Ich mache es neutral.",
        ],
        "pains": [
            "Der Agent verkauft, was Provision bringt, nicht was passt",
            "Fine Print ist absichtlich unlesbar — aber es ist lesbar",
            "Vergleiche sind schwierig, weil jede Police anders formuliert ist",
            "Claim-Ablehnung nach Schadensfall ist die eigentliche Angst",
        ],
        "insights": [
            "Die 3-Quote-Regel: jede Empfehlung gegen 3 echte Angebote testen — sonst ist es Theorie",
            "Whole Life ist nicht böse — es ist ein teures Vehikel für ein einfaches Bedürfnis",
            "Term Life bis 30 Jahre deckt 90 Prozent der Bedürfnisse — der Rest ist Luxus",
            "Die Fine-Print-Sätze, die zählen, sind immer 3 — Exclusion, Waiting Period, Definition of Disability",
            "Disability Insurance ist die am meisten unterschätzte Police — und die am schwersten zu bekommende",
            "Ein Claim wird nicht abgelehnt wegen des Ereignisses — sondern wegen fehlender Doku",
            "Umbrella-Versicherung kostet 15 Euro pro Monat und deckt Löcher, die keine andere Police füllt",
        ],
        "ctas": [
            "Die 3-Quote-Checkliste als PDF ist im ersten Kommentar — mit den 3 Sätzen, die du immer suchst.",
            "Der Policy-Audit-Template-Bundle ist unten. Du kannst deine eigene Police heute prüfen.",
        ],
        "tease_pattern": "Nächstes Video: {next_title} — und die 3 Sätze, die Claims entscheiden.",
    },
    8: {
        "tone": "international, pragmatisch, steuer-bewusst",
        "hooks": [
            "Wenn du als US-Bürger im Ausland lebst, schuldest du dem IRS Geld — außer du nutzt die 2 Ausnahmen. Die zeige ich dir in 8 Minuten.",
            "Portugal gegen Spanien ist die häufigste Expat-Frage — aber die Steuer-Antwort ist nicht die, die du erwartest.",
            "Die meisten Expats zahlen 12.000 Dollar zu viel Steuern im ersten Jahr. Nicht aus Bosheit — aus Unwissenheit. Hier ist der Fix.",
        ],
        "pains": [
            "Doppel-Besteuerung, ohne zu wissen, wie man sie vermeidet",
            "Broker-Setups, die im einen Land funktionieren, im anderen nicht",
            "Währungsschwankungen, die 20 Prozent Portfolio auffressen",
            "Retirement-Konten, die beim Länderwechsel kollabieren",
        ],
        "insights": [
            "Die 3-Account-Regel: Earn, Grow, Home — jedes Konto hat eine Währung und einen Zweck, nie vermischen",
            "FEIE vs Foreign Tax Credit ist nicht 'entweder-oder' — es ist Situations-abhängig",
            "Interactive Brokers ist der Expat-Broker, nicht der beste — aber der zuverlässigste",
            "Wise ist keine Bank, Revolut ist keine Bank — beide sind Tools, und Tools brauchen Backups",
            "Das Land, in dem du Steuern zahlst, ist nicht das Land, in dem du Steuern schuldest",
            "Retirement-Konten über Grenzen sind der teuerste Fehler im Expat-Portfolio",
            "Die 3-Account-Regel funktioniert nur, wenn du jedes Konto jährlich prüfst — sonst driftet es",
        ],
        "ctas": [
            "Die Country-Tax-Checkliste für 12 Länder ist im ersten Kommentar — sortiert nach Steuer-Risiko.",
            "Der 3-Account-Setup-Guide als PDF ist unten. Du kannst heute dein Setup planen.",
        ],
        "tease_pattern": "Nächstes Video: {next_title} — mit echten Zahlen aus echten Fällen.",
    },
    9: {
        "tone": "ehrlich, karriere-orientiert, anti-hype",
        "hooks": [
            "Die Security+-Zertifizierung verspricht einen Job. Ich habe nachgezählt — sie liefert den ersten Schritt, nicht den Job. Der Unterschied ist ein 60-Tage-Plan.",
            "Ich habe 100 Bewerbungen im Cyber-Bereich geschickt. Hier ist, was 97 davon gekillt hat.",
            "Helpdesk zu SOC-Analyst in 9 Monaten ist möglich — aber nur, wenn du die 4 Schritte in der richtigen Reihenfolge machst.",
        ],
        "pains": [
            "Zertifizierungen ohne Job-Markt-Realität",
            "Helpdesk-Loops, aus denen man nicht rauskommt",
            "Interviews, die praktisch sind, aber man hat nur Theorie gelernt",
            "Home Labs, die nie zum Gesprächsthema werden",
        ],
        "insights": [
            "Die Cert-Ladder-Regel: jede Cert wird erst nach einer konkreten Job-Titel-Stufe empfohlen",
            "Security+ ist der Einstieg, nicht der Abschluss — CySA+ oder OSCP je nach Richtung",
            "Der Home Lab ist kein Hobby — er ist dein Interview-Material",
            "TryHackMe ist Anfänger-freundlich, HackTheBox ist Interview-realistisch — beide, nicht eins",
            "Der Job-Markt sucht SOC-Analysten, nicht Pentester — die Wahrnehmung ist falsch",
            "Die 4-Schritte-Reihenfolge: Cert, Lab, Portfolio, Bewerbung — nie überspringen",
            "Ein Interview gewinnt, wer seine Fehler erklären kann — nicht, wer alles weiß",
        ],
        "ctas": [
            "Die Cert-Ladder-Grafik mit Job-Titel-Mapping ist im ersten Kommentar — sortiert nach ROI.",
            "Der Home-Lab-Setup-Guide für unter 300 Euro ist unten verlinkt.",
        ],
        "tease_pattern": "Nächstes Video: {next_title} — und welche Cert wirklich den Unterschied macht.",
    },
    10: {
        "tone": "pragmatisch, audit-fokussiert, ohne Berater-Sprech",
        "hooks": [
            "Die meisten SMBs brauchen kein Compliance-Programm — sie brauchen 6 Wochen. Das ist der Sprint.",
            "Ein Kunde hat mich nach einer 40.000-Euro-GDPR-Strafe angerufen. In 6 Wochen waren wir compliant. Hier ist das System.",
            "GDPR und HIPAA klingen wie riesige Berge. Es sind 12 Policies, die zählen. Ich zeige sie dir.",
        ],
        "pains": [
            "Berater-Rechnungen von 15.000 Euro für Templates, die man selbst ausfüllen kann",
            "Angst, dass eine falsche Cookie-Banner-Formulierung 20.000 Euro kostet",
            "Kein Plan, welche Policies wirklich Pflicht sind",
            "Mitarbeiter-Schulungen, die nie stattfinden",
        ],
        "insights": [
            "Die 6-Wochen-Sprint-Regel: jede Woche ein Policy-Paket, abhakbar, sonst wird es nie fertig",
            "Die 12 Pflicht-Policies sind immer die gleichen — sortiert, dokumentiert, versioniert",
            "Ein DPO ist nur in 3 Fällen Pflicht — die meisten SMBs brauchen keinen",
            "Privacy Policy und Cookie Policy sind zwei Dokumente — immer",
            "HIPAA ist nicht 'Healthcare-only' — jeder, der Health-Daten berührt, ist betroffen",
            "Ein Audit prüft nicht, was du denkst, sondern was dokumentiert ist",
            "Der Compliance-Stack für SMBs kostet unter 500 Euro pro Monat — alles darüber ist Upsell",
        ],
        "ctas": [
            "Die 12-Policy-Checkliste + Bundle ist im ersten Kommentar — audit-fähig, sortiert nach Priorität.",
            "Der 6-Wochen-Sprint-Plan als Notion-Template ist unten. Startklar, morgen.",
        ],
        "tease_pattern": "Nächstes Video: {next_title} — und der Audit, den niemand überlebt hat.",
    },
}


# Handgeschriebene Flagship-Scripts (Video #1 pro Nische) — Gold-Standard.
# Format: {"hook": str, "agitation": str, "solution": str, "insights": [3 str], "cta": str, "tease": str}

FLAGSHIP_SCRIPTS = {
    1: {
        "hook": (
            "Ich habe seit 6 Monaten keinen manuellen Task in meiner SaaS mehr angefasst. "
            "Kein Copy-Paste zwischen Tools. Kein Ticket, das ich von Hand route. "
            "Meine komplette Operations laufen auf 4 Tools und einer Regel — "
            "in diesem Video zeige ich dir die Regel und den Stack, damit du sie morgen nachbaust."
        ),
        "agitation": (
            "Wenn du eine SaaS baust, kennst du die Routine: Jeder neue Kunde triggert "
            "einen Onboarding-Flow, der in 6 Tools gleichzeitig passiert. Support landet im "
            "E-Mail-Postfach, im Slack, in Notion und — aus irgendeinem Grund — manchmal auf Papier. "
            "Dashboards werden gebaut und sind 3 Wochen später veraltet. Rechnungen entstehen "
            "aus Excel-Sheets, die niemand mehr versteht. Das ist kein Ops-Problem — das ist "
            "das Fehlen eines Modells. Und die meisten Founder merken es erst, wenn sie "
            "einen Ops-Hire brauchen, den sie sich nicht leisten können."
        ),
        "solution": (
            "Das Modell heißt 3-Layer: Intake, Automate, Measure. "
            "Layer 1 — Intake: alles landet in Airtable. Anfragen, Kunden, Tickets, Leads. "
            "Airtable ist die Single Source of Truth, und niemand schreibt in ein anderes Tool. "
            "Layer 2 — Automate: Zapier oder Make verbindet Airtable mit den Tools, die "
            "wirklich Action brauchen — Slack, E-Mail, Stripe, Notion. Aber Zapier macht keine "
            "Logik — es macht nur Verbindungen. Wenn du Bedingungen brauchst, gehören sie in "
            "Airtable-Formeln oder in einen N8N-Workflow, nicht in einen Zapier-Zap. "
            "Layer 3 — Measure: ein einziges Dashboard (Notion oder Metabase), das "
            "die 3 KPIs zeigt, die dich wirklich interessieren. Nicht 20 — 3. "
            "Das ist die Regel: keine Aktion ohne Layer, kein Layer ohne Monitor."
        ),
        "insights": [
            "Die 3-Layer-Regel: Intake, Automate, Measure — niemals alle drei im selben Tool. "
            "Airtable macht Intake, Zapier/Make macht Automate, Metabase macht Measure. "
            "Sobald du anfängst, ein Tool zu überladen, brichst du das Modell.",
            "Zapier ist Klebstoff, nicht Gehirn. Wenn du im Zapier-Zap mehr als 2 Conditions "
            "hast, ist die Logik im falschen Tool. Sie gehört in Airtable-Formeln oder in "
            "einen N8N-Workflow — alles andere wird ein Debug-Albtraum.",
            "Der eigentliche Wert ist nicht die Automation — es ist der Monitor darüber. "
            "Ein Zap, der ohne Monitor läuft, ist eine Zeitbombe. Ein Zap mit Monitor ist "
            "ein System. Der Unterschied ist eine 20-Zeilen-Notion-Seite, die du wöchentlich checkst.",
        ],
        "cta": (
            "Lade das Template im ersten Kommentar — der komplette Stack ist drin, du "
            "importierst in 30 Sekunden. Airtable-Base, Zapier-Zaps, Notion-Dashboard. "
            "Du kannst morgen mit Layer 1 starten, ohne irgendetwas zu bauen."
        ),
        "tease": (
            "Im nächsten Video zerlege ich Airtable gegen Notion — und zeige, welches Tool "
            "bei mir in Layer 1 wirklich gewonnen hat. Wenn du SaaS-Ops ernst nimmst, "
            "willst du das sehen."
        ),
    },
}


def render_one(rank: int, video_index: int) -> dict:
    """Gibt ein fertiges Script-Dict zurück für (niche, video#)."""
    from data.roadmap import ROADMAP
    from data.identities import IDENTITIES

    if rank not in NICHE_PROFILES:
        raise ValueError(f"Keine Profil-Daten für Nische {rank}")
    if rank not in ROADMAP:
        raise ValueError(f"Keine Roadmap für Nische {rank}")

    videos = ROADMAP[rank]["videos"]
    if not (1 <= video_index <= len(videos)):
        raise ValueError(f"Video-Index {video_index} außerhalb 1–{len(videos)}")

    title, focus, phase, pillar = videos[video_index - 1]
    profile = NICHE_PROFILES[rank]
    ident = IDENTITIES[rank]

    # Flagship-Override (nur Video 1, nur wenn handgeschrieben vorhanden)
    if video_index == 1 and rank in FLAGSHIP_SCRIPTS:
        f = FLAGSHIP_SCRIPTS[rank]
        return {
            "niche": ident["niche"],
            "title": title,
            "focus": focus,
            "phase": phase,
            "pillar": pillar,
            "tone": profile["tone"],
            "hook": f["hook"],
            "agitation": f["agitation"],
            "solution": f["solution"],
            "insights": f["insights"],
            "cta": f["cta"],
            "tease": f["tease"],
            "source": "flagship",
        }

    # Template-Generierung für alle anderen Videos
    next_title = videos[(video_index % len(videos))][0]

    hook = profile["hooks"][(video_index - 1) % len(profile["hooks"])]
    pains = profile["pains"]
    agitation = (
        f"Konkret geht es um {title.split(':')[0]}. "
        f"Was die meisten übersehen: " + " — ".join(pains[:3]) + ". "
        f"Das ist kein Wissens-Problem, das ist ein System-Problem. "
        f"In dieser Nische, {profile['tone']}, ist der Unterschied zwischen "
        f"denen, die Ergebnisse sehen, und denen, die Videos schauen, immer "
        f"derselbe: ein Modell, keine Taktik."
    )

    insights_pool = profile["insights"]
    start = (video_index - 1) % max(1, len(insights_pool) - 2)
    insights = insights_pool[start:start + 3]
    while len(insights) < 3:
        insights.append(insights_pool[len(insights)])

    solution = (
        f"Der Weg für {title.split(':')[0]}: "
        f"(1) Kontext aufbauen — was ist das Problem, warum jetzt. "
        f"(2) Walkthrough — konkret, Schritt für Schritt, ohne Sprünge. "
        f"(3) Ergebnis zeigen — was am Ende messbar anders ist. "
        f"Pillar: {pillar}. Der Fokus dieses Videos ist {focus} — "
        f"das heißt: wir optimieren hier auf Suchbarkeit und Tiefe, "
        f"nicht auf Reichweite. Das nächste Video wird anders."
    )

    cta = profile["ctas"][(video_index - 1) % len(profile["ctas"])]
    tease = profile["tease_pattern"].format(next_title=next_title)

    return {
        "niche": ident["niche"],
        "title": title,
        "focus": focus,
        "phase": phase,
        "pillar": pillar,
        "tone": profile["tone"],
        "hook": hook,
        "agitation": agitation,
        "solution": solution,
        "insights": insights,
        "cta": cta,
        "tease": tease,
        "source": "template",
    }

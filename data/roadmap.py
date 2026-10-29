"""90-Tage Content-Roadmap pro Nische — 12 Titel, Schedule, Progression."""

# video = (title, focus, phase, pillar)
#   focus: "seo" | "viral"
#   phase: 1 = Tage 1–30 (Search Foundation)
#          2 = Tage 31–60 (Authority Build)
#          3 = Tage 61–90 (Virality / Scale)

ROADMAP = {
    1: {
        "niche": "B2B SaaS Tutorials & Workflow Automation",
        "schedule": "2×/Woche — Di + Fr, 18:00 UTC",
        "progression": (
            "Phase 1 (T1–30): Search-Foundation — 8 SEO-Videos, 0 Viral. "
            "Phase 2 (T31–60): Authority — 4 SEO + 4 Viral, Stack-Teardowns. "
            "Phase 3 (T61–90): Virality — 2 SEO + 6 Viral, Case-Studies."
        ),
        "videos": [
            ("How I Automated 90% of My SaaS Ops with Notion + Zapier", "seo", 1, "Ops"),
            ("Airtable vs Notion 2026: Which Wins for SaaS?", "seo", 1, "Stack"),
            ("The 3-Layer Automation Model Every SaaS Needs", "seo", 1, "Ops"),
            ("Zapier vs Make: Which Actually Scales?", "seo", 1, "Stack"),
            ("I Automated My Whole Onboarding in 45 Minutes", "viral", 2, "Recipes"),
            ("Why I Deleted Half My SaaS Stack", "viral", 2, "Stack"),
            ("Building a $0 Ops Team With 4 Tools", "viral", 2, "Case"),
            ("Notion as a CRM — I Tested 30 Days", "seo", 2, "Ops"),
            ("The Automation That Saved a Client $80K/Year", "viral", 3, "Case"),
            ("Every SaaS Founder Overpays for This Tool", "viral", 3, "Stack"),
            ("Full Ops Stack Teardown (7-Figure SaaS)", "seo", 3, "Stack"),
            ("I Copied a $50M SaaS's Ops — Here's the Sheet", "viral", 3, "Case"),
        ],
    },
    2: {
        "niche": "Small Claims Court & Consumer Legal Self-Defense",
        "schedule": "2×/Woche — Mo + Do, 17:00 UTC",
        "progression": (
            "Phase 1 (T1–30): Filing-Foundation — Filing-Walkthroughs für 3 Staaten, "
            "0 Viral. Phase 2 (T31–60): Evidence + Courtroom. "
            "Phase 3 (T61–90): Collection + Case Stories."
        ),
        "videos": [
            ("How to File a Small Claims Case (California, 2026)", "seo", 1, "Filing"),
            ("Small Claims Filing — Texas Walkthrough", "seo", 1, "Filing"),
            ("New York Small Claims: Everything You Need", "seo", 1, "Filing"),
            ("What Evidence Actually Wins in Small Claims", "seo", 1, "Evidence"),
            ("I Took My Landlord to Court — Full Story", "viral", 2, "Tactics"),
            ("The 5-Piece Case File System (Free Template)", "seo", 2, "Evidence"),
            ("What Judges Hate in Small Claims", "viral", 2, "Tactics"),
            ("Cross-Examining Your Opponent (Without a Lawyer)", "seo", 2, "Tactics"),
            ("He Won $4,200 — Here's How He Collected", "viral", 3, "Collection"),
            ("The Judgment Was Easy. Collection Wasn't.", "viral", 3, "Collection"),
            ("How to Serve Someone Who Avoids You", "seo", 3, "Filing"),
            ("I Sued a Contractor — The Whole Timeline", "viral", 3, "Tactics"),
        ],
    },
    3: {
        "niche": "Medical Coding & Billing Careers",
        "schedule": "2×/Woche — Mi + Sa, 16:00 UTC",
        "progression": (
            "Phase 1 (T1–30): Cert-Foundation — CPC-Roadmap + Exam Basics. "
            "Phase 2 (T31–60): Exam Drills + Job-Hunt. "
            "Phase 3 (T61–90): Real Career Stories + Salary."
        ),
        "videos": [
            ("CPC Certification in 90 Days — Full Roadmap", "seo", 1, "Roadmap"),
            ("CPC vs CCS: Which Cert Gets You Hired?", "seo", 1, "Roadmap"),
            ("ICD-10 Basics Every Beginner Needs", "seo", 1, "Exam"),
            ("Medical Coding Salary in 2026 (Real Numbers)", "seo", 1, "Career"),
            ("I Passed CPC on the First Try — Here's How", "viral", 2, "Exam"),
            ("Coding Exam Practice — 10 Real Questions", "seo", 2, "Exam"),
            ("Resume That Got Me a Remote Coding Job", "viral", 2, "Career"),
            ("Day in the Life of a Medical Coder", "viral", 2, "Career"),
            ("From Waitress to $58K Coder in 8 Months", "viral", 3, "Career"),
            ("Everything They Don't Tell You About Coding School", "viral", 3, "Roadmap"),
            ("CPT vs ICD-10: What Beginners Confuse", "seo", 3, "Exam"),
            ("How I Beat Imposter Syndrome as a Coder", "viral", 3, "Career"),
        ],
    },
    4: {
        "niche": "Home Inspection & Property Due Diligence",
        "schedule": "2×/Woche — Di + Sa, 15:00 UTC",
        "progression": (
            "Phase 1 (T1–30): Red-Flag-Foundation — Top-Findings. "
            "Phase 2 (T31–60): Walkthrough-Audits + Tool-Tests. "
            "Phase 3 (T61–90): Deal-Breaker-Stories + Inspector-Path."
        ),
        "videos": [
            ("10 Red Flags Every First-Time Buyer Misses", "seo", 1, "RedFlag"),
            ("What a Home Inspector Actually Looks For", "seo", 1, "Walkthrough"),
            ("Foundation Cracks: Real vs Cosmetic", "seo", 1, "RedFlag"),
            ("Moisture Meters: What Buyers Should Own", "seo", 1, "Tool"),
            ("$40K Foundation Problem We Caught in 10 Min", "viral", 2, "Walkthrough"),
            ("I Inspected a $1M Listing — Here's What I Found", "viral", 2, "Walkthrough"),
            ("Thermal Cameras for Buyers — Worth It?", "seo", 2, "Tool"),
            ("The Checklist That Saved a Client $60K", "seo", 2, "Walkthrough"),
            ("The Inspection That Killed the Deal", "viral", 3, "RedFlag"),
            ("Every Roof Issue Explained in 12 Minutes", "seo", 3, "RedFlag"),
            ("How Much Home Inspectors Actually Earn", "viral", 3, "Career"),
            ("Realtors Hated Me for This Video", "viral", 3, "Walkthrough"),
        ],
    },
    5: {
        "niche": "Industrial Engineering & Manufacturing Explained",
        "schedule": "2×/Woche — Mo + Fr, 17:00 UTC",
        "progression": (
            "Phase 1 (T1–30): Process-Foundation — eine Fertigungsart pro Video. "
            "Phase 2 (T31–60): Machine Teardowns + Plant Tours. "
            "Phase 3 (T61–90): Failures + Engineering Stories."
        ),
        "videos": [
            ("How Injection Molding Actually Works", "seo", 1, "Process"),
            ("How CNC Machining Turns Metal Into Parts", "seo", 1, "Process"),
            ("How Aluminum Cans Are Made (Full Process)", "seo", 1, "Process"),
            ("How PCBs Are Manufactured — Step by Step", "seo", 1, "Process"),
            ("Inside a Real Auto Plant (Plant Tour)", "viral", 2, "Plant"),
            ("The Machine That Makes Microchips", "viral", 2, "Machine"),
            ("How Steel Beams Are Made From Scratch", "seo", 2, "Process"),
            ("Why This $2M Machine Exists", "viral", 2, "Machine"),
            ("The Engineering Failure That Killed 100 People", "viral", 3, "Failure"),
            ("How Tesla's Gigapress Actually Works", "seo", 3, "Machine"),
            ("Every Manufacturing Process in 20 Minutes", "seo", 3, "Process"),
            ("3 Factories That Shouldn't Exist", "viral", 3, "Failure"),
        ],
    },
    6: {
        "niche": "Accounting & Bookkeeping for Small Business",
        "schedule": "2×/Woche — Di + Fr, 16:00 UTC",
        "progression": (
            "Phase 1 (T1–30): Software-Foundation — QBO vs Xero Basics. "
            "Phase 2 (T31–60): Month-End Close + Tax-Ready. "
            "Phase 3 (T61–90): DIY vs Hire + Owner Stories."
        ),
        "videos": [
            ("QuickBooks Online vs Xero 2026: Honest Test", "seo", 1, "Software"),
            ("How to Set Up QBO in 30 Minutes (2026)", "seo", 1, "Software"),
            ("Chart of Accounts: The Beginner Version", "seo", 1, "Close"),
            ("Bookkeeping Basics Every Owner Skips", "seo", 1, "Close"),
            ("My 15-Minute Month-End Close Routine", "viral", 2, "Close"),
            ("I Cleaned Up a $2M Business's Books", "viral", 2, "Close"),
            ("Tax-Ready Books in 4 Weeks — The System", "seo", 2, "Close"),
            ("Do You Actually Need a Bookkeeper?", "viral", 2, "Hire"),
            ("The Books That Almost Cost This Owner $80K", "viral", 3, "Hire"),
            ("Every Small Biz Bookkeeping Mistake (Ranked)", "viral", 3, "Close"),
            ("Bookkeeper vs DIY — Real Cost Breakdown", "seo", 3, "Hire"),
            ("I Fixed a 3-Year-Old QuickBooks Disaster", "viral", 3, "Close"),
        ],
    },
    7: {
        "niche": "Insurance Deep Dives (Life / Disability / Umbrella)",
        "schedule": "2×/Woche — Mo + Do, 16:00 UTC",
        "progression": (
            "Phase 1 (T1–30): Policy-Basics — Term vs Whole, Disability. "
            "Phase 2 (T31–60): Claim-Szenarien + Fine-Print-Audits. "
            "Phase 3 (T61–90): Rate-Shop-Playbooks + Real Stories."
        ),
        "videos": [
            ("Term vs Whole Life: The Honest Math", "seo", 1, "Policy"),
            ("How Much Life Insurance Do You Actually Need?", "seo", 1, "Policy"),
            ("Disability Insurance: The One Nobody Buys", "seo", 1, "Policy"),
            ("Umbrella Insurance Explained in 5 Minutes", "seo", 1, "Policy"),
            ("The Fine Print That Denied a $500K Claim", "viral", 2, "FinePrint"),
            ("I Read 6 Life Policies — Here's What's Hidden", "viral", 2, "FinePrint"),
            ("Claim Scenarios: When Insurance Actually Pays", "seo", 2, "Claim"),
            ("Why Your Agent Sells You Whole Life", "viral", 2, "Policy"),
            ("The 3-Quote Rule for Every Policy", "seo", 3, "Shop"),
            ("Widow's Story: The Policy That Saved Her", "viral", 3, "Claim"),
            ("Disability Claim Approved — Full Timeline", "seo", 3, "Claim"),
            ("I Compared 10 Policies So You Don't Have To", "viral", 3, "Shop"),
        ],
    },
    8: {
        "niche": "Wealth Management for Expats & Cross-Border",
        "schedule": "2×/Woche — Di + Sa, 17:00 UTC",
        "progression": (
            "Phase 1 (T1–30): Country-Foundation — Tax-Basics für 3 Länder. "
            "Phase 2 (T31–60): Broker-Setups + Currency. "
            "Phase 3 (T61–90): Retirement + Portfolio-Stories."
        ),
        "videos": [
            ("US Expat Taxes in 2026 — Complete Guide", "seo", 1, "Country"),
            ("Portugal vs Spain: Expat Tax Compared", "seo", 1, "Country"),
            ("Interactive Brokers for Expats — Setup", "seo", 1, "Broker"),
            ("Wise vs Revolut for Expats (2026)", "seo", 1, "Currency"),
            ("I Moved to Portugal — Real Money Story", "viral", 2, "Country"),
            ("The 3-Account Rule Every Expat Needs", "seo", 2, "Broker"),
            ("Currency Hedging for Normal People", "seo", 2, "Currency"),
            ("The Tax Mistake That Cost Me $12K", "viral", 2, "Country"),
            ("Retiring Abroad: The Real Math", "viral", 3, "Retire"),
            ("My Expat Portfolio — Full Breakdown", "viral", 3, "Retire"),
            ("Best Countries for US Expats (Ranked)", "seo", 3, "Country"),
            ("I Interviewed 5 Expats About Money", "viral", 3, "Retire"),
        ],
    },
    9: {
        "niche": "Cybersecurity Careers & Certifications",
        "schedule": "2×/Woche — Mo + Do, 18:00 UTC",
        "progression": (
            "Phase 1 (T1–30): Cert-Roadmaps — Sec+, CySA+, OSCP. "
            "Phase 2 (T31–60): Labs + Job-Market. "
            "Phase 3 (T61–90): Interview + Real Career Stories."
        ),
        "videos": [
            ("Security+ in 60 Days — Full Roadmap", "seo", 1, "Cert"),
            ("Sec+ vs CySA+: Which First?", "seo", 1, "Cert"),
            ("OSCP Reality Check (2026)", "seo", 1, "Cert"),
            ("SOC Analyst Salary in 2026", "seo", 1, "Career"),
            ("I Passed Sec+ in 42 Days — Here's How", "viral", 2, "Cert"),
            ("TryHackMe vs HackTheBox for Beginners", "seo", 2, "Lab"),
            ("My First SOC Job — Real Day", "viral", 2, "Career"),
            ("Home Lab Setup Under $300", "seo", 2, "Lab"),
            ("Helpdesk to $80K SOC Analyst in 9 Months", "viral", 3, "Career"),
            ("Interview Questions That Broke Me", "viral", 3, "Career"),
            ("Every Cert Ranked by ROI", "viral", 3, "Cert"),
            ("I Applied to 100 Cyber Jobs — Results", "viral", 3, "Career"),
        ],
    },
    10: {
        "niche": "Compliance, GDPR & HIPAA for SMBs",
        "schedule": "2×/Woche — Di + Fr, 16:00 UTC",
        "progression": (
            "Phase 1 (T1–30): GDPR/HIPAA Basics. "
            "Phase 2 (T31–60): Policies + Templates. "
            "Phase 3 (T61–90): Audit-Stories + Sprint-Playbook."
        ),
        "videos": [
            ("GDPR for Small Business — 2026 Basics", "seo", 1, "GDPR"),
            ("HIPAA for Non-Healthcare Founders", "seo", 1, "HIPAA"),
            ("Do You Need a DPO? (Honest Answer)", "seo", 1, "GDPR"),
            ("Privacy Policy vs Cookie Policy Explained", "seo", 1, "GDPR"),
            ("The GDPR Fine That Killed an SMB", "viral", 2, "Audit"),
            ("My 6-Week Compliance Sprint (Templates)", "seo", 2, "Policy"),
            ("What an Auditor Actually Checks", "viral", 2, "Audit"),
            ("HIPAA Policy Bundle — Full Walkthrough", "seo", 2, "Policy"),
            ("We Almost Failed Our First Audit", "viral", 3, "Audit"),
            ("Every GDPR Fine in 2025, Ranked", "viral", 3, "Audit"),
            ("SMB Compliance Stack — Under $500/mo", "seo", 3, "Policy"),
            ("6 Weeks From Audit Alert to Compliant", "viral", 3, "Audit"),
        ],
    },
}

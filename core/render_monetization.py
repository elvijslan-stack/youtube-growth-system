from data.monetization import MONETIZATION, TIERS, tier_for_subs
from data.identities import IDENTITIES


def _fmt_pitch(niche: str, subs: int, tier_key: str, m: dict) -> str:
    sp = m["sponsorships"]
    brands = ", ".join(sp["target_brands"][:4])
    return (
        f"**Betreff:** {niche} — {subs:,} Abonnenten · Q-Sponsorship\n"
        f"\n"
        f"Hi [Name],\n"
        f"\n"
        f"ich betreibe einen YouTube-Kanal zu {niche} mit aktuell "
        f"{subs:,} Abonnenten und einer durchschnittlichen Watch-Time von "
        f"[X Min]. Mein Publikum: [X%] US/EU, [X%] Entscheider — konkret "
        f"die Personen, die {sp['target_brands'][0]} kaufen.\n"
        f"\n"
        f"Warum eine Kooperation passt:\n"
        f"- **Publikums-Fit:** {sp['pitch_angle']}\n"
        f"- **Reichweite:** [X Views/Monat], [X%] Traffic aus Suche (evergreen)\n"
        f"- **Format:** 60–90 Sek Integration + Pinned Comment + Link in Beschreibung\n"
        f"- **Bisherige Sponsors:** {brands}\n"
        f"\n"
        f"Vorschlag: [Rate] € pro Video-Integration, [Rate×2] € für 2-Video-Paket.\n"
        f"\n"
        f"Ich schicke gern Media-Kit mit Analytics-Screenshots.\n"
        f"\n"
        f"Beste Grüße,\n"
        f"[Dein Name] — [Kanal-Link]"
    )


def _fmt_one(rank: int, subs: int) -> str:
    m = MONETIZATION[rank]
    tier_key = tier_for_subs(subs)
    tier_label = next(t["label"] for t in TIERS if t["key"] == tier_key)
    tier_data = m["tiers"][tier_key]
    ident = IDENTITIES[rank]

    lines = [
        f"## {rank}. {m['niche']}",
        "",
        f"**Aktuell:** {subs:,} Abonnenten → **Tier:** {tier_key} ({tier_label})",
        "",
        f"**Revenue-Erwartung:** {tier_data['monthly_range']} / Monat",
        f"**Fokus in diesem Tier:** {tier_data['focus']}",
        "",
        "**Hebel in diesem Tier:**",
    ]
    for p in tier_data["plays"]:
        lines.append(f"- {p}")
    lines.append("")

    lines.append("### 🧲 Lead-Magnet")
    lm = m["lead_magnet"]
    lines.append(f"- **Name:** {lm['name']}")
    lines.append(f"- **Format:** {lm['format']}")
    lines.append(f"- **Value-Promise:** {lm['value_promise']}")
    lines.append(f"- **Email-Hook (copy-paste):** _{lm['email_hook']}_")
    lines.append("")

    lines.append("### 💰 Affiliate-Programme")
    lines.append("")
    lines.append("| Tool | Typ | RPM / Payout | Hinweis |")
    lines.append("|------|-----|--------------|---------|")
    for a in m["affiliate"]:
        lines.append(f"| {a['tool']} | {a['type']} | {a['rpm_range']} | `{a['link_hint']}` |")
    lines.append("")

    lines.append("### 📦 Digitale Produkte (launch-at)")
    lines.append("")
    lines.append("| Produkt | Format | Preis | Launch ab |")
    lines.append("|---------|--------|-------|-----------|")
    for p in m["products"]:
        lines.append(f"| {p['name']} | {p['format']} | {p['price']} | {p['launch_at']} |")
    lines.append("")

    lines.append("### 🤝 Sponsorship")
    lines.append(f"- **Rate (per 1K Views):** {m['sponsorships']['rate_per_1k_views']}")
    lines.append(f"- **Ziel-Brands:** {', '.join(m['sponsorships']['target_brands'])}")
    lines.append(f"- **Pitch-Angle:** {m['sponsorships']['pitch_angle']}")
    lines.append("")
    lines.append("**Pitch-Template (ready to paste):**")
    lines.append("")
    lines.append("````text")
    lines.append(_fmt_pitch(m["niche"], subs, tier_key, m))
    lines.append("````")
    lines.append("")

    lines.append("### 📊 Tier-Übersicht")
    lines.append("")
    lines.append("| Tier | Subscriber | Revenue/Monat | Fokus |")
    lines.append("|------|-----------|---------------|-------|")
    for t in TIERS:
        td = m["tiers"][t["key"]]
        marker = " ← **du bist hier**" if t["key"] == tier_key else ""
        lines.append(f"| {t['key']} | {t['label']} | {td['monthly_range']} | {td['focus']}{marker} |")
    lines.append("")

    lines.append(f"### ⚠️ Reality-Check")
    lines.append(f"{m['revenue_model_note']}")
    lines.append("")

    lines.append(f"**Nischen-Kontext:** {ident['niche']} · "
                 f"Unique Mechanism: _{ident['unique_mechanism']}_")
    lines.append("")
    return "\n".join(lines)


def render_monetization(rank: int, subs: int = 1_000) -> str:
    header = (
        f"# Monetization Stack — Nische {rank}\n\n"
        f"**Subscriber-Stand:** {subs:,}  \n"
        f"**Nische:** {IDENTITIES[rank]['niche']}\n\n"
    )
    return header + _fmt_one(rank, subs) + "\n"


def render_monetization_all(subs: int = 1_000) -> str:
    parts = [
        f"# Monetization Stack — Alle Nischen ({subs:,} Abonnenten)\n",
    ]
    for rank in sorted(MONETIZATION):
        parts.append(_fmt_one(rank, subs))
        parts.append("\n---\n")
    return "\n".join(parts)

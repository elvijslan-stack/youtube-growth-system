from data.niches import NICHES


def render_table() -> str:
    lines = [
        "| # | Nische | CPM (USD) | Difficulty | Kanal-Konzept |",
        "|---|--------|-----------|-----------|----------------|",
    ]
    for n in NICHES:
        cpm = f"${n['cpm_low']:.0f}–${n['cpm_high']:.0f}"
        lines.append(
            f"| {n['rank']} | {n['name']} | {cpm} | "
            f"{n['difficulty']}/5 | {n['concept']} |"
        )
    return "\n".join(lines)


def render_detail(n: dict) -> str:
    mono = "\n".join(f"   - {m}" for m in n["monetization"])
    return (
        f"### {n['rank']}. {n['name']}\n"
        f"- **CPM:** ${n['cpm_low']:.0f}–${n['cpm_high']:.0f} (US-Audience, 2025/26)\n"
        f"- **Difficulty:** {n['difficulty']}/5 — {n['difficulty_note']}\n"
        f"- **Monetarisierung (jenseits AdSense):**\n{mono}\n"
        f"- **Kanal-Konzept:** _{n['concept']}_"
    )


def render_full() -> str:
    parts = ["# Top 10 YouTube-Nischen — High CPM · Low Competition · Evergreen", ""]
    parts.append(render_table())
    parts.append("")
    parts.append("---")
    parts.append("")
    for n in NICHES:
        parts.append(render_detail(n))
        parts.append("")
    return "\n".join(parts)

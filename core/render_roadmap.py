from __future__ import annotations

from data.roadmap import ROADMAP

PHASE_LABEL = {
    1: "Phase 1 — Search Foundation (Tage 1–30)",
    2: "Phase 2 — Authority Build (Tage 31–60)",
    3: "Phase 3 — Virality / Scale (Tage 61–90)",
}


def render_one(rank: int) -> str:
    d = ROADMAP[rank]
    lines = [
        f"## {rank}. {d['niche']}",
        "",
        f"**Upload-Schedule:** {d['schedule']}",
        "",
        f"**Progression:** {d['progression']}",
        "",
        "**12 Videos**",
        "",
        "| # | Titel | Focus | Phase | Pillar |",
        "|---|-------|-------|-------|--------|",
    ]
    for i, (title, focus, phase, pillar) in enumerate(d["videos"], 1):
        badge = "🔍 SEO" if focus == "seo" else "🚀 Viral"
        lines.append(f"| {i} | {title} | {badge} | {phase} | {pillar} |")

    lines.append("")
    for phase in (1, 2, 3):
        vids = [v for v in d["videos"] if v[2] == phase]
        lines.append(f"**{PHASE_LABEL[phase]}** — {len(vids)} Videos")
        for i, (title, focus, _, pillar) in enumerate(vids, 1):
            lines.append(f"   {i}. {title}  _({focus} · {pillar})_")
        lines.append("")
    return "\n".join(lines)


def render_roadmap(rank: int | None = None) -> str:
    if rank is not None:
        if rank not in ROADMAP:
            raise ValueError(f"Keine Roadmap für Rank {rank}")
        return f"# 90-Tage Content-Roadmap — Nische {rank}\n\n{render_one(rank)}\n"

    parts = ["# 90-Tage Content-Roadmaps — Top 10 Nischen", ""]
    for r in sorted(ROADMAP):
        parts.append(render_one(r))
        parts.append("\n---\n")
    return "\n".join(parts)

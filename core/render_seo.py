from data.seo import NICHE_SEO, SEO_OVERRIDES, shorten_title
from data.roadmap import ROADMAP
from data.identities import IDENTITIES


def _build_seo_title(base_title: str, rank: int, video_index: int) -> str:
    override = SEO_OVERRIDES.get((rank, video_index), {})
    if override.get("seo_title"):
        return override["seo_title"]
    return shorten_title(base_title)


def _select_tags(rank: int, video_index: int, pillar: str) -> list[str]:
    override = SEO_OVERRIDES.get((rank, video_index), {})
    if override.get("tags"):
        return override["tags"][:10]

    pool = NICHE_SEO[rank]["tags_pool"]
    pillar_tags = [t for t in pool if pillar.lower() in t.lower()][:2]
    head = pool[:3]
    rest = [t for t in pool if t not in head and t not in pillar_tags]
    start = ((video_index - 1) * 3) % max(1, len(rest))
    rotated = [rest[(start + i) % len(rest)] for i in range(len(rest))]
    merged: list[str] = []
    seen: set[str] = set()
    for t in head + pillar_tags + rotated:
        if t not in seen:
            seen.add(t)
            merged.append(t)
        if len(merged) >= 10:
            break
    return merged


def _rotate_concepts(concepts: list[dict], video_index: int) -> list[dict]:
    start = (video_index - 1) % len(concepts)
    return [concepts[(start + i) % len(concepts)] for i in range(len(concepts))]


def _build_description(
    rank: int, title: str, tags: list[str], video_index: int
) -> str:
    n = NICHE_SEO[rank]
    labels = n["section_labels"]
    hashtags = " ".join(n["hashtags"][:3])
    keywords = ", ".join(tags[:6])
    next_video = ROADMAP[rank]["videos"][video_index % len(ROADMAP[rank]["videos"])][0]
    return (
        f"{n['description_intro']}\n\n"
        f"Was dich erwartet:\n"
        f"• {labels['hook']}\n"
        f"• {labels['solution']}\n"
        f"• {labels['insights']}\n\n"
        f"⏱️ TIMESTAMPS\n"
        f"0:00 {labels['hook']}\n"
        f"0:30 {labels['agitation']}\n"
        f"1:30 {labels['solution']}\n"
        f"4:00 {labels['insights']}\n"
        f"6:00 {labels['cta']}\n"
        f"6:30 {labels['tease']}\n\n"
        f"🔗 LINKS & RESSOURCEN\n"
        f"→ Kostenloses Template: [LINK in Kommentar / Beschreibung einfügen]\n"
        f"→ Bundle / Playlist: [LINK einfügen]\n"
        f"→ Mehr Videos: [KANAL-LINK]\n\n"
        f"📌 KEYWORDS\n"
        f"{keywords}\n\n"
        f"🔔 Abonniere für wöchentliche {IDENTITIES[rank]['niche']}-Tiefen.\n\n"
        f"Nächstes Video: {next_video}\n\n"
        f"{hashtags}"
    )


def _fmt_video(rank: int, video_index: int) -> str:
    n = NICHE_SEO[rank]
    title, focus, phase, pillar = ROADMAP[rank]["videos"][video_index - 1]
    seo_title = _build_seo_title(title, rank, video_index)
    title_len = len(seo_title)
    title_ok = "✓" if title_len <= 60 else "⚠️ >60"
    tags = _select_tags(rank, video_index, pillar)
    concepts = _rotate_concepts(n["thumb_concepts"], video_index)
    description = _build_description(rank, title, tags, video_index)

    lines = [
        f"## {rank}.{video_index} — {title}",
        "",
        f"**Focus:** {focus} · **Phase:** {phase} · **Pillar:** {pillar}",
        "",
        "### 🎬 SEO-Titel (Ziel: <60 Zeichen)",
        f"**Final:** `{seo_title}`",
        f"**Länge:** {title_len} Zeichen {title_ok}",
        "",
        "**A/B-Test-Varianten:**",
        f"1. `{seo_title}` (Original)",
        f"2. `{shorten_title(title, 45)}` (Kurzform)",
        f"3. `{shorten_title(title, 55)} (2026)` (Jahr-Variante)",
        "",
        "### 🖼️ 3 Thumbnail-Konzepte",
        "",
    ]
    for i, c in enumerate(concepts, 1):
        lines.append(f"**Concept {i} — \"{c['overlay']}\"**")
        lines.append(f"- **Visual:** {c['visual']}")
        lines.append(f"- **Overlay:** \"{c['overlay']}\"")
        lines.append(f"- **A/B-Test:** {c['ab']}")
        lines.append("")

    lines.append("### 🧪 Thumbnail-A/B-Matrix (globale Variablen)")
    for i, v in enumerate(n["ab_matrix"], 1):
        lines.append(f"{i}. {v}")
    lines.append("")
    lines.append("**Stil-Regeln:**")
    lines.append(f"- **Palette:** {n['palette']}")
    lines.append(f"- **Face-Rule:** {n['face_rule']}")
    lines.append(f"- **Text-Stil:** {n['text_style']}")
    lines.append("")
    lines.append("### 📝 YouTube-Beschreibung (ready to paste)")
    lines.append("")
    lines.append("````text")
    lines.append(description)
    lines.append("````")
    lines.append("")
    lines.append("### 🏷️ Tags (10)")
    lines.append(", ".join(tags))
    lines.append("")
    return "\n".join(lines)


def render_seo(rank: int, video_index: int = 1) -> str:
    header = (
        f"# SEO & Thumbnail Strategy — Nische {rank}, Video {video_index}\n\n"
        f"**Nische:** {IDENTITIES[rank]['niche']}\n\n"
    )
    return header + _fmt_video(rank, video_index) + "\n"


def render_seo_all(rank: int) -> str:
    n_videos = len(ROADMAP[rank]["videos"])
    parts = [
        f"# SEO & Thumbnail Strategy — Alle Videos, Nische {rank}\n",
        f"**Nische:** {IDENTITIES[rank]['niche']}\n",
    ]
    for i in range(1, n_videos + 1):
        parts.append(_fmt_video(rank, i))
        parts.append("\n---\n")
    return "\n".join(parts)

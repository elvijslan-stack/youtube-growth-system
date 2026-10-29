import re
from data.repurpose import REPURPOSE
from data.scripts import render_one


def _first_sentences(text: str, max_len: int = 240) -> str:
    text = text.strip()
    if len(text) <= max_len:
        return text
    sentences = re.split(r"(?<=[.!?])\s+", text)
    out = ""
    for s in sentences:
        if len(out) + len(s) + 1 > max_len:
            break
        out = (out + " " + s).strip()
    return out or text[:max_len].rsplit(" ", 1)[0] + "…"


def _render_twitter(script: dict, config: dict) -> str:
    hook = _first_sentences(script["hook"], 260)
    insights = [_first_sentences(i, 260) for i in script["insights"]]
    cta = _first_sentences(script["cta"], 200)
    return (
        "**1/** " + hook + "\n\n"
        "**2/** " + insights[0] + "\n\n"
        "**3/** " + insights[1] + "\n\n"
        "**4/** " + insights[2] + "\n\n"
        "**5/** " + cta + " → [Link in Bio / Pinned Tweet]"
    )


def _render_linkedin(script: dict, config: dict) -> str:
    insights = script["insights"]
    numbered = "\n\n".join(
        f"{i}. {ins.strip()}" for i, ins in enumerate(insights, 1)
    )
    return (
        config["linkedin_opener"] + "\n\n"
        "Hier ist, was die meisten übersehen:\n\n"
        + _first_sentences(script["agitation"], 420) + "\n\n"
        "Meine 3 Prinzipien:\n\n"
        + numbered + "\n\n"
        + _first_sentences(script["cta"], 300) + "\n\n"
        "♻️ Wenn das für dich relevant ist, teil den Post — "
        "irgendwo sitzt jemand mit demselben Problem."
    )


def _render_shorts(config: dict) -> str:
    lines = []
    for i, (hook, angle) in enumerate(config["shorts_hooks"], 1):
        lines.append(f"**Hook {i}:** \"{hook}\"")
        lines.append(f"   - Winkel: {angle}")
        lines.append(f"   - Länge: 30–60 Sekunden · vertical 9:16 · CTA in letzten 5s")
        lines.append("")
    return "\n".join(lines)


def _render_email(script: dict, config: dict, rank: int, video_index: int) -> str:
    subject = config["email_subjects"][(video_index - 1) % len(config["email_subjects"])]
    preview = _first_sentences(script["hook"], 90)
    insights = "\n".join(f"→ {_first_sentences(i, 320)}" for i in script["insights"])
    return (
        f"**Subject:** {subject}\n"
        f"**Preview-Text:** {preview}\n\n"
        "---\n\n"
        "Hey,\n\n"
        + _first_sentences(script["hook"], 340) + "\n\n"
        "Im Video zeige ich das komplette System — aber hier in Kürze, "
        "die 3 Dinge, die wirklich zählen:\n\n"
        + insights + "\n\n"
        + _first_sentences(script["cta"], 260) + "\n\n"
        "Bis nächste Woche,\n"
        "[Dein Name]\n\n"
        "---\n"
        "P.S. Das komplette Video (7 Minuten) → [Link]"
    )


def _render_pinterest(config: dict) -> str:
    p = config["pinterest"]
    desc = p["description"]
    return (
        f"**Board:** {p['board']}\n\n"
        f"**Description ({len(desc)} Zeichen — Pinterest-Limit 500):**\n\n"
        f"{desc}\n\n"
        "**Pin-Format:** 1000×1500 px (2:3), Text-Overlay 4 Wörter max, "
        "Marken-Farbe im Hintergrund."
    )


def _render_priority(config: dict) -> str:
    lines = [
        "| Rang | Plattform | Begründung |",
        "|------|-----------|------------|",
    ]
    for i, (name, rationale) in enumerate(config["platforms"], 1):
        lines.append(f"| {i} | **{name}** | {rationale} |")
    return "\n".join(lines)


def render_repurpose(rank: int, video_index: int = 1) -> str:
    if rank not in REPURPOSE:
        raise ValueError(f"Keine Repurpose-Config für Nische {rank}")
    config = REPURPOSE[rank]
    script = render_one(rank, video_index)

    parts = [
        f"# Growth & Repurposing Pack — Nische {rank}, Video {video_index}",
        "",
        f"**Original-Video:** {script['title']}",
        f"**Nische:** {script['niche']}",
        f"**Focus:** {script['focus']} · **Pillar:** {script['pillar']}",
        "",
        "---",
        "",
        "## 🎯 Platform-Priority (was zuerst, was zuletzt)",
        "",
        _render_priority(config),
        "",
        "---",
        "",
        "## 🐦 Twitter / X Thread (5 Tweets)",
        "",
        _render_twitter(script, config),
        "",
        "---",
        "",
        "## 💼 LinkedIn Post",
        "",
        _render_linkedin(script, config),
        "",
        "---",
        "",
        "## 📱 3 YouTube Shorts Hooks",
        "",
        _render_shorts(config),
        "---",
        "",
        "## 📧 Email Newsletter",
        "",
        _render_email(script, config, rank, video_index),
        "",
        "---",
        "",
        "## 📌 Pinterest",
        "",
        _render_pinterest(config),
        "",
        "---",
        "",
        "## ✅ Reihenfolge (Posting-Schedule)",
        "",
        "1. **Tag 0:** YouTube-Video live (Kernformat, Kernplattform)",
        "2. **Tag 0:** LinkedIn-Post (B2B-Publikum abholen)",
        "3. **Tag 1:** Twitter-Thread (Thread-Timing 14–16 Uhr UTC)",
        "4. **Tag 2:** Email an Liste (Preview-Text = Hook)",
        "5. **Tag 3:** 3 Shorts nacheinander (je 24h Abstand)",
        "6. **Tag 5–7:** Pinterest-Pin(s) — Evergreen, kein Zeitdruck",
    ]
    return "\n".join(parts) + "\n"

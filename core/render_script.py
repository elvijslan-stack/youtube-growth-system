from data.scripts import render_one


def _fmt_script(rank: int, video_index: int) -> str:
    s = render_one(rank, video_index)
    insights_md = "\n\n".join(
        f"### Insight {i}\n{i_text.strip()}" for i, i_text in enumerate(s["insights"], 1)
    )
    return (
        f"## {rank}.{video_index} — {s['title']}\n\n"
        f"**Nische:** {s['niche']}  \n"
        f"**Focus:** {s['focus']} · **Phase:** {s['phase']} · "
        f"**Pillar:** {s['pillar']}  \n"
        f"**Tonalität:** {s['tone']}  \n"
        f"**Script-Quelle:** {s['source']}\n\n"
        f"---\n\n"
        f"### 🎯 HOOK (0:00–0:30)\n{s['hook'].strip()}\n\n"
        f"### 🔥 PROBLEM AGITATION (0:30–1:30)\n{s['agitation'].strip()}\n\n"
        f"### 🛠️ SOLUTION WALKTHROUGH (1:30–4:00)\n{s['solution'].strip()}\n\n"
        f"### 💡 3 KEY INSIGHTS (4:00–6:00)\n\n{insights_md}\n\n"
        f"### 📣 CTA (6:00–6:30)\n{s['cta'].strip()}\n\n"
        f"### 👉 END SCREEN TEASE (6:30–7:00)\n{s['tease'].strip()}\n"
    )


def render_script(rank: int, video_index: int = 1) -> str:
    header = f"# Video-Script — Nische {rank}, Video {video_index}\n\n"
    return header + _fmt_script(rank, video_index)


def render_script_all_videos(rank: int) -> str:
    from data.roadmap import ROADMAP
    n_videos = len(ROADMAP[rank]["videos"])
    parts = [f"# Alle Video-Scripts — Nische {rank}\n"]
    for i in range(1, n_videos + 1):
        parts.append(_fmt_script(rank, i))
        parts.append("\n---\n")
    return "\n".join(parts)

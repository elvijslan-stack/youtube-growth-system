from __future__ import annotations

import argparse
import sys
from pathlib import Path

from core.render import render_full
from core.render_identity import render_identities
from core.render_roadmap import render_roadmap
from core.render_script import render_script, render_script_all_videos
from core.render_seo import render_seo, render_seo_all
from core.render_monetization import render_monetization, render_monetization_all
from core.render_repurpose import render_repurpose

OUTPUT_DIR = Path(__file__).parent / "output"

PIPELINE = {
    "01": ("01_niche_analysis", "niche_analysis", render_full, False),
    "02": ("02_channel_identity", "channel_identities", render_identities, True),
    "03": ("03_content_roadmap", "content_roadmap", render_roadmap, True),
    "04": ("04_video_scripts", "video_script", render_script, True),
    "05": ("05_seo_thumbnail", "seo_thumbnail", render_seo, True),
    "06": ("06_monetization", "monetization", render_monetization, True),
    "07": ("07_repurposing", "repurpose_pack", render_repurpose, True),
}


def run(step: str, niche: int | None = None, video: int | None = None,
        subs: int = 1_000) -> None:
    if step not in PIPELINE:
        print(f"Unbekannter Step '{step}'. Verfügbar: {', '.join(PIPELINE)}")
        sys.exit(1)

    folder, name, renderer, supports_niche = PIPELINE[step]
    target = OUTPUT_DIR / folder
    target.mkdir(parents=True, exist_ok=True)

    if step == "07" and niche is not None:
        vid = video if video is not None else 1
        md = render_repurpose(niche, vid)
        filename = f"{name}_niche{niche}_v{vid}"
    elif step == "06":
        if niche is not None:
            md = render_monetization(niche, subs)
            filename = f"{name}_niche{niche}_{subs}subs"
        else:
            md = render_monetization_all(subs)
            filename = f"{name}_all_{subs}subs"
    elif step == "05" and niche is not None:
        if video is None:
            md = render_seo_all(niche)
            filename = f"{name}_niche{niche}_all"
        else:
            md = render_seo(niche, video)
            filename = f"{name}_niche{niche}_v{video}"
    elif step == "04" and niche is not None:
        if video is None:
            md = render_script_all_videos(niche)
            filename = f"{name}_niche{niche}_all"
        else:
            md = render_script(niche, video)
            filename = f"{name}_niche{niche}_v{video}"
    elif supports_niche and niche is not None:
        md = renderer(niche)
        filename = f"{name}_niche{niche}"
    else:
        md = renderer()
        filename = name

    path = target / f"{filename}.md"
    path.write_text(md, encoding="utf-8")

    print(f"✓ Gespeichert: {path}")
    print(f"  ({len(md)} Zeichen, {md.count(chr(10))} Zeilen)")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="YouTube Growth System")
    parser.add_argument("step", help="Step-ID (01–07)")
    parser.add_argument("--niche", type=int, default=None, help="Nische 1–10")
    parser.add_argument("--video", type=int, default=None, help="Video-Nr. 1–12")
    parser.add_argument("--subs", type=int, default=1_000, help="Subscriber-Stand")
    args = parser.parse_args()
    run(args.step, args.niche, args.video, args.subs)

import json
from datetime import datetime, timezone
from pathlib import Path
from config import OUTPUT_DIR


def write_output(folder: str, name: str, markdown: str, meta: dict | None = None) -> Path:
    target = OUTPUT_DIR / folder
    target.mkdir(parents=True, exist_ok=True)

    md_path = target / f"{name}.md"
    md_path.write_text(markdown, encoding="utf-8")

    meta_path = target / f"{name}.meta.json"
    meta_data = {
        "generated_at": datetime.now(timezone.utc).isoformat(),
        **(meta or {}),
    }
    meta_path.write_text(
        json.dumps(meta_data, indent=2, ensure_ascii=False), encoding="utf-8"
    )

    return md_path

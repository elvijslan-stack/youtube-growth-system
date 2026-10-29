from __future__ import annotations

from data.identities import IDENTITIES


def render_one(rank: int) -> str:
    d = IDENTITIES[rank]
    names = "\n".join(f"   {i}. {n}" for i, n in enumerate(d["names"], 1))
    pillars = "\n".join(f"   {i}. {p}" for i, p in enumerate(d["pillars"], 1))
    return (
        f"## {rank}. {d['niche']}\n\n"
        f"**Kanalname-Optionen**\n{names}\n\n"
        f"**Tagline:** _{d['tagline']}_\n\n"
        f"**Zielpublikum-Persona:**\n   {d['audience']}\n\n"
        f"**Content-Pillars (4)**\n{pillars}\n\n"
        f"**Unique Mechanism:**\n   {d['unique_mechanism']}"
    )


def render_identities(rank: int | None = None) -> str:
    if rank is not None:
        if rank not in IDENTITIES:
            raise ValueError(f"Keine Identity für Rank {rank}")
        header = f"# Channel Identity — Nische {rank}"
        return f"{header}\n\n{render_one(rank)}\n"

    parts = ["# Channel Identities — Top 10 Nischen", ""]
    for rank in sorted(IDENTITIES):
        parts.append(render_one(rank))
        parts.append("\n---\n")
    return "\n".join(parts)

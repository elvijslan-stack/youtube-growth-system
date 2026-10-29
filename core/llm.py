import anthropic
import openai
from config import (
    PROVIDER,
    ANTHROPIC_API_KEY,
    OPENAI_API_KEY,
    MODEL,
    MAX_TOKENS,
)


def call_llm(prompt: str) -> str:
    if PROVIDER == "anthropic":
        if not ANTHROPIC_API_KEY:
            raise RuntimeError("ANTHROPIC_API_KEY fehlt in .env")
        client = anthropic.Anthropic(api_key=ANTHROPIC_API_KEY)
        resp = client.messages.create(
            model=MODEL,
            max_tokens=MAX_TOKENS,
            messages=[{"role": "user", "content": prompt}],
        )
        return resp.content[0].text

    if PROVIDER == "openai":
        if not OPENAI_API_KEY:
            raise RuntimeError("OPENAI_API_KEY fehlt in .env")
        client = openai.OpenAI(api_key=OPENAI_API_KEY)
        resp = client.chat.completions.create(
            model=MODEL,
            max_tokens=MAX_TOKENS,
            messages=[{"role": "user", "content": prompt}],
        )
        return resp.choices[0].message.content

    raise ValueError(f"Unbekannter PROVIDER: {PROVIDER}")

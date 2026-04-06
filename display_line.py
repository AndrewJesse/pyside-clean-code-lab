"""Pure display-string logic (no Qt). Kept tiny so pytest can cover it on every branch."""


def build_display_line(raw: str) -> str:
    text = raw.strip()
    if not text:
        return "Enter a name and click Apply."
    return f"Hello, {text}!"

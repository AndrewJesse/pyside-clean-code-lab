"""Pure display-string logic (no Qt). Single place for normalization, validation rules, and formatting."""

from typing import Protocol

_EMPTY_LABEL_PROMPT = "Enter a name and click Apply."
_MAX_NAME_LEN = 40


class GreetingStrategy(Protocol):
    def format(self, name: str) -> str: ...


def normalized_name(raw: str) -> str:
    return raw.strip()


def validation_error_for_name(raw: str) -> str | None:
    """Return a user-visible error string, or None if the name is acceptable."""
    name = normalized_name(raw)
    if not name:
        return "Please enter a name before applying."
    if len(name) > _MAX_NAME_LEN:
        return f"Name is too long (max {_MAX_NAME_LEN} characters)."
    return None


def format_greeting(name: str) -> str:
    """Format a non-empty normalized name."""
    return f"Hello, {name}!"


def build_display_line(raw: str) -> str:
    """Build label text without raising; used by tests and for passive empty-state copy."""
    name = normalized_name(raw)
    if not name:
        return _EMPTY_LABEL_PROMPT
    return format_greeting(name)


def apply_greeting_message(
    raw: str,
    strategy: GreetingStrategy,
) -> tuple[str | None, str | None]:
    """
    Single validation path for Apply: returns (greeting, error).
    If error is not None, greeting is None.
    """
    err = validation_error_for_name(raw)
    if err is not None:
        return None, err
    name = normalized_name(raw)
    return strategy.format(name), None

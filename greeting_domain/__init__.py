"""Domain component: validation and greeting rules (no framework imports)."""

from greeting_domain.rules import (
    apply_greeting_message,
    build_display_line,
    format_greeting,
    normalized_name,
    validation_error_for_name,
)

__all__ = [
    "apply_greeting_message",
    "build_display_line",
    "format_greeting",
    "normalized_name",
    "validation_error_for_name",
]

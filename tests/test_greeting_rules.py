from greeting_domain.rules import (
    apply_greeting_message,
    build_display_line,
    normalized_name,
    validation_error_for_name,
)
from greeting_strategies import CasualGreetingStrategy, DefaultHelloStrategy

_DEFAULT = DefaultHelloStrategy()


def test_build_display_line_trims_and_formats() -> None:
    assert build_display_line("  Ada  ") == "Hello, Ada!"


def test_build_display_line_empty_prompts() -> None:
    assert build_display_line("") == "Enter a name and click Apply."
    assert build_display_line("   ") == "Enter a name and click Apply."


def test_normalized_name() -> None:
    assert normalized_name("  x  ") == "x"


def test_validation_error_for_name() -> None:
    assert validation_error_for_name("") is not None
    assert validation_error_for_name("   ") is not None
    assert validation_error_for_name("Ada") is None
    assert validation_error_for_name("x" * 41) is not None


def test_apply_greeting_message_success() -> None:
    greeting, err = apply_greeting_message("  Ada  ", _DEFAULT)
    assert err is None
    assert greeting == "Hello, Ada!"


def test_apply_greeting_message_casual_strategy() -> None:
    greeting, err = apply_greeting_message("Ada", CasualGreetingStrategy())
    assert err is None
    assert greeting == "Hey Ada!"


def test_apply_greeting_message_empty() -> None:
    greeting, err = apply_greeting_message("  ", _DEFAULT)
    assert greeting is None
    assert err is not None


def test_apply_greeting_message_too_long() -> None:
    greeting, err = apply_greeting_message("x" * 41, _DEFAULT)
    assert greeting is None
    assert "too long" in (err or "").lower()

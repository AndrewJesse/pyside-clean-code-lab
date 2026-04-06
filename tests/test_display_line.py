from display_line import build_display_line


def test_build_display_line_trims_and_formats() -> None:
    assert build_display_line("  Ada  ") == "Hello, Ada!"


def test_build_display_line_empty_prompts() -> None:
    assert build_display_line("") == "Enter a name and click Apply."
    assert build_display_line("   ") == "Enter a name and click Apply."

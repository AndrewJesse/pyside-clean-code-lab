# Lesson 01 — Meaningful names and small functions

**Branch:** `lesson/01-names-and-functions`

## What this lesson shows

- **Names** that state intent (`_name_input`, `_greeting_label`, `_apply_button` instead of vague `_in` / `_out`).
- **Small methods** at one level of abstraction: window setup, widget factories, layout, signal wiring, and refreshing the label each live in their own step.

Behavior matches **`main`**: same UI and same use of [`display_line.py`](../../display_line.py).

## Files to open

| File | Why |
|------|-----|
| [`main.py`](../../main.py) | All changes are in `MainWindow` — compare to `main` with the command below |

## Compare to baseline (`main`)

From the repo root:

```bash
git diff main...lesson/01-names-and-functions
```

## Tests

Unchanged from baseline: run `pytest` from the repo root; coverage stays on [`display_line.py`](../../display_line.py) via [`tests/test_display_line.py`](../../tests/test_display_line.py).

## Related

- [Curriculum table (all lessons)](../CURRICULUM.MD)

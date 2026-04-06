# Lesson 03 — DRY · error handling

**Branch:** `lesson/03-dry-and-error-handling`

## What this lesson shows

- **DRY** — one validation path via `validation_error_for_name` / `apply_greeting_message`; shared `normalized_name` and `format_greeting`.
- **Visible errors** — invalid input uses `QMessageBox.warning` (no silent `except: pass`).

## Files to open

| File | Why |
|------|-----|
| [`display_line.py`](../../display_line.py) | Validation + apply pipeline |
| [`greeter_controller.py`](../../greeter_controller.py) | Surfaces domain errors in the UI |
| [`tests/test_display_line.py`](../../tests/test_display_line.py) | Validation and apply tests |

## Compare

```bash
git diff lesson/02-srp-and-separation-of-concerns...lesson/03-dry-and-error-handling
git diff main...lesson/03-dry-and-error-handling
```

## Tests

`pytest` — expanded tests for validation and strategies of error messages.

## Related

- [Curriculum](../../CURRICULUM.MD)

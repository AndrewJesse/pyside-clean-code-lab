# Lesson 02 — Single Responsibility · separation of concerns

**Branch:** `lesson/02-srp-and-separation-of-concerns`

## What this lesson shows

- **GreeterView** — builds widgets and exposes `current_name` / `set_greeting_text` / `apply_clicked` only.
- **GreeterController** — connects signals to domain; no layout code.
- **display_line.py** — pure domain (no Qt imports).

## Files to open

| File | Why |
|------|-----|
| [`greeter_view.py`](../../greeter_view.py) | View layer |
| [`greeter_controller.py`](../../greeter_controller.py) | Application wiring |
| [`main.py`](../../main.py) | Composition root (bootstrap only) |
| [`display_line.py`](../../display_line.py) | Domain |

## Compare

```bash
git diff lesson/01-names-and-functions...lesson/02-srp-and-separation-of-concerns
# or from baseline:
git diff main...lesson/02-srp-and-separation-of-concerns
```

## Tests

`pytest` on [`display_line.py`](../../display_line.py).

## Related

- [Curriculum](../../CURRICULUM.MD)

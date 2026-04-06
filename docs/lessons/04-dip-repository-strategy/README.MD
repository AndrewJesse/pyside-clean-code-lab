# Lesson 04 — Dependency inversion · repository + strategy

**Branch:** `lesson/04-dip-repository-strategy`

## What this lesson shows

- **`LabelStore` protocol** — [`label_store.py`](../../label_store.py): `InMemoryLabelStore`, `FileLabelStore` (`saved_name.txt` next to `main.py`, gitignored).
- **`GreetingStrategy` protocol** — in [`display_line.py`](../../display_line.py); implementations in [`greeting_strategy.py`](../../greeting_strategy.py) (Hello / Casual / Formal).
- **Composition root** — [`main.py`](../../main.py) constructs concrete store + strategies and passes them into `GreeterController`.

## Files to open

| File | Why |
|------|-----|
| [`main.py`](../../main.py) | Wires real `FileLabelStore` + strategy tuple |
| [`greeter_controller.py`](../../greeter_controller.py) | Depends only on `LabelStore` + strategy tuple |
| [`greeter_view.py`](../../greeter_view.py) | Style combo + Load/Save |
| [`label_store.py`](../../label_store.py) | Repository-style port + adapters |
| [`greeting_strategy.py`](../../greeting_strategy.py) | Strategy implementations |

## Compare

```bash
git diff lesson/03-dry-and-error-handling...lesson/04-dip-repository-strategy
git diff main...lesson/04-dip-repository-strategy
```

## Tests

`pytest` includes [`tests/test_label_store.py`](../../tests/test_label_store.py) (no Qt).

## Related

- [Curriculum](../../CURRICULUM.MD)

# Curriculum: three lesson branches

Super-minimal **PySide6 Qt Widgets** UI (one window) to show *why* structure matters. **No QML.** **pytest** on every branch for non-Qt code.

**Naming + small functions** are *not* a separate branch: when you split **view / controller / domain** (lesson 01), call out **meaningful names** and **small, single-purpose methods** in passing—that lesson already forces clearer boundaries and readable private methods (`_build_ui`, `_wire_signals`, etc.) if you narrate them while refactoring.

## Shared toy feature

- `QLineEdit` — user types a short string (e.g. name).
- `QPushButton` — **Apply** updates a `QLabel` from pure Python logic.
- **Lesson 03 only** — add **Load / Save** plus a **style** picker (`QComboBox` or radios) for repository + strategy.

Baseline on `main`: line edit, Apply, label; logic in [`display_line.py`](display_line.py); tests in [`tests/`](tests/).

---

## Branch 1 — `lesson/01-srp-and-separation-of-concerns`

| | |
|--|--|
| **Topics** | Single Responsibility · separation of concerns · *(in passing: meaningful names, small functions)* |
| **UI** | Unchanged from baseline |
| **Code** | **View** (widgets only) · **controller** (wiring) · **domain** (no Qt imports) |
| **Tests** | pytest on domain (and thin controller if useful) |

---

## Branch 2 — `lesson/02-dry-and-error-handling`

| | |
|--|--|
| **Topics** | DRY · error handling (no silent failures) |
| **UI** | Same + `QMessageBox` or status label on errors |
| **Code** | Single validation path; visible failures for invalid input or simulated I/O errors |
| **Tests** | pytest for validation / error outcomes |

---

## Branch 3 — `lesson/03-dip-repository-strategy`

| | |
|--|--|
| **Topics** | Dependency inversion / DI · repository + strategy |
| **UI** | Add Load/Save + style A/B picker |
| **Code** | `Protocol`/ABC for repository (in-memory vs file) and strategy (two formatters); controller depends on ports; **`main.py`** composes concrete types |
| **Tests** | pytest with fakes; no GUI driver required |

---

## Video / git workflow

```bash
git diff main...lesson/01-srp-and-separation-of-concerns
```

Optional: tag `baseline-widgets` on `main` after baseline is stable.

See [README.MD](README.MD) for run instructions and [LISTING.MD](LISTING.MD) for optional HMI/architect role context.

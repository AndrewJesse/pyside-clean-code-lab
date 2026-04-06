# Curriculum: four lesson branches

Super-minimal **PySide6 Qt Widgets** UI (one window) to show *why* structure matters. **No QML.** **pytest** on every branch for non-Qt code.

## Shared toy feature

- `QLineEdit` — user types a short string (e.g. name).
- `QPushButton` — **Apply** updates a `QLabel` from pure Python logic.
- **Lesson 04 only** — add **Load / Save** plus a **style** picker (`QComboBox` or radios) for repository + strategy.

Baseline on `main`: line edit, Apply, label; logic in [`display_line.py`](display_line.py); tests in [`tests/`](tests/).

---

## Branch 1 — `lesson/01-names-and-functions`

| | |
|--|--|
| **Topics** | Meaningful names · small functions (one level of abstraction per method) |
| **UI** | Same as baseline |
| **Code** | Refactor a dense `MainWindow` into **small private methods** with intention-revealing names (`_configure_window`, `_create_name_field`, `_build_layout`, `_wire_signals`, `_refresh_greeting_label`, …); behavior unchanged |
| **Tests** | Same pytest on [`display_line.py`](display_line.py) |

Compare to `main`:

```bash
git diff main...lesson/01-names-and-functions
```

---

## Branch 2 — `lesson/02-srp-and-separation-of-concerns`

| | |
|--|--|
| **Topics** | Single Responsibility · separation of concerns |
| **UI** | Unchanged |
| **Code** | **View** (widgets only) · **controller** (wiring) · **domain** (no Qt imports) |
| **Tests** | pytest on domain (and thin controller if useful) |

---

## Branch 3 — `lesson/03-dry-and-error-handling`

| | |
|--|--|
| **Topics** | DRY · error handling (no silent failures) |
| **UI** | Same + `QMessageBox` or status label on errors |
| **Code** | Single validation path; visible failures for invalid input or simulated I/O errors |
| **Tests** | pytest for validation / error outcomes |

---

## Branch 4 — `lesson/04-dip-repository-strategy`

| | |
|--|--|
| **Topics** | Dependency inversion / DI · repository + strategy |
| **UI** | Add Load/Save + style A/B picker |
| **Code** | `Protocol`/ABC for repository (in-memory vs file) and strategy (two formatters); controller depends on ports; **`main.py`** composes concrete types |
| **Tests** | pytest with fakes; no GUI driver required |

---

## Video / git workflow

```bash
git diff main...lesson/01-names-and-functions
```

Optional: tag `baseline-widgets` on `main` after baseline is stable.

See [README.MD](README.MD) for run instructions and [LISTING.MD](LISTING.MD) for optional HMI/architect role context.

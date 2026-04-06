# Walkthrough — `lesson/03-dry-and-error-handling`

You are on **`lesson/03-dry-and-error-handling`**. This walkthrough covers **through Lesson 03: DRY** (don’t repeat validation/format rules) and **explicit error handling** (no silent failures).

---

## 0. Setup and checks

```bash
git checkout lesson/03-dry-and-error-handling
pip install -r requirements.txt
pytest -v
python main.py
```

Tests: **7** — domain and validation paths are now fully covered without Qt.

---

## 1. Read the single “Apply pipeline”

Open [`display_line.py`](../display_line.py) and follow **one path** from raw input to result:

1. **`normalized_name`** — trimming happens here only (shared building block).
2. **`validation_error_for_name`** — empty vs too-long rules in **one** place.
3. **`apply_greeting_message(raw)`** — returns `(greeting, error)`:
   - if `error` is set, **greeting** is `None`;
   - if valid, **error** is `None`.

**Why this is good (DRY):** Apply, future features (Save, batch import), and tests all use the **same** rules. You do not copy-paste “if empty…” in the controller and again in another dialog.

**Why tuple return is good:** Callers must decide how to show failure (dialog, status bar, log) without the domain importing Qt.

---

## 2. See errors in the UI

Open [`greeter_controller.py`](../greeter_controller.py), `_on_apply_clicked`:

- If `error_message` is not `None`, it calls **`QMessageBox.warning`** and **returns** (does not update the greeting label with garbage).

**Why this is good:** Users see *that* something went wrong; you avoid silently ignoring bad input (a common maintenance bug).

**Try it:** run the app, leave the name empty, click **Apply** — you should get a dialog, not a silent no-op.

---

## 3. Read the tests as documentation

Open [`tests/test_display_line.py`](../tests/test_display_line.py).

- Tests for **`validation_error_for_name`** and **`apply_greeting_message`** encode the product rules.
- When someone asks “what’s invalid?”, point them here first.

---

## 4. Diff vs Lesson 02

```bash
git diff lesson/02-srp-and-separation-of-concerns...lesson/03-dry-and-error-handling
```

Narrate: domain grew **policy**; controller gained **presentation of failure**.

---

## 5. Reflect

1. Where would you add a third rule (e.g. “no digits in name”) so you still have **one** validation path?
2. Why should `display_line.py` avoid importing `QMessageBox`?

---

## Next

Checkout **`lesson/04-dip-repository-strategy`** for **protocols**, **LabelStore**, **GreetingStrategy**, and wiring in **`main.py`**.

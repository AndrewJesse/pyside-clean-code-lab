# Walkthrough — `lesson/02-srp-and-separation-of-concerns`

You are on **`lesson/02-srp-and-separation-of-concerns`**. This covers **baseline → Lesson 01 (names/small methods) → Lesson 02 (SRP / separation of concerns)**.

---

## 0. Setup and checks

```bash
git checkout lesson/02-srp-and-separation-of-concerns
pip install -r requirements.txt
pytest -v
python main.py
```

Tests: **2** — still only testing [`display_line.py`](../display_line.py) (domain).

---

## 1. See how the code is split

Open these three files **in this order**:

| Order | File | Responsibility |
|------|------|------------------|
| 1 | [`greeter_view.py`](../greeter_view.py) | **View** — builds widgets, exposes `current_name`, `set_greeting_text`, signal `apply_clicked`. No `build_display_line`. |
| 2 | [`greeter_controller.py`](../greeter_controller.py) | **Controller** — connects `apply_clicked` to domain; no layout code. |
| 3 | [`display_line.py`](../display_line.py) | **Domain** — pure Python, no Qt imports. |
| 4 | [`main.py`](../main.py) | **Composition root** — creates `QApplication`, `GreeterView`, `GreeterController`, shows window. |

**Why this is good:**

- **Single Responsibility:** each file has one reason to change (UI layout vs wiring vs string rules vs startup).
- **Separation of concerns:** you can reason about greeting *rules* without reading Qt widget code.
- **Testability:** pytest still hits domain without spinning up a GUI.

---

## 2. Diff against the previous lesson

vs Lesson 01 (structure only):

```bash
git diff lesson/01-names-and-functions...lesson/02-srp-and-separation-of-concerns
```

vs baseline:

```bash
git diff main...lesson/02-srp-and-separation-of-concerns
```

**What to narrate in a video:** “We moved widget creation out of the controller and domain out of the view.”

---

## 3. Trace Apply click

1. `GreeterView` button emits **`apply_clicked`**.
2. `GreeterController._on_apply_clicked` reads `view.current_name()`, calls **`build_display_line`**, writes `view.set_greeting_text(...)`.

**Why this is good:** Dependencies point **inward** toward domain; the view does not import `display_line`.

---

## 4. Reflect

1. If you changed from `QLabel` to `QPlainTextEdit`, which file would change the most? Which would stay stable?
2. Why does `test_display_line.py` still not import `PySide6`?

---

## Next

Checkout **`lesson/03-dry-and-error-handling`** for **one validation path** and **QMessageBox** error handling.

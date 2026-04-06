# Walkthrough — `lesson/01-names-and-functions`

You are on the branch **`lesson/01-names-and-functions`**. This walkthrough includes everything from the **baseline** (`main`) plus **Lesson 01: meaningful names and small functions**.

---

## 0. Setup and checks

```bash
git checkout lesson/01-names-and-functions
pip install -r requirements.txt
pytest -v
python main.py
```

Tests: **2** (same as `main` — behavior did not change).

---

## 1. Compare this branch to `main` (see the refactor)

From the repo root:

```bash
git diff main...lesson/01-names-and-functions
```

You should see only [`main.py`](../main.py) change. The UI and `display_line.py` are the same.

**What to notice:**

- `__init__` now reads like a **checklist**: configure window → create widgets → layout → wire signals.
- Private methods have **names that say what they do**: `_create_name_field`, `_wire_signals`, `_refresh_greeting_label`.
- Widget fields are named for **meaning** (`_name_input`, `_greeting_label`, `_apply_button`), not `_in` / `_out`.

**Why this is good:**

- Readers find code faster; you reduce “what does this block do?” time.
- Small methods are easier to test or reuse later, and easier to debug in a stack trace.

---

## 2. Trace one user action

1. Open [`main.py`](../main.py).
2. Start at `_on_apply_clicked` → it calls `_refresh_greeting_label`.
3. `_refresh_greeting_label` reads the line edit and calls `build_display_line` (still in [`display_line.py`](../display_line.py)).

**Why this is good:** The “apply” path is a short chain with obvious names — good for code review and videos.

---

## 3. Read the tests again

[`tests/test_display_line.py`](../tests/test_display_line.py) still targets **domain only**. Lesson 01 did not need new tests because **behavior** did not change — only structure inside `MainWindow`.

**Lesson:** Refactors that preserve behavior should keep existing tests green; add tests when you add rules or fix bugs.

---

## 4. Reflect

1. Name one private method from this branch and what would break if its name were vague (e.g. `_go`).
2. If you added a second button “Clear”, which method would you extend first: `_wire_signals` or `_build_layout`?

---

## Next

Checkout **`lesson/02-srp-and-separation-of-concerns`** and read `docs/WALKTHROUGH.MD` there for **view vs controller vs domain**.

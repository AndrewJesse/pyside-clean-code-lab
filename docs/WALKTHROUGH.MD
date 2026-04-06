# Walkthrough — baseline (`main`)

Use this document **on the `main` branch**. It steps through what exists here and *why* it is structured this way. Later branches add lessons; each branch has its own `docs/WALKTHROUGH.MD` that builds on this.

---

## 0. Setup

From the repository root:

```bash
python3 -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

---

## 1. Run the tests (always do this first)

```bash
pytest -v
```

You should see **2** tests pass.

Open [`tests/test_display_line.py`](../tests/test_display_line.py). Notice:

- Tests import **`display_line`** only — no Qt, no windows. That is intentional: **pure logic is cheap to test**.

**Why this is good:** You can change the UI or add buttons later and still prove the string rules with fast tests.

---

## 2. Read the domain module

Open [`display_line.py`](../display_line.py).

- `build_display_line(raw)` trims whitespace, treats “empty” as a special case, and returns a friendly prompt or `Hello, …`.

**Why this is good:** One place owns the greeting rule. The UI should not duplicate string logic.

---

## 3. Read the UI entrypoint

Open [`main.py`](../main.py).

Follow the flow:

1. `QApplication` starts Qt.
2. `MainWindow` builds three widgets: line edit, **Apply** button, label.
3. Clicking **Apply** calls `_on_apply_clicked`, which passes the line text into `build_display_line` and shows the result on the label.

**Why this is good (for a baseline):** Everything is in one file so a beginner can run it quickly. The tradeoff is that `MainWindow` mixes **layout**, **wiring**, and **calling domain** in one class — later branches split that up.

---

## 4. Run the app

```bash
python main.py
```

Try:

- Empty input + **Apply** → you should see the “Enter a name…” prompt on the label.
- A name with extra spaces → greeting uses the trimmed name.

---

## 5. Reflect (short answers for yourself)

1. If you changed the greeting format to “Hi, {name}!”, which **single function** should you edit?
2. Why can `test_display_line.py` run without a display server?

---

## Next

Checkout **`lesson/01-names-and-functions`** and open `docs/WALKTHROUGH.MD` there to see how naming and small methods improve `MainWindow` without changing behavior.

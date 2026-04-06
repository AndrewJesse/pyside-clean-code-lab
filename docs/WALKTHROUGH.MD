# Walkthrough — `lesson/04-dip-repository-strategy`

You are on **`lesson/04-dip-repository-strategy`**. This is the **full stack** of the lab: lessons **01–04**, ending with **Dependency Inversion**, a **repository-style `LabelStore`**, and **Strategy** for greeting wording.

---

## 0. Setup and checks

```bash
git checkout lesson/04-dip-repository-strategy
pip install -r requirements.txt
pytest -v
python main.py
```

Tests: **11** — domain, validation, and **label store** adapters (no GUI driver).

---

## 1. Dependency Inversion (the big idea)

**High-level modules** (`GreeterController`) should depend on **abstractions** (protocols), not on concrete file paths or one fixed string format.

Concrete classes are chosen in **one place**: [`main.py`](../main.py).

**Steps:**

1. Open [`main.py`](../main.py). Find where **`FileLabelStore`** and the **three strategy objects** are constructed and passed into **`GreeterController`**.
2. Open [`greeter_controller.py`](../greeter_controller.py). Notice the type hints: **`LabelStore`** and a **tuple of `GreetingStrategy`**. The controller does not know about disk paths or JSON vs memory.

**Why this is good:**

- Swap **`InMemoryLabelStore`** in tests or a future “cloud” store without rewriting the controller.
- Swap strategies (product branding, A/B test, locale) without branching `if` trees everywhere.

---

## 2. Repository pattern — `LabelStore`

Open [`label_store.py`](../label_store.py).

- **`LabelStore`** protocol: `load()` / `save(text)`.
- **`InMemoryLabelStore`** — trivial, perfect for unit tests ([`tests/test_label_store.py`](../tests/test_label_store.py)).
- **`FileLabelStore`** — persists next to the app (`saved_name.txt`, gitignored).

**Try it:** type a name, **Save**, quit, run again, **Load** — the field should repopulate (if the file is writable).

**Why this is good:** Persistence is an **adapter**; domain and controller stay free of `Path` details except at the root.

---

## 3. Strategy pattern — greeting wording

Open [`greeting_strategy.py`](../greeting_strategy.py) and [`display_line.py`](../display_line.py).

- **`GreetingStrategy`** is a **`Protocol`** in `display_line.py` (structural typing — no inheritance required).
- Implementations: **`DefaultHelloStrategy`**, **`CasualGreetingStrategy`**, **`FormalGreetingStrategy`**.
- **`apply_greeting_message(raw, strategy)`** validates once, then calls **`strategy.format(normalized_name)`**.

Open [`greeter_view.py`](../greeter_view.py): the **combo box** chooses which strategy slot maps to which implementation (indices line up with the tuple in `main.py`).

**Why this is good:** Adding a fourth tone (“Fleet / driver / service”) is a **new class + one combo entry + wire in main**, not a giant `switch`.

---

## 4. View additions

Still in [`greeter_view.py`](../greeter_view.py): **Load** / **Save** buttons emit signals; the view does not call the store.

**Why this is good:** Same SRP story as Lesson 02 — view knows clicks; controller knows side effects.

---

## 5. Error handling (carried from Lesson 03)

In [`greeter_controller.py`](../greeter_controller.py):

- Invalid name → **`QMessageBox`** (from Lesson 03).
- **Load/Save** → `try` / `except OSError` → **`QMessageBox.warning`** so IO failures are visible.

---

## 6. Diff vs Lesson 03

```bash
git diff lesson/03-dry-and-error-handling...lesson/04-dip-repository-strategy
```

---

## 7. Full tour from baseline

```bash
git diff main...lesson/04-dip-repository-strategy
```

Use this when you want one narrative: “from one file to layered, tested, swappable design.”

---

## 8. Reflect

1. To use **`InMemoryLabelStore`** in a headless integration test, which file would you **not** need to import?
2. Name a change that touches **only** `main.py` and **not** `GreeterController`.

---

## You’re done with the four lessons

Re-read [CURRICULUM.MD](CURRICULUM.MD) and tie each branch to interview talking points (boundaries, testability, swappable adapters).

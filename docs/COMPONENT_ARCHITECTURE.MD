# Component boundaries, interfaces, deployment units, and integration

Read this on branch **`topic/component-boundaries-and-integration`**.

This branch reshapes the same greeter demo as `lesson/04-dip-repository-strategy`, but the **folder layout** matches vocabulary you will use for **large, multi-team software** (including HMI / ECU-style programs): **component boundaries**, **interfaces**, **deployment units**, and **integration**.

The ideas align with job postings that ask for *scalable architecture*, *design patterns*, and *system decomposition* (see [LISTING.MD](LISTING.MD)).

---

## 1. Component boundaries

A **component** is a chunk of the system with a **clear responsibility** and **minimal knowledge** of other chunks’ internals.

| Folder (component) | Responsibility | Must not… |
|--------------------|----------------|-----------|
| [`contracts/`](../contracts/) | Shared **interfaces** (ports) only | Import Qt, files, or feature logic |
| [`greeting_domain/`](../greeting_domain/) | Validation + greeting **rules** (pure Python) | Import Qt |
| [`greeting_strategies/`](../greeting_strategies/) | Swappable **formatting** policies | Know about widgets or disk paths |
| [`greeting_persistence/`](../greeting_persistence/) | **Save/load** text | Know about greetings or Qt |
| [`greeting_ui_qt/`](../greeting_ui_qt/) | **Qt** view + presenter for this feature | Choose *which* file path or *which* strategy implementation |
| [`integration/`](../integration/) | **Wire** concrete classes for *this* build | Contain business rules (only glue) |

**Why this is good:** Teams can own a component; changes stay localized; reviews focus on one boundary at a time.

**Learning step:** Open each folder’s `__init__.py` and skim what it exports. That is the component’s **public face**.

---

## 2. Interfaces (contracts / ports)

Files in **`contracts/ports.py`** define **`Protocol`** types:

- **`LabelStore`** — “something that can `load` / `save` a string.”
- **`GreetingStrategy`** — “something that can `format` a validated name.”

**Domain** ([`greeting_domain/rules.py`](../greeting_domain/rules.py)) depends on **`GreetingStrategy`** only as a type — not on `CasualGreetingStrategy` or `FormalGreetingStrategy`.

**Presenter** ([`greeting_ui_qt/presenter.py`](../greeting_ui_qt/presenter.py)) depends on **`LabelStore`** and **`GreetingStrategy`**, not on `FileLabelStore`.

**Why this is good:** You can substitute fakes in tests, swap file vs cloud storage, or add a new strategy **without** editing domain rules.

**Learning step:** Search the repo for `LabelStore` and `GreetingStrategy`. Notice **implementations** live in other packages; **callers** only see the protocol.

---

## 3. Deployment units (logical “things we could ship separately”)

This repo is still one Python tree for teaching. In industry, each **deployment unit** is often:

- a **library** (`.so` / `.jar` / Python package),
- a **process**,
- or a **firmware partition** / **AUTOSAR SWC** with a published API.

Here, treat each **top-level package directory** as a **logical deployment unit**:

| Unit | Role in a bigger program |
|------|---------------------------|
| `contracts` | API headers / IDL — agreed types between teams |
| `greeting_domain` | Core policy — might run in CI, headless services, or multiple UIs |
| `greeting_strategies` | Optional plug-in pack (product variants) |
| `greeting_persistence` | I/O adapters (filesystem today, vehicle store tomorrow) |
| `greeting_ui_qt` | HMI adapter for Qt |
| `integration` | ECU startup / composition — **one place** per product flavor |

**Why this is good:** Interview answer: “We decompose into units with explicit contracts so variants (brands, markets, hardware) don’t fork the whole tree.”

**Learning step:** Ask yourself: *If `greeting_ui_qt` were deleted, what still compiles and what tests still run?* (Domain + persistence + strategies + contracts should.)

---

## 4. Integration (composition root)

[`integration/compose.py`](../integration/compose.py) is the **composition root**:

- It picks **`FileLabelStore`** (not `InMemoryLabelStore`).
- It instantiates the **three** concrete strategies and passes them as a tuple.
- It builds **`GreeterView`** and **`GreeterPresenter`**.

[`main.py`](../main.py) is minimal: **Qt application** + `build_greeter_window()` + event loop.

**Why this is good:** Product-specific choices (paths, backends, feature flags) stay out of domain and UI internals — the same pattern as **wiring** in automotive startup or **DI** in larger frameworks.

**Learning step:** Trace `main.py` → `build_greeter_window` → constructor arguments on `GreeterPresenter`. Every **concrete** type appears in **integration**, not inside **rules**.

---

## 5. How to study this branch (step by step)

1. **Run tests** from repo root: `pytest -v` (all fast; no GUI automation).
2. **Read** `contracts/ports.py` — two ports, no logic.
3. **Read** `greeting_domain/rules.py` — uses `GreetingStrategy` but not Qt.
4. **Read** `integration/compose.py` — list every `import` and note which package it comes from.
5. **Compare** to lesson 04: `git diff lesson/04-dip-repository-strategy...topic/component-boundaries-and-integration` — mostly moves/renames + `GreeterController` → `GreeterPresenter`.
6. **Run** `python main.py` — behavior should match lesson 04.

---

## 6. Relation to earlier lesson branches

| Lesson branch | Idea |
|----------------|------|
| `lesson/04-dip-repository-strategy` | Same DIP story with flatter files |
| **`topic/component-boundaries-and-integration`** | Same code **packaged** as **components** + explicit **integration** layer |

Use lesson 04 for “what is DI?” and this branch for “how do architects **talk about** and **structure** subsystems?”

---

## 7. One-sentence interview bridge

> “We define **ports** in a contracts package, implement **adapters** per component, and keep a thin **integration** layer that composes concrete implementations for each deployment — so teams integrate through **interfaces**, not through each other’s internals.”

That sentence maps cleanly to listings that emphasize **architecture**, **decomposition**, and **maintainable** HMI platforms.

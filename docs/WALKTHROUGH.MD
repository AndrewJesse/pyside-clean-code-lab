# Walkthrough — `topic/component-boundaries-and-integration`

You are on the **topic** branch that packages the lesson-04 behavior into **named components** plus an **`integration/`** composition root.

The detailed learning guide is **[COMPONENT_ARCHITECTURE.MD](COMPONENT_ARCHITECTURE.MD)** — read that next (boundaries, interfaces, deployment units, integration, interview bridge).

---

## Quick start

```bash
git checkout topic/component-boundaries-and-integration
pip install -r requirements.txt
pytest -v
python main.py
```

## What moved vs `lesson/04-dip-repository-strategy`

| Before (flat files) | After (component) |
|---------------------|-------------------|
| `display_line.py` | [`greeting_domain/rules.py`](../greeting_domain/rules.py) |
| `label_store.py` | [`greeting_persistence/`](../greeting_persistence/) |
| `greeting_strategy.py` | [`greeting_strategies/`](../greeting_strategies/) |
| `greeter_view.py` / `greeter_controller.py` | [`greeting_ui_qt/`](../greeting_ui_qt/) (`GreeterPresenter`) |
| Ports inside `display_line` | [`contracts/ports.py`](../contracts/ports.py) |
| Wiring in `main.py` | [`integration/compose.py`](../integration/compose.py) + thin [`main.py`](../main.py) |

```bash
git diff lesson/04-dip-repository-strategy...topic/component-boundaries-and-integration
```

---

## Next

Open [COMPONENT_ARCHITECTURE.MD](COMPONENT_ARCHITECTURE.MD) and follow sections 1–7 in order.

# PySide Clean Code Lab

Small **PySide6 Qt Widgets** demo repo for teaching **Clean Code** and **layering**: one minimal window, pure Python logic where it is easy to test, and **four lesson branches** (see [CURRICULUM.MD](CURRICULUM.MD) and [lessons/](lessons/README.MD)). Run commands from the **repository root** (parent of `docs/`).

**No QML** — widgets only, on purpose.

## Run

```bash
python -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -r requirements.txt
pytest
python main.py
```

## Layout (baseline `main`)

| File | Role |
|------|------|
| [`main.py`](../main.py) | Tiny `MainWindow`: line edit, Apply, label |
| [`display_line.py`](../display_line.py) | Pure string logic (no Qt) |
| [`tests/test_display_line.py`](../tests/test_display_line.py) | pytest |

## Lessons

- **Per-lesson notes:** [lessons/README.MD](lessons/README.MD) (folder per lesson under `docs/lessons/`)
- **Overview table:** [CURRICULUM.MD](CURRICULUM.MD) for all four branches and topics

## Optional context

[LISTING.MD](LISTING.MD) — sample HMI/architect job posting for interview talking points (not required to run the code).

## Repository name

This project is intended to live at **`pyside-clean-code-lab`** (local folder and GitHub repo name). If your remote still points at an older name, rename the repository on GitHub under **Settings → General → Repository name**, then:

```bash
git remote set-url origin https://github.com/<you>/pyside-clean-code-lab.git
```

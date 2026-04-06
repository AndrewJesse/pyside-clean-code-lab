"""
Composition root: the only place that chooses concrete adapters for this deployment.

In a larger program (e.g. cluster HMI), this maps to startup code that:
- reads configuration,
- selects vehicle vs simulation backends,
- registers plugins,
- then hands control to the UI event loop.
"""

from pathlib import Path

from contracts.ports import GreetingStrategy
from greeting_persistence import FileLabelStore
from greeting_strategies import CasualGreetingStrategy, DefaultHelloStrategy, FormalGreetingStrategy
from greeting_ui_qt.presenter import GreeterPresenter
from greeting_ui_qt.view import GreeterView


def build_greeter_window(data_path: Path | None = None) -> GreeterView:
    """
    Assemble components into a wired window. Callers own QApplication and .show().
    """
    path = data_path or Path(__file__).resolve().parent.parent / "saved_name.txt"
    label_store = FileLabelStore(path)
    strategies: tuple[GreetingStrategy, GreetingStrategy, GreetingStrategy] = (
        DefaultHelloStrategy(),
        CasualGreetingStrategy(),
        FormalGreetingStrategy(),
    )
    view = GreeterView()
    GreeterPresenter(view, label_store, strategies)
    return view

from PySide6.QtCore import QObject
from PySide6.QtWidgets import QMessageBox

from display_line import GreetingStrategy, apply_greeting_message
from greeter_view import GreeterView
from label_store import LabelStore


class GreeterController(QObject):
    """Depends on abstractions (store + strategies); composed in main.py."""

    def __init__(
        self,
        view: GreeterView,
        label_store: LabelStore,
        strategies: tuple[GreetingStrategy, GreetingStrategy, GreetingStrategy],
    ) -> None:
        super().__init__(view)
        self._view = view
        self._label_store = label_store
        self._strategies = strategies
        self._view.apply_clicked.connect(self._on_apply_clicked)
        self._view.load_clicked.connect(self._on_load_clicked)
        self._view.save_clicked.connect(self._on_save_clicked)

    def _strategy_for_view(self) -> GreetingStrategy:
        idx = self._view.strategy_slot_index()
        return self._strategies[idx]

    def _on_apply_clicked(self) -> None:
        greeting, error_message = apply_greeting_message(
            self._view.current_name(),
            self._strategy_for_view(),
        )
        if error_message is not None:
            QMessageBox.warning(self._view, "Invalid input", error_message)
            return
        assert greeting is not None
        self._view.set_greeting_text(greeting)

    def _on_load_clicked(self) -> None:
        try:
            text = self._label_store.load()
        except OSError as exc:
            QMessageBox.warning(self._view, "Load failed", str(exc))
            return
        self._view.set_name_text(text)

    def _on_save_clicked(self) -> None:
        try:
            self._label_store.save(self._view.current_name())
        except OSError as exc:
            QMessageBox.warning(self._view, "Save failed", str(exc))

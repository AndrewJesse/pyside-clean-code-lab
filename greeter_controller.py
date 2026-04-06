from PySide6.QtCore import QObject
from PySide6.QtWidgets import QMessageBox

from display_line import apply_greeting_message
from greeter_view import GreeterView


class GreeterController(QObject):
    """Wires view events to domain logic (no widget construction)."""

    def __init__(self, view: GreeterView) -> None:
        super().__init__(view)
        self._view = view
        self._view.apply_clicked.connect(self._on_apply_clicked)

    def _on_apply_clicked(self) -> None:
        greeting, error_message = apply_greeting_message(self._view.current_name())
        if error_message is not None:
            QMessageBox.warning(self._view, "Invalid input", error_message)
            return
        assert greeting is not None
        self._view.set_greeting_text(greeting)

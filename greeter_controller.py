from PySide6.QtCore import QObject

from display_line import build_display_line
from greeter_view import GreeterView


class GreeterController(QObject):
    """Wires view events to domain logic (no widget construction)."""

    def __init__(self, view: GreeterView) -> None:
        super().__init__(view)
        self._view = view
        self._view.apply_clicked.connect(self._on_apply_clicked)

    def _on_apply_clicked(self) -> None:
        message = build_display_line(self._view.current_name())
        self._view.set_greeting_text(message)

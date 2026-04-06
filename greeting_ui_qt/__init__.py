"""UI adapter component: Qt widgets + presenter (application wiring to view signals)."""

from greeting_ui_qt.presenter import GreeterPresenter
from greeting_ui_qt.view import GreeterView

__all__ = ["GreeterPresenter", "GreeterView"]

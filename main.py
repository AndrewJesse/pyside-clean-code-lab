import sys
from pathlib import Path

from PySide6.QtWidgets import QApplication

from greeter_controller import GreeterController
from greeter_view import GreeterView
from greeting_strategy import CasualGreetingStrategy, DefaultHelloStrategy, FormalGreetingStrategy
from label_store import FileLabelStore


def main() -> None:
    app = QApplication(sys.argv)
    view = GreeterView()
    data_path = Path(__file__).resolve().parent / "saved_name.txt"
    store = FileLabelStore(data_path)
    strategies = (
        DefaultHelloStrategy(),
        CasualGreetingStrategy(),
        FormalGreetingStrategy(),
    )
    GreeterController(view, store, strategies)
    view.resize(420, 260)
    view.show()
    raise SystemExit(app.exec())


if __name__ == "__main__":
    main()

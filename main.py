import sys

from PySide6.QtWidgets import QApplication

from greeter_controller import GreeterController
from greeter_view import GreeterView


def main() -> None:
    app = QApplication(sys.argv)
    view = GreeterView()
    GreeterController(view)
    view.resize(400, 160)
    view.show()
    raise SystemExit(app.exec())


if __name__ == "__main__":
    main()

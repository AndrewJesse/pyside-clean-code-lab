import sys

from PySide6.QtWidgets import QApplication

from integration.compose import build_greeter_window


def main() -> None:
    app = QApplication(sys.argv)
    window = build_greeter_window()
    window.resize(420, 260)
    window.show()
    raise SystemExit(app.exec())


if __name__ == "__main__":
    main()

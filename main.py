import sys

from PySide6.QtWidgets import (
    QApplication,
    QLabel,
    QLineEdit,
    QPushButton,
    QVBoxLayout,
    QWidget,
)

from display_line import build_display_line


class MainWindow(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle("PySide Clean Code Lab")
        self._input = QLineEdit()
        self._input.setPlaceholderText("Name")
        self._output = QLabel("")
        self._output.setWordWrap(True)
        apply_btn = QPushButton("Apply")
        apply_btn.clicked.connect(self._on_apply_clicked)

        layout = QVBoxLayout()
        layout.addWidget(self._input)
        layout.addWidget(apply_btn)
        layout.addWidget(self._output)
        self.setLayout(layout)

    def _on_apply_clicked(self) -> None:
        self._output.setText(build_display_line(self._input.text()))


def main() -> None:
    app = QApplication(sys.argv)
    window = MainWindow()
    window.resize(400, 160)
    window.show()
    raise SystemExit(app.exec())


if __name__ == "__main__":
    main()

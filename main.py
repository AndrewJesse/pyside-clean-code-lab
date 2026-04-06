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
        self._configure_window()
        self._name_input = self._create_name_field()
        self._apply_button = self._create_apply_button()
        self._greeting_label = self._create_greeting_label()
        self._build_layout()
        self._wire_signals()

    def _configure_window(self) -> None:
        self.setWindowTitle("PySide Clean Code Lab")

    def _create_name_field(self) -> QLineEdit:
        field = QLineEdit()
        field.setPlaceholderText("Name")
        return field

    def _create_apply_button(self) -> QPushButton:
        return QPushButton("Apply")

    def _create_greeting_label(self) -> QLabel:
        label = QLabel("")
        label.setWordWrap(True)
        return label

    def _build_layout(self) -> None:
        layout = QVBoxLayout()
        layout.addWidget(self._name_input)
        layout.addWidget(self._apply_button)
        layout.addWidget(self._greeting_label)
        self.setLayout(layout)

    def _wire_signals(self) -> None:
        self._apply_button.clicked.connect(self._on_apply_clicked)

    def _on_apply_clicked(self) -> None:
        self._refresh_greeting_label()

    def _refresh_greeting_label(self) -> None:
        raw_name = self._name_input.text()
        self._greeting_label.setText(build_display_line(raw_name))


def main() -> None:
    app = QApplication(sys.argv)
    window = MainWindow()
    window.resize(400, 160)
    window.show()
    raise SystemExit(app.exec())


if __name__ == "__main__":
    main()

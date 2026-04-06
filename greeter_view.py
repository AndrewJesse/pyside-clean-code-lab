from PySide6.QtCore import Signal
from PySide6.QtWidgets import QLabel, QLineEdit, QPushButton, QVBoxLayout, QWidget


class GreeterView(QWidget):
    """Widgets only: layout, user input, and display text."""

    apply_clicked = Signal()

    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle("PySide Clean Code Lab")
        self._name_input = QLineEdit()
        self._name_input.setPlaceholderText("Name")
        self._greeting_label = QLabel("")
        self._greeting_label.setWordWrap(True)
        apply_btn = QPushButton("Apply")
        apply_btn.clicked.connect(self.apply_clicked.emit)

        layout = QVBoxLayout()
        layout.addWidget(self._name_input)
        layout.addWidget(apply_btn)
        layout.addWidget(self._greeting_label)
        self.setLayout(layout)

    def current_name(self) -> str:
        return self._name_input.text()

    def set_greeting_text(self, text: str) -> None:
        self._greeting_label.setText(text)

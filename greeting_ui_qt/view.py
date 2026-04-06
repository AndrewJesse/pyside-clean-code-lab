from PySide6.QtCore import Signal
from PySide6.QtWidgets import (
    QComboBox,
    QHBoxLayout,
    QLabel,
    QLineEdit,
    QPushButton,
    QVBoxLayout,
    QWidget,
)


class GreeterView(QWidget):
    """Widgets only: layout, user input, display text, style picker, load/save."""

    apply_clicked = Signal()
    load_clicked = Signal()
    save_clicked = Signal()

    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle("PySide Clean Code Lab — components demo")
        self._name_input = QLineEdit()
        self._name_input.setPlaceholderText("Name")
        self._greeting_label = QLabel("")
        self._greeting_label.setWordWrap(True)

        self._strategy_combo = QComboBox()
        self._strategy_combo.addItem("Hello (classic)", userData=0)
        self._strategy_combo.addItem("Casual", userData=1)
        self._strategy_combo.addItem("Formal", userData=2)

        apply_btn = QPushButton("Apply")
        apply_btn.clicked.connect(self.apply_clicked.emit)
        load_btn = QPushButton("Load")
        load_btn.clicked.connect(self.load_clicked.emit)
        save_btn = QPushButton("Save")
        save_btn.clicked.connect(self.save_clicked.emit)

        button_row = QHBoxLayout()
        button_row.addWidget(load_btn)
        button_row.addWidget(save_btn)

        layout = QVBoxLayout()
        layout.addWidget(QLabel("Greeting style:"))
        layout.addWidget(self._strategy_combo)
        layout.addWidget(self._name_input)
        layout.addWidget(apply_btn)
        layout.addLayout(button_row)
        layout.addWidget(self._greeting_label)
        self.setLayout(layout)

    def current_name(self) -> str:
        return self._name_input.text()

    def set_name_text(self, text: str) -> None:
        self._name_input.setText(text)

    def set_greeting_text(self, text: str) -> None:
        self._greeting_label.setText(text)

    def strategy_slot_index(self) -> int:
        return self._strategy_combo.currentIndex()

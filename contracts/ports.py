from typing import Protocol


class LabelStore(Protocol):
    """Persistence port: load/save a text label (name field) without UI details."""

    def load(self) -> str: ...

    def save(self, text: str) -> None: ...


class GreetingStrategy(Protocol):
    """Formatting port: turn a validated name into user-visible greeting text."""

    def format(self, name: str) -> str: ...

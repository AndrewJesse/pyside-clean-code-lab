from pathlib import Path


class InMemoryLabelStore:
    def __init__(self, initial: str = "") -> None:
        self._value = initial

    def load(self) -> str:
        return self._value

    def save(self, text: str) -> None:
        self._value = text


class FileLabelStore:
    def __init__(self, path: Path) -> None:
        self._path = path

    def load(self) -> str:
        if not self._path.exists():
            return ""
        return self._path.read_text(encoding="utf-8").strip()

    def save(self, text: str) -> None:
        self._path.write_text(text, encoding="utf-8")

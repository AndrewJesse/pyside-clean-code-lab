from pathlib import Path

from label_store import FileLabelStore, InMemoryLabelStore


def test_in_memory_label_store_roundtrip() -> None:
    store = InMemoryLabelStore("Ada")
    assert store.load() == "Ada"
    store.save("Bob")
    assert store.load() == "Bob"


def test_file_label_store_roundtrip(tmp_path: Path) -> None:
    path = tmp_path / "name.txt"
    store = FileLabelStore(path)
    assert store.load() == ""
    store.save("  Ada  ")
    assert store.load() == "Ada"
    assert path.read_text(encoding="utf-8") == "  Ada  "


def test_file_label_store_missing_file_is_empty(tmp_path: Path) -> None:
    store = FileLabelStore(tmp_path / "nope.txt")
    assert store.load() == ""

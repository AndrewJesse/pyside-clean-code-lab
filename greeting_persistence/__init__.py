"""Persistence component: LabelStore implementations (file, in-memory)."""

from greeting_persistence.impl import FileLabelStore, InMemoryLabelStore

__all__ = ["FileLabelStore", "InMemoryLabelStore"]

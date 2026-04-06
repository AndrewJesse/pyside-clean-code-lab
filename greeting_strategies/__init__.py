"""Strategy component: swappable greeting formatters (implements GreetingStrategy)."""

from greeting_strategies.impl import CasualGreetingStrategy, DefaultHelloStrategy, FormalGreetingStrategy

__all__ = ["CasualGreetingStrategy", "DefaultHelloStrategy", "FormalGreetingStrategy"]

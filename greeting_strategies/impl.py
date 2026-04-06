from greeting_domain.rules import format_greeting


class CasualGreetingStrategy:
    def format(self, name: str) -> str:
        return f"Hey {name}!"


class FormalGreetingStrategy:
    def format(self, name: str) -> str:
        return f"Good day, {name}."


class DefaultHelloStrategy:
    """Same wording as the default domain helper; useful for tests and combo slot 0."""

    def format(self, name: str) -> str:
        return format_greeting(name)

from display_line import format_greeting


class CasualGreetingStrategy:
    def format(self, name: str) -> str:
        return f"Hey {name}!"


class FormalGreetingStrategy:
    def format(self, name: str) -> str:
        return f"Good day, {name}."


class DefaultHelloStrategy:
    """Same wording as early lessons; useful for tests and default combo slot."""

    def format(self, name: str) -> str:
        return format_greeting(name)

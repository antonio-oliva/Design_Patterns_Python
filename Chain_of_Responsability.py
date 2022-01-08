from abc import ABC, abstractmethod
from typing import Optional


class BaseHandler(ABC):
    """
    The default chaining behavior can be implemented inside a base handler class.
    It also declares a method for executing a request.
    """
    _next_handler: Optional["BaseHandler"] = None

    def set_next(self, handler: "BaseHandler") -> "BaseHandler":
        self._next_handler = handler
        return handler

    @abstractmethod
    def handle(self, request: str) -> Optional[str]:
        if self._next_handler:
            return self._next_handler.handle(request)
        return None


"""
All Concrete Handlers either handle a request or pass it to the next handler in
the chain.
"""


class MonkeyHandler(BaseHandler):
    def handle(self, request: str) -> str:
        if request == "Banana":
            return f"Monkey: I'll eat the {request}"
        else:
            return super().handle(request)


class SquirrelHandler(BaseHandler):
    def handle(self, request: str) -> str:
        if request == "Nut":
            return f"Squirrel: I'll eat the {request}"
        else:
            return super().handle(request)


class DogHandler(BaseHandler):
    def handle(self, request: str) -> str:
        if request == "MeatBall":
            return f"Dog: I'll eat the {request}"
        else:
            return super().handle(request)


def client_code(handler: BaseHandler) -> None:
    """
    The client code is usually suited to work with a single handler.
    In most cases, it is not even aware that the handler is part of a chain.
    """
    for food in ["Nut", "Banana", "Cup of coffee"]:
        print(f"\nClient: Who wants a {food}?")
        result = handler.handle(food)
        if result:
            print(f"\t{result}")
        else:
            print(f"\t{food} was left untouched.")


if __name__ == "__main__":
    monkey = MonkeyHandler()
    squirrel = SquirrelHandler()
    dog = DogHandler()

    monkey.set_next(squirrel).set_next(dog)

    # The client should be able to send a request to any handler, not just the first one in the chain.
    print("Chain: Monkey > Squirrel > Dog")
    client_code(monkey)
    print("\n")

    print("Sub-chain: Squirrel > Dog")
    client_code(squirrel)

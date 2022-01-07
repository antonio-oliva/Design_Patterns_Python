from abc import ABC, abstractmethod


class Notifier(ABC):
    """
    The base Notifier interface defines operations that can be altered by decorators.
    """

    @abstractmethod
    def send(self) -> str:
        pass


class ConcreteNotifier(Notifier):
    """
    Concrete Notifier(s) provide default implementations of the operations. There might be several variations of
    these classes.
    """

    def send(self) -> str:
        return "Concrete Notifier: sending popup notification."


class Decorator(Notifier):
    """
    The base Decorator class follows the same interface as the other components.
    The primary purpose of this class is to define the wrapping interface for all concrete decorators.
    The default implementation of the wrapping code might include a field for storing a wrapped component and the means
    to initialize it.
    """

    def __init__(self, notifier: Notifier) -> None:
        self._notifier = notifier

    @property
    def notifier(self) -> Notifier:
        """
        The Decorator delegates all work to the wrapped component.
        """

        return self._notifier

    def send(self) -> str:
        return self.notifier.send()


class SmsDecorator(Decorator):
    """
    Concrete Decorator(s) (like SmsDecoretor and FacebookDecoretor) call the wrapped object and alter its result.
    """

    def send(self) -> str:
        """
        Decorators may call parent implementation of the operation, instead of calling the wrapped object directly.
        This approach simplifies extension of decorator classes.
        """
        return f"{self.notifier.send()}" \
               f"\n SMS Decorator: sending SMS notification."


class FacebookDecorator(Decorator):
    """
    Decorators can execute their behavior either before or after the call to a wrapped object.
    """

    def send(self) -> str:
        return f"{self.notifier.send()}" \
               f"\n Facebook Decorator: sending Facebook notification."


def client_code(notifier: Notifier) -> None:
    """
    The client code works with all objects using the Component interface. This way it can stay independent of the
    concrete classes of components it works with.
    """

    print(f"RESULT:\n {notifier.send()}", end="")


if __name__ == "__main__":
    # This way the client code can support both simple components...
    simple = ConcreteNotifier()
    print("Client: I've got a simple notifier:")
    client_code(simple)
    print("\n")

    # ...as well as decorated ones.

    # Decorators can wrap not only simple components but the other decorators as well.
    decorator1 = SmsDecorator(simple)
    decorator2 = FacebookDecorator(decorator1)
    print("Client: Now I've got a decorated notifier:")
    client_code(decorator2)
    print("\n")

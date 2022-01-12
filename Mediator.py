from abc import ABC


class AbstractMediator(ABC):
    """
    The AbstractMediator interface declares a method used by components to notify the mediator about various events.
    The mediator may react to these events and pass the execution to other components.
    """

    def notify(self, sender: "BaseComponent", event: str) -> None:
        pass


class Mediator(AbstractMediator):
    def __init__(self, component1: "BaseComponent", component2: "BaseComponent") -> None:
        self._component1 = component1
        self._component1.mediator = self
        self._component2 = component2
        self._component2.mediator = self

    def notify(self, sender: "BaseComponent", event: str) -> None:
        if sender == self._component1 and event == "A":
            print("Mediator reacts on Component 1 action A and triggers following operations:")
            self._component2.do_c()
        elif sender == self._component2 and event == "D":
            print("Mediator reacts on Component 2 action D and triggers following operations:")
            self._component1.do_b()
            self._component2.do_c()


class BaseComponent:
    """
    The Base Component provides the basic functionality of storing a mediator's instance inside component objects.
    """

    def __init__(self, mediator: AbstractMediator = None) -> None:
        self._mediator = mediator

    @property
    def mediator(self) -> AbstractMediator:
        return self._mediator

    @mediator.setter
    def mediator(self, mediator: AbstractMediator) -> None:
        self._mediator = mediator


"""
Concrete Components implement various functionality. They don't depend on other
components. They also don't depend on any concrete mediator classes.
"""


class Component1(BaseComponent):
    def do_a(self) -> None:
        print("Component 1 does A.")
        self.mediator.notify(self, "A")

    def do_b(self) -> None:
        print("Component 1 does B.")
        self.mediator.notify(self, "B")


class Component2(BaseComponent):
    def do_c(self) -> None:
        print("Component 2 does C.")
        self.mediator.notify(self, "C")

    def do_d(self) -> None:
        print("Component 2 does D.")
        self.mediator.notify(self, "D")


if __name__ == "__main__":
    # The client code.
    c1 = Component1()
    c2 = Component2()
    mediator = Mediator(c1, c2)

    print("Client triggers Component 1 operation A.")
    c1.do_a()

    print("\nClient triggers Component 2 operation D.")
    c2.do_d()

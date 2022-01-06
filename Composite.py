from abc import ABC, abstractmethod
from typing import Set


class Component(ABC):
    """
    The base Component class declares common operations for both simple and
    complex objects of a composition.
    """

    @abstractmethod
    def price(self) -> float:
        pass


class Product(Component):

    def __init__(self, price: float) -> None:
        self._price = price

    @property
    def price(self) -> float:
        return self._price


class Box(Component):

    def __init__(self, price: float) -> None:
        self._price = price
        self._components: Set[Component] = set()

    def add(self, component: Component) -> None:
        self._components.add(component)

    def remove(self, component: Component) -> None:
        self._components.remove(component)

    @property
    def price(self) -> float:
        totalPrice = self._price
        for product in self._components:
            totalPrice += product.price

        return totalPrice


def client_code(component: Component) -> None:
    print(f"Component price: {component.price:.2f} €")


if __name__ == "__main__":
    # The client code can support the simple Product components...
    simple = Product(11.2)
    print("\nClient: I've got a simple component:")
    client_code(simple)

    # ...as well as complex composites
    box = Box(1.25)

    smallerBox1 = Box(0.8)
    smallerBox1.add(Product(4.25))
    smallerBox1.add(Product(1.3))

    smallerBox2 = Box(0.5)
    smallerBox2.add(Product(2.05))

    box.add(smallerBox1)
    box.add(smallerBox2)

    print("\nClient: I've got a complex composite component:")
    client_code(box)

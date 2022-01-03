from abc import ABC, abstractmethod


class Delivery(ABC):
    """
    The Product interface declares the operations that all concrete products
    must implement.
    """
    @abstractmethod
    def operation(self):
        pass


"""
Concrete Products provide various implementations of the Product interface.
"""


class DeliveryByTruck(Delivery):
    def operation(self) -> None:
        print(f"Delivery will be done by TRUCK!\n")


class DeliveryByTrain(Delivery):
    def operation(self) -> None:
        print(f"Delivery will be done by TRAIN!\n")


class Creator(ABC):
    """
    The Creator class declares the factory method that is supposed to return an
    object of a Product class. The Creator's subclasses usually provide the
    implementation of this method.
    """
    @abstractmethod
    def factoryMethod(self):
        """
        Note that the Creator may also provide some default implementation of
        the factory method.
        """
        pass

    def startDelivery(self) -> None:
        """
        Also note that, despite its name, the Creator's primary responsibility
        is not creating products. Usually, it contains some core business logic
        that relies on Product objects, returned by the factory method.
        Subclasses can indirectly change that business logic by overriding the
        factory method and returning a different type of product from it.
        """
        # Call the factory method to create a Product object.
        delivery = self.factoryMethod()
        # Now, use the product.
        delivery.operation()


"""
Concrete Creators override the factory method in order to change the resulting
product's type.
"""


class CreatorDeliveryTruck(Creator):
    """
    Note that the signature of the method still uses the abstract product type,
    even though the concrete product is actually returned from the method. This
    way the Creator can stay independent of concrete product classes.
    """
    def factoryMethod(self) -> DeliveryByTruck:
        return DeliveryByTruck()


class CreatorDeliveryTrain(Creator):
    def factoryMethod(self) -> DeliveryByTrain:
        return DeliveryByTrain()


if __name__ == "__main__":
    print('\n********************************')
    print('*** FACTORY METHOD IN PYTHON ***')
    print('********************************\n')

    c1 = CreatorDeliveryTruck()
    c1.startDelivery()

    c2 = CreatorDeliveryTrain()
    c2.startDelivery()

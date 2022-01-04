class Subsystem1:
    @staticmethod
    def operation1():
        print("Subsystem1: Ready!")

    @staticmethod
    def operationN():
        print("Subsystem1: Go!")


class Subsystem2:
    @staticmethod
    def operation1():
        print("Subsystem2: Get ready!")

    @staticmethod
    def operationN():
        print("Subsystem2: Fire!")


class Facade:
    """
    The Facade class provides a simple interface to the complex logic of one or several subsystems. The Facade delegates
    the client requests to the appropriate objects within the subsystem. The Facade is also responsible for managing
    their lifecycle. All of this shields the client from the undesired complexity of the subsystem.
    """
    def __init__(self, subsystem1: Subsystem1 = Subsystem1(), subsystem2: Subsystem2 = Subsystem2()) -> None:
        self.subsystem1 = subsystem1
        self.subsystem2 = subsystem2

    def operations(self):
        """
        The Facade's methods are convenient shortcuts to the sophisticated functionality of the subsystems. However,
        clients get only to a fraction of a subsystem's capabilities.
        """
        print("Facade initializes subsystems:")
        self.subsystem1.operation1()
        self.subsystem2.operation1()
        print("Facade orders subsystems to perform the action:")
        self.subsystem1.operationN()
        self.subsystem2.operationN()
        print("Facade has ended!")


class Client:
    """
    The client code works with complex subsystems through a simple interface provided by the Facade. When a facade
    manages the lifecycle of the subsystem, the client might not even know about the existence of the subsystem. This
    approach lets you keep the complexity under control.
    """
    @staticmethod
    def run(facade: Facade):
        facade.operations()


if __name__ == "__main__":
    # The client code may have some of the subsystem's objects already created.
    # In this case, it might be worthwhile to initialize the Facade with these objects instead of letting the Facade
    # create new instances.
    f = Facade()

    Client.run(f)

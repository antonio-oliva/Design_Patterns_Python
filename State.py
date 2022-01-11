from abc import ABC, abstractmethod


class Elevator:
    """
    The Elevator class is the context. It should be initiated with a default state.
    """

    _state = None

    def __init__(self, state: "State") -> None:
        self.setElevator(state)

    def setElevator(self, state: "State"):
        """
        Method to change the state of the object
        """
        self._state = state
        self._state.elevator = self

    def presentState(self):
        print(f"Elevator is in {type(self._state).__name__}\n")

    # The methods for executing the elevator functionality. These depends on the current state of the object.
    def pushDownButton(self):
        self._state.pushDownButton()

    def pushUpButton(self):
        self._state.pushUpButton()


class State(ABC):
    """
    The common State interface for all the states
    """

    _elevator = None

    @property
    def elevator(self) -> Elevator:
        return self._elevator

    @elevator.setter
    def elevator(self, elevator: Elevator) -> None:
        self._elevator = elevator

    @abstractmethod
    def pushDownButton(self) -> None:
        pass

    @abstractmethod
    def pushUpButton(self) -> None:
        pass


# The concrete states
class FirstFloor(State):

    def pushDownButton(self) -> None:
        """
        If the down button is pushed when it is already on the first floor, nothing should happen
        """
        print("Already in the bottom floor!")

    def pushUpButton(self) -> None:
        """
        If up button is pushed, move upwards then it changes its state to second floor.
        """
        print("Elevator moving upward one floor...")
        self.elevator.setElevator(SecondFloor())


class SecondFloor(State):

    def pushDownButton(self) -> None:
        """
        If down button is pushed it should move one floor down
        """
        print("Elevator moving down a floor...")
        self.elevator.setElevator(FirstFloor())

    def pushUpButton(self) -> None:
        """
        If up button is pushed, move upwards then it changes its state to third floor.
        """
        print("Elevator moving upward one floor...")
        self.elevator.setElevator(ThirdFloor())


class ThirdFloor(State):

    def pushDownButton(self) -> None:
        """
        If down button is pushed it should move one floor down
        """
        print("Elevator moving down a floor...")
        self.elevator.setElevator(SecondFloor())

    def pushUpButton(self) -> None:
        """
        If up button is pushed nothing should happen
        """
        print("Already in the top floor!")


if __name__ == "__main__":
    # The client code
    myElevator = Elevator(FirstFloor())
    myElevator.presentState()

    # Up button is pushed twice
    myElevator.pushUpButton()
    myElevator.pushUpButton()
    myElevator.presentState()

    # Down button is pushed
    myElevator.pushDownButton()
    myElevator.presentState()

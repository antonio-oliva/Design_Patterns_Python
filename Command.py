from abc import ABC, abstractmethod


class Command(ABC):
    """COMMAND INTERFACE
    The switch interface, that all commands will implement
    """
    _backup = None

    def __init__(self, light: "Light") -> None:  # The _light is the Receiver
        self._light = light

    def backup(self):
        self._backup = self._light.state

    def undo(self):
        self._light.state = self._backup

    @staticmethod
    @abstractmethod
    def execute() -> None:
        pass


class SwitchOnCommand(Command):
    """SWITCH ON COMMAND
    A Command object, that implements the Command interface and runs the command on the designated Receiver
    """
    def execute(self) -> None:
        self.backup()
        print("Turning light on...")
        self._light.turnOn()


class SwitchOffCommand(Command):
    """SWITCH OFF COMMAND
    A Command object, that implements the Command interface and runs the command on the designated Receiver
    """
    def execute(self) -> None:
        self.backup()
        print("Turning light off...")
        self._light.turnOff()


class Light:
    """RECEIVER
    Implements the methods called by Commands through the execute()
    """

    _state = 0

    def turnOn(self) -> None:
        self.state = 1

    def turnOff(self) -> None:
        self.state = 0

    @property
    def state(self) -> int:
        return self._state

    @state.setter
    def state(self, state: int) -> None:
        self._state = state

    def showState(self) -> None:
        if self.state:
            print("\033[92;1m" + "Light is ON" + "\033[0m")
        else:
            print("\033[31;1m" + "Light is OFF" + "\033[0m")


class Switch:
    """INVOKER
    The Invoker is associated with one or several commands. It sends a request to the command.
    """

    def __init__(self) -> None:
        self._commands = {}
        self._history = []

    def showHistory(self) -> None:
        """
        Print the command history
        """
        for index, commandName in enumerate(self._history):
            print(f"{index}:\t{commandName}")

    def registerCommand(self, commandName: str, command: Command) -> None:
        """
        Add a command to the invoker
        """
        self._commands[commandName] = command

    def executeCommand(self, commandName: str):
        """
        Execute a registered command
        """
        if commandName in self._commands.keys():
            self._commands[commandName].execute()
            self._history.append(self._commands[commandName])
        else:
            print(f"Command [{commandName}] not recognised")

    def undo(self):
        if len(self._history):
            print("Undoing last command...")
            lastCommand = self._history[-1]
            lastCommand.undo()
            self._history.pop(-1)
        else:
            print("No commands to undo!")


if __name__ == "__main__":
    # Create the Receiver (a Light)
    light = Light()

    # Create Commands
    switchOn = SwitchOnCommand(light)
    switchOff = SwitchOffCommand(light)

    # Create the Invoker (a Switch) and register Commands
    switch = Switch()
    switch.registerCommand("on", switchOn)
    switch.registerCommand("off", switchOff)

    # Execute the commands
    light.showState()
    switch.executeCommand("on")
    light.showState()
    switch.executeCommand("off")
    light.showState()
    switch.undo()
    light.showState()
    switch.undo()
    light.showState()
    switch.undo()
    light.showState()

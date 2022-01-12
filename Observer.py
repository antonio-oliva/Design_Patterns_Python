from typing import List
from abc import ABC, abstractmethod


class Publisher:

    observers: dict = {}

    def __init__(self, operations: List[str]) -> None:
        for operation in operations:
            self.observers[operation] = []

    def subscribe(self, eventType: str, observer: "Observer") -> None:
        self.observers[eventType].append(observer)

    def unsubscribe(self, eventType: str, observer: "Observer") -> None:
        self.observers[eventType].remove(observer)

    def notify(self, eventType: str, filePath: str) -> None:
        for observer in self.observers[eventType]:
            observer.update(eventType, filePath)


class Editor:

    publisher: Publisher = None
    _file: str = None

    def __init__(self) -> None:
        self.publisher = Publisher(["open", "save"])

    def openFile(self, filePath: str) -> None:
        self._file = filePath
        self.publisher.notify("open", self._file)

    def saveFile(self) -> None:
        if self._file:
            self.publisher.notify("save", self._file)
        else:
            raise FileNotFoundError("Please first open a file!")


class Observer(ABC):
    @abstractmethod
    def update(self, eventType: str, filePath: str) -> None:
        pass


class EmailNotificationObserver(Observer):
    _email: str = None

    def __init__(self, email: str):
        self._email = email

    def update(self, eventType: str, filePath: str) -> None:
        print(f"Email to {self._email}:\n\tSomeone has performed {eventType} operation with the following file: {filePath}")


class LogObserver(Observer):
    _logPath: str = None

    def __init__(self, logPath: str) -> None:
        self._logPath = logPath

    def update(self, eventType: str, filePath: str) -> None:
        print(f"Save to log {self._logPath}:\n\tSomeone has performed {eventType} operation with the following file: {filePath}")


if __name__ == "__main__":
    editor = Editor()
    editor.publisher.subscribe("open", LogObserver("/path/to/log/file.txt"))
    editor.publisher.subscribe("save", EmailNotificationObserver("admin@example.com"))

    editor.openFile("test.txt")
    editor.saveFile()

from abc import ABC, abstractmethod


class Network(ABC):

    def __init__(self, username, password):
        self.username = username
        self.password = password

    def post(self, message: str) -> bool:
        """
        Authenticate before posting. Every network uses a different authentication method.
        """
        if self.logIn():
            # Send the post data.
            result = self.sendData(message)
            self.logOut()
            return result
        return False

    @abstractmethod
    def logIn(self) -> bool:
        pass

    @staticmethod
    @abstractmethod
    def sendData(data: str) -> bool:
        pass

    @abstractmethod
    def logOut(self) -> None:
        pass


class Facebook(Network):

    def logIn(self) -> bool:
        print("\nChecking user's parameters")
        print(f"Name: {self.username}")
        print(f"Password: {'*' * len(self.password)}")
        print("\n\nLogIn success on Facebook")
        return True

    @staticmethod
    def sendData(data: str) -> bool:
        messagePosted = True
        if messagePosted:
            print(f"Message: '{data}' was posted on Facebook")
            return True
        return False

    def logOut(self) -> None:
        print(f"User: '{self.username}' was logged out from Facebook")


class Instagram(Network):

    def logIn(self) -> bool:
        print("\nChecking user's parameters")
        print(f"Name: {self.username}")
        print(f"Password: {'*' * len(self.password)}")
        print("\n\nLogIn success on Instagram")
        return True

    @staticmethod
    def sendData(data: str) -> bool:
        messagePosted = True
        if messagePosted:
            print(f"Message: '{data}' was posted on Intagram")
            return True
        return False

    def logOut(self) -> None:
        print(f"User: '{self.username}' was logged out from Instagram")


if __name__ == "__main__":
    username = input("Input user name: ")
    password = input("Input password: ")
    message = input("\nInput message: \n")

    choice = int(input("\nChoose social network for posting message.\n" +
                   "1 - Facebook\n" +
                   "2 - Instagram\n"))

    if choice == 1:
        network = Facebook(username, password)
    elif choice == 2:
        network = Instagram(username, password)

    network.post(message)


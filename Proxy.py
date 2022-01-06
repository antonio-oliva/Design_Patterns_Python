from abc import ABC, abstractmethod


class Service(ABC):
    """
    The Service interface declares common operations for both RealService and the Proxy. As long as the client works
    with RealService using this interface, you'll be able to pass it a proxy instead of a real service.
    """
    @abstractmethod
    def request(self) -> None:
        pass


class RealService(Service):
    """
    The RealService contains some core business logic. Usually, RealService(s) are capable of doing some useful work
    which may also be very slow or sensitive - e.g. correcting input data. A Proxy can solve these issues without any
    changes to the RealService's code.
    """
    def request(self) -> None:
        print("Real Service: handling request.")


class Proxy(Service):
    """
    The Proxy has an interface identical to the RealService.
    """
    def __init__(self, realService: RealService):
        self.real_service = realService

    def request(self) -> None:
        """
        The most common applications of the Proxy pattern are lazy loading, caching, controlling the access, logging,
        etc. A Proxy can perform one of these things and then, depending on the result, pass the execution to the same
        method in a linked RealService object.
        """
        if self.check_access():
            self.real_service.request()
            self.log_access()

    def log_access(self):
        print("Proxy: Logging the time of request.")

    def check_access(self) -> bool:
        print("Proxy: Checking access prior to firing a real request.")
        return True


def client_code(service: Service) -> None:
    """
    The client code is supposed to work with all objects (both real services and proxies) via the Service interface in
    order to support both real services and proxies.
    """
    service.request()


if __name__ == "__main__":
    print("Client: Executing the client code with a real service:")
    real_service = RealService()
    client_code(real_service)

    print("")

    print("Client: Executing the same client code with a proxy:")
    proxy = Proxy(real_service)
    client_code(proxy)

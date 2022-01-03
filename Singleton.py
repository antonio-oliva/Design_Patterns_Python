class SingletonMetaclass(type):
    """
    The Singleton class can be implemented in different ways in Python. Some
    possible methods include: base class, decorator, metaclass. We will use the
    metaclass because it is best suited for this purpose.
    """
    _instances = {}

    def __call__(cls, *args, **kwargs):
        """
        Possible changes to the value of the `__init__` argument do not affect
        the returned instance.
        """
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]


class Singleton(metaclass=SingletonMetaclass):

    def some_function(self):
        """
        Finally, any singleton should define some business logic, which can be
        executed on its instance.
        """
        print("Running Singleton's some function\n")


# ############################################################################## #
# My implementation without metaclass as in the Java example
class SingletonWithoutMetaclass:
    _instance = None

    def __new__(cls, *args, **kwargs):
        try:
            kwargs['viaGetInstance']
        except KeyError:
            raise NotImplementedError('New SingletonWithoutMetaclass objects can only be inizialized via the getInstance method')

    @classmethod
    def getInstance(cls):
        if not cls._instance:
            cls._instance = SingletonWithoutMetaclass(viaGetInstance=True)
        return cls._instance


if __name__ == "__main__":
    # The client code.
    print("\n\n%%%%%%% SINGLETON with metaclass %%%%%%%")

    s1 = Singleton()
    s2 = Singleton()

    # Check that s2 is exactly s1 (same id, which means same memory location)
    print("s1 id: " + str(id(s1)))
    print("s2 id: " + str(id(s2)))

    if id(s1) == id(s2):
        print("Singleton works, both variables contain the same instance.")
    else:
        print("Singleton failed, variables contain different instances.")

    # ############################################################################## #
    # Client code in case of my implementation without metaclass
    print("\n\n%%%%%%% SINGLETON without metaclass %%%%%%%")
    s3 = SingletonWithoutMetaclass.getInstance()
    s4 = SingletonWithoutMetaclass.getInstance()
    # s4 = SingletonWithoutMetaclass()
    print("s3 id: " + str(id(s3)))
    print("s4 id: " + str(id(s4)))

    if id(s3) == id(s4):
        print("Singleton w/o metaclass works, both variables contain the same instance.")
    else:
        print("Singleton w/o metaclass failed, variables contain different instances.")

    # Check that a notImplementError is raised if initializing out of getInstace
    try:
        s5 = SingletonWithoutMetaclass()
    except NotImplementedError:
        print("NotImplementError correctly raised when trying: s5 = SingletonWithoutMetaclass()")

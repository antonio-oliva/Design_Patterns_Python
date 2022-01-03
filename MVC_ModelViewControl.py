# MVC stands for Model - View - Control
import json


# ############################# MODEL ############################# #
class Model:
    """
    In this example, the Model class is a Person (or User) class
    """
    def __init__(self, first_name=None, last_name=None):
        self.first_name = first_name
        self.last_name = last_name

    @property
    def signature(self):
        return f"{self.first_name} {self.last_name}"

    @classmethod
    def getAll(cls):
        """
        Returns all people inside db.txt as list of Person objects
        """
        database = open('mvc_db.txt', 'r')
        result = []
        json_list = json.loads(database.read())
        for item in json_list:
            user = cls(item['first_name'], item['last_name'])
            result.append(user)
        return result


# ############################## VIEW ############################## #
class View:
    @staticmethod
    def showAllView(users):
        print(f'In our db we have {len(users)} users. Here they are: {[user.signature for user in users]}')

    @staticmethod
    def startView():
        print('MVC - the simplest example')

    @staticmethod
    def endView():
        print('Goodbye!')


# ############################# CONTROL ############################# #
class Controller:
    # We could instantiate a Controller with different models and views
    def __init__(self, model, view):
        self.model = model
        self.view = view

    def showAll(self):
        users = self.model.getAll()
        return self.view.showAllView(users)

    def start(self):
        self.view.startView()
        while True:
            controllerInput = input('Do you want to see everyone in my db? [y/n] \n')
            if controllerInput in ('y', 'Y'):
                return self.showAll()
            elif controllerInput in ('n', 'N'):
                return self.view.endView()
            else:
                print("Please, insert a valid request!")
                continue


# ######### #
# main #
c = Controller(Model(), View())
c.start()

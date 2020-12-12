import abc
from os import system, name

class customLoad(metaclass=abc.ABCMeta):
    """Template class for making loading figures"""
    def __init__(self):
        self.name = None
        self.width = None

    @classmethod
    def __subclasshook__(cls, subclass):
        #return (hasattr(subclass, 'clear') and
        #        callable(subclass.clear) and
        #        hasattr(subclass, 'showBar') and
        #        callable(subclass.showBar) or
        #        NotImplemented)

        return (hasattr(subclass, 'showBar') and
                callable(subclass.showBar) or
                NotImplemented)

    @abc.abstractmethod
    def showBar(self) :
        raise NotImplementedError

    def clear(self):
        """Clears output on screen"""
        # for windows
        if name == 'nt':
            _ = system('cls')
        # for mac and linux(here, os.name is 'posix')
        else:
            _ = system('clear')
from abc import ABC, ABCMeta, abstractmethod

class AbstractInputProvider(ABC, metaclass=ABCMeta):
    def __init__(self):
        pass

    @abstractmethod
    def is_input_depleted(self):
        pass

    @abstractmethod
    def get_next_input(self):
        pass
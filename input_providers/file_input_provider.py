from .abstract_input_provider import AbstractInputProvider

class AbstractInputProvider():
    def __init__(self):
        pass

    def is_input_depleted(self):
        return False

    def get_next_input(self):
        return {}
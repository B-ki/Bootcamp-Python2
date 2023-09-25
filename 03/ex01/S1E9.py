from abc import ABC, abstractmethod


class Character(ABC):
    """Class Character"""
    @abstractmethod
    def __init__(self, first_name, is_alive=True):
        self.first_name = first_name
        self.is_alive = is_alive

    def die(self):
        """Die method"""
        self.is_alive = False


class Stark(Character):
    """Class Stark inheriting from Character class"""
    def __init__(self, first_name, is_alive=True):
        """Stark constructor"""
        super().__init__(first_name=first_name, is_alive=is_alive)

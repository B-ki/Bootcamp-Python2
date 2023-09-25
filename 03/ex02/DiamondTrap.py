from S1E7 import Baratheon, Lannister


class King(Baratheon, Lannister):
    """Class King from Baratheon and Lannister"""
    def __init__(self, first_name):
        """Constructing King"""
        super().__init__(first_name=first_name)

    def set_eyes(self, color):
        self.eyes = color

    def set_hairs(self, color):
        self.hair = color

    def get_eyes(self):
        return self.eyes

    def get_hairs(self):
        return self.hair

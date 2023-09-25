from S1E9 import Character


class Baratheon(Character):
    """Class Baratheon"""
    def __init__(self, first_name, is_alive=True):
        """Constructing Baratheon"""
        super().__init__(first_name=first_name, is_alive=is_alive)
        self.family_name = "Baratheon"
        self.eyes = "brown"
        self.hair = "dark"

    def __str__(self) -> str:
        return f'{self.family_name}, {self.eyes}, {self.hair}'

    def __repr__(self):
        return self.__str__()


class Lannister(Character):
    """Class Lannister"""
    def __init__(self, first_name, is_alive=True):
        """Constructing Lannister"""
        super().__init__(first_name=first_name, is_alive=is_alive)
        self.family_name = "Lannister"
        self.eyes = "blue"
        self.hair = "light"

    def create_lannister(self, first_name):
        """Creating Lannister"""
        return Lannister(first_name, is_alive=True)

    def __str__(self):
        return f'{self.family_name}, {self.eyes}, {self.hair}'

    def __repr__(self):
        return self.__str__()

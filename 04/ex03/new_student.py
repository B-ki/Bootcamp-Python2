import random
import string
from dataclasses import dataclass


def generate_id() -> str:
    '''generate_id'''
    return "".join(random.choices(string.ascii_lowercase, k=15))


@dataclass
class Student:
    '''Student class'''
    name: str
    surname: str
    active: bool
    login: str
    ID: str

    def __init__(self, name, surname):
        '''Student constructor'''
        self.name = name
        self.surname = surname
        self.active = True
        self.login = name[0] + surname[0:]
        self.ID = generate_id()

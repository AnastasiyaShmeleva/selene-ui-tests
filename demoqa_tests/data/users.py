import dataclasses
from datetime import date
from enum import Enum


class Gender(Enum):
    MALE = 'Male'
    FEMALE = 'Female'
    OTHER = 'Other'


class Subject(Enum):
    HISTORY = 'History'
    ENGLISH = 'English'


class Hobby(Enum):
    SPORTS = 'Sports'
    READING = 'Reading'
    MUSIC = 'Music'


@dataclasses.dataclass
class User:
    first_name: str
    last_name: str
    email: str
    gender: Gender
    number: str
    date_of_birth: date
    subjects: list[Subject]
    hobbies: list[Hobby]
    picture: str
    current_address: str
    state: str
    city: str


student = User(
    first_name='Ivan',
    last_name='Ivanov',
    email='test@test.ru',
    gender=Gender.MALE,
    number='9101112233',
    date_of_birth=date(1995, 4, 17),
    subjects=[Subject.HISTORY, Subject.ENGLISH],
    hobbies=[Hobby.READING, Hobby.MUSIC],
    picture='images.jpeg',
    current_address='11 Lenin Avenue',
    state='Haryana',
    city='Karnal'
)

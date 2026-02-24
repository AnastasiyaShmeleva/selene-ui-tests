import dataclasses


@dataclasses.dataclass(frozen=True)
class Birthday:
    day: str
    month: str
    year: str


@dataclasses.dataclass
class User:
    first_name: str
    last_name: str
    email: str
    gender: str
    number: str
    birthday: Birthday
    subjects: list[str]
    hobbies: list[str]
    picture: str
    current_address: str
    state: str
    city: str


student = User(
    first_name='Ivan',
    last_name='Ivanov',
    email='test@test.ru',
    gender='Male',
    number='9101112233',
    birthday=Birthday(
        day='17',
        month='April',
        year='1995',
    ),
    subjects=['History', 'English'],
    hobbies=['Reading', 'Music'],
    picture='images.jpeg',
    current_address='11 Lenin Avenue',
    state='Haryana',
    city='Karnal'
)

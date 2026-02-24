from demoqa_tests.data import users
from demoqa_tests.pages.registration_page import RegistrationPage
from demoqa_tests import resource


def test_registration_form():
    # Подготавливаем тестовые данные
    student = users.student

    registration_page = RegistrationPage()
    registration_page.open()

    registration_page \
        .fill_first_name(student.first_name) \
        .fill_last_name(student.last_name) \
        .fill_email(student.email) \
        .select_gender(student.gender) \
        .fill_mobile_number(student.number) \
        .select_date_of_birth(
            student.birthday.day,
            student.birthday.month,
            student.birthday.year,
        )

    for subject in student.subjects:
        registration_page.select_subject(subject)

    for hobby in student.hobbies:
        registration_page.select_hobby(hobby)

    # Пример через круглые скобки
    (
        registration_page
        .upload_picture(resource.path(student.picture))
        .fill_current_address(student.current_address)
        .fill_state(student.state)
        .fill_city(student.city)
        .submit()
    )

    # Проверка поп-ап
    registration_page.should_have_registered(student)

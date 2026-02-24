from demoqa_tests.pages.registration_page import RegistrationPage
from demoqa_tests import resource


def test_registration_form():
    # Подготавливаем тестовые данные
    form_data = {
        'first_name': 'Ivan',
        'last_name': 'Ivanov',
        'email': 'test@test.ru',
        'gender': 'Male',
        'number': '9101112233',
        'month': 'April',
        'year': '1995',
        'day': '17',
        'subjects': ['History', 'English'],
        'hobbies': ['Reading', 'Music'],
        'photo': 'images.jpeg',
        'current_address': '11 Lenin Avenue',
        'state': 'Haryana',
        'city': 'Karnal'
    }

    registration_page = RegistrationPage()
    registration_page.open()

    registration_page \
        .fill_first_name(form_data['first_name']) \
        .fill_last_name(form_data['last_name']) \
        .fill_email(form_data['email']) \
        .select_gender(form_data['gender']) \
        .fill_mobile_number(form_data['number']) \
        .select_date_of_birth(
            form_data['day'],
            form_data['month'],
            form_data['year'],
        )

    for subject in form_data['subjects']:
        registration_page.select_subject(subject)

    for hobby in form_data['hobbies']:
        registration_page.select_hobby(hobby)

    # Пример через круглые скобки
    (
        registration_page
        .upload_picture(resource.path(form_data["photo"]))
        .fill_current_address(form_data['current_address'])
        .fill_state(form_data['state'])
        .fill_city(form_data['city'])
        .submit()
    )

    # Проверка поп-ап
    registration_page.should_have_registered(form_data)

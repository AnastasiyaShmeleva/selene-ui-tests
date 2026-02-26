import allure

from demoqa_tests import resource
from demoqa_tests.application import app
from demoqa_tests.data import users

@allure.feature('Регистрация')
@allure.story('Валидные данные')
@allure.title('Регистрация нового пользователя')
def test_registration_form():
    # GIVEN
    student = users.student

    app.registration_page.open()

    # WHEN
    app.registration_page \
        .fill_first_name(student.first_name) \
        .fill_last_name(student.last_name) \
        .fill_email(student.email) \
        .select_gender(student.gender) \
        .fill_mobile_number(student.number) \
        .select_date_of_birth(student.date_of_birth)

    app.registration_page.select_subjects(student.subjects)
    app.registration_page.select_hobbies(student.hobbies)

    # Пример через круглые скобки
    (
        app.registration_page
        .upload_picture(resource.path(student.picture))
        .fill_current_address(student.current_address)
        .fill_state(student.state)
        .fill_city(student.city)
        .submit()
    )

    # THEN
    app.registration_page.should_have_registered(student)

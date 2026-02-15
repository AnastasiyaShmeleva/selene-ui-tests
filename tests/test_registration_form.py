import os

from selene import browser, have, command


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
        'current_address': '11 Lenin Avenue',
        'state': 'Haryana',
        'city': 'Karnal'
        }

    browser.open('/automation-practice-form')

    # Удаление рекламы
    ads = browser.all('[id^=google_ads][id$=container__]')
    ads.with_(timeout=10).wait_until(have.size_greater_than_or_equal(3))
    ads.perform(command.js.remove)

    # Ввод имени и почты
    browser.element('#firstName').type(form_data['first_name'])
    browser.element('#lastName').type(form_data['last_name'])
    browser.element('#userEmail').type(form_data['email'])

    # Выбор пола
    browser.element('[for="gender-radio-1"]').click()

    # Ввод номера телефона
    browser.element('#userNumber').type(form_data['number'])

    # Выбор даты рождения
    browser.element('#dateOfBirthInput').click()
    browser.element('.react-datepicker__month-select').type(form_data['month'])
    browser.element('.react-datepicker__year-select').type(form_data['year'])
    browser.element(f'.react-datepicker__day--0{form_data['day']}:not(.react-datepicker__day--outside-month)').click()

    # Выбор предметов из выпадающего списка
    browser.element('#subjectsInput').type(form_data['subjects'][0][:3])
    browser.all('[class$="-option"]').element_by(have.exact_text(form_data['subjects'][0])).click()
    browser.element('#subjectsInput').type(form_data['subjects'][1][:1])
    browser.all('[class$="-option"]').element_by(have.text(form_data['subjects'][1])).click()

    # Выбор хобби
    browser.all('.form-check-label').element_by(have.exact_text(form_data['hobbies'][0])).click()
    browser.all('.form-check-label').element_by(have.exact_text(form_data['hobbies'][1])).click()

    # Загрузка фото
    browser.element('#uploadPicture').set_value(os.path.abspath('tests/resources/images.jpeg'))

    # Ввод адреса
    browser.element('#currentAddress').type(form_data['current_address'])

    # Выбор штата и города
    browser.element('#state input').type(form_data['state']).press_enter()
    browser.element('#city input').type(form_data['city']).press_enter()

    # Нажатие кнопки Отправить
    browser.element('#submit').perform(command.js.click)

    # Проверка поп-ап
    check_pop_up(form_data)


def check_pop_up(form_data):
    browser.element('.table-responsive').all('td').even.should(have.exact_texts(
        f"{form_data['first_name']} {form_data['last_name']}",
        form_data['email'],
        form_data['gender'],
        form_data['number'],
        f"{form_data['day']} {form_data['month']},{form_data['year']}",
        f"{form_data['subjects'][0]}, {form_data['subjects'][1]}",
        f"{form_data['hobbies'][0]}, {form_data['hobbies'][1]}",
        'images.jpeg',
        form_data['current_address'],
        f"{form_data['state']} {form_data['city']}"
    ))

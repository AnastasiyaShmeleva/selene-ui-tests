import os

from selene import browser, have


def test_form_verification():
    # Подготавливаем тестовые данные
    form_data = {
        'first_name': 'Ivan',
        'last_name': 'Ivanov',
        'email': 'test@test.ru',
        'gender': 'Other',
        'number': '9101112233',
        'subjects': ['History', 'English'],
        'hobbies': ['Reading', 'Music'],
        'current_address': 'Test address',
        'state': 'Haryana',
        'city': 'Karnal'
        }

    browser.open('/automation-practice-form')

    browser.execute_script("""
        document.querySelector('#fixedban')?.remove();
        document.querySelector('footer')?.remove();
    """)

    # Ввод имени и почты
    browser.element('#firstName').type(form_data['first_name'])
    browser.element('#lastName').type(form_data['last_name'])
    browser.element('#userEmail').type(form_data['email'])

    # Выбор пола
    browser.all('.custom-control-label').element_by(have.exact_text(form_data['gender'])).click()

    # Ввод номера телефона
    browser.element('#userNumber').type(form_data['number'])

    # Выбор даты рождения
    browser.element('#dateOfBirthInput').click()
    browser.element('.react-datepicker__month-select').element('[value="3"]').click()
    browser.element('.react-datepicker__year-select').element('[value="1995"]').click()
    browser.element('[aria-label="Choose Monday, April 10th, 1995"]').click()

    # Выбор предметов из выпадающего списка
    browser.element('#subjectsInput').type(form_data['subjects'][0][:2])
    browser.all('[class$="-option"]').element_by(have.text(form_data['subjects'][0])).click()
    browser.element('#subjectsInput').type(form_data['subjects'][1][:1])
    browser.all('[class$="-option"]').element_by(have.text(form_data['subjects'][1])).click()

    # Выбор хобби
    browser.all('.custom-control-label').element_by(have.exact_text(form_data['hobbies'][0])).click()
    browser.all('.custom-control-label').element_by(have.exact_text(form_data['hobbies'][1])).click()

    # Загрузка фото
    browser.element('#uploadPicture').send_keys(
        os.path.abspath('/Users/an_shmeleva/PycharmProjects/selene-ui-tests/images.jpeg'))

    # Ввод адреса
    browser.element('#currentAddress').type(form_data['current_address'])

    # Выбор штата и города из выпадающего списка
    browser.element('#state').click()
    browser.all('[class$="-option"]').element_by(have.exact_text(form_data['state'])).click()
    browser.element('#city').click()
    browser.all('[class$="-option"]').element_by(have.exact_text(form_data['city'])).click()

    # Нажатие кнопки Отправить
    browser.element('#submit').click()

    # Проверка поп-ап
    check_pop_up(form_data)


def check_pop_up(form_data):
    table = browser.element('.table-responsive')

    expected_data = {
        'Student Name': f"{form_data['first_name']} {form_data['last_name']}",
        'Student Email': form_data['email'],
        'Gender': form_data['gender'],
        'Mobile': form_data['number'],
        'Date of Birth': '10 April,1995',
        'Subjects': f"{form_data['subjects'][0]}, {form_data['subjects'][1]}",
        'Hobbies': f"{form_data['hobbies'][0]}, {form_data['hobbies'][1]}",
        'Picture': 'images.jpeg',
        'Address': form_data['current_address'],
        'State and City': f"{form_data['state']} {form_data['city']}",
    }

    for label, value in expected_data.items():
        table.should(have.text(f'{label} {value}'))

import os

from selene import browser, have


def test_form_verification():
    # Подготавливаем тестовые данные
    first_name = 'Ivan'
    last_name = 'Ivanov'
    email = 'test@test.ru'
    number = '9101112233'
    gender = 'Other'
    subjects = ['hi', 'History', 'e', 'English']
    hobbies = ['Reading', 'Music']
    current_address = 'Test address'
    state = 'Haryana'
    city = 'Karnal'

    browser.open('/')

    browser.execute_script("""
        document.querySelector('#fixedban')?.remove();
        document.querySelector('footer')?.remove();
    """)

    # Ввод имени и почты
    browser.element('#firstName').type(first_name)
    browser.element('#lastName').type(last_name)
    browser.element('#userEmail').type(email)

    # Выбор пола
    browser.all('.custom-control-label').element_by(have.exact_text(gender)).click()

    # Ввод номера телефона
    browser.element('#userNumber').type(number)

    # Выбор даты рождения
    browser.element('#dateOfBirthInput').click()
    browser.element('.react-datepicker__month-select').element('[value="3"]').click()
    browser.element('.react-datepicker__year-select').element('[value="1995"]').click()
    browser.element('[aria-label="Choose Monday, April 10th, 1995"]').click()

    # Выбор предметов из выпадающего списка
    browser.element('#subjectsInput').type(subjects[0])
    browser.all('[class$="-option"]').element_by(have.text(subjects[1])).click()
    browser.element('#subjectsInput').type(subjects[2])
    browser.all('[class$="-option"]').element_by(have.text(subjects[3])).click()

    # Выбор хобби
    browser.all('.custom-control-label').element_by(have.exact_text(hobbies[0])).click()
    browser.all('.custom-control-label').element_by(have.exact_text(hobbies[1])).click()

    # Загрузка фото
    browser.element('#uploadPicture').send_keys(
        os.path.abspath('/Users/an_shmeleva/Desktop/rozi-5120x2880-4k-hd-8k-cveti-rozoviy-4884.jpg'))

    # Ввод адреса
    browser.element('#currentAddress').type(current_address)

    # Выбор штата и города из выпадающего списка
    browser.element('#state').click()
    browser.all('[class$="-option"]').element_by(have.exact_text(state)).click()
    browser.element('#city').click()
    browser.all('[class$="-option"]').element_by(have.exact_text(city)).click()

    # Нажатие кнопки Отправить
    browser.element('#submit').click()

    check_pop_up()


def check_pop_up():
    pass

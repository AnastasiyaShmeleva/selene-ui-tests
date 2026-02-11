import os

from selene import browser, have


def test_form_verification():
    browser.open('/')

    browser.execute_script("""
        document.querySelector('#fixedban')?.remove();
        document.querySelector('footer')?.remove();
    """)

    # Ввод имени и почты
    browser.element('#firstName').type('Ivan')
    browser.element('#lastName').type('Ivanov')
    browser.element('#userEmail').type('test@test.ru')

    # Выбор пола
    browser.all('.custom-control-label').element_by(have.exact_text('Other')).click()

    # Ввод номера телефона
    browser.element('#userNumber').type('9101112233')

    # Выбор даты рождения
    browser.element('#dateOfBirthInput').click()
    browser.element('.react-datepicker__month-select').element('[value="3"]').click()
    browser.element('.react-datepicker__year-select').element('[value="1995"]').click()
    browser.element('[aria-label="Choose Monday, April 10th, 1995"]').click()

    # Выбор предметов из выпадающего списка
    browser.element('#subjectsInput').type('hi')
    browser.all('[class$="-option"]').element_by(have.text('History')).click()
    browser.element('#subjectsInput').type('e')
    browser.all('[class$="-option"]').element_by(have.text('English')).click()

    # Выбор хобби
    browser.all('.custom-control-label').element_by(have.exact_text('Reading')).click()
    browser.all('.custom-control-label').element_by(have.exact_text('Music')).click()

    # Загрузка фото
    browser.element('#uploadPicture').send_keys(
        os.path.abspath('/Users/an_shmeleva/Desktop/rozi-5120x2880-4k-hd-8k-cveti-rozoviy-4884.jpg'))

    # Ввод адреса
    browser.element('#currentAddress').type('Test address')

    # Выбор штата и города из выпадающего списка
    browser.element('#state').click()
    browser.all('[class$="-option"]').element_by(have.exact_text('Haryana')).click()
    browser.element('#city').click()
    browser.all('[class$="-option"]').element_by(have.exact_text('Karnal')).click()

    # Нажатие кнопки Отправить
    browser.element('#submit').click()

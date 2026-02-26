import allure
from selene import browser, have, command

from demoqa_tests.data.users import User


class RegistrationPage:
    def __init__(self):
        self.first_name = browser.element('#firstName')
        self.last_name = browser.element('#lastName')
        self.email = browser.element('#userEmail')
        self.gender = browser.all('[name=gender]')
        self.mobile_number = browser.element('#userNumber')
        self.date_of_birth = browser.element('#dateOfBirthInput')
        self.month_select = browser.element('.react-datepicker__month-select')
        self.year_select = browser.element('.react-datepicker__year-select')
        self.subjects_input = browser.element('#subjectsInput')
        self.hobbies = browser.all('.form-check-label')
        self.upload_picture_input = browser.element('#uploadPicture')
        self.current_address = browser.element('#currentAddress')
        self.state_input = browser.element('#state input')
        self.city_input = browser.element('#city input')
        self.submit_button = browser.element('#submit')
        self.result_table_cells = browser.element('.table-responsive').all('td')

    @allure.step('Открываем страницу регистрации')
    def open(self):
        browser.open('/automation-practice-form')

        # Удаление рекламы
        ads = browser.all('[id^=google_ads][id$=container__]')
        ads.with_(timeout=10).wait_until(have.size_greater_than_or_equal(3))
        ads.perform(command.js.remove)

        return self

    @allure.step('Заполняем имя: {value}')
    def fill_first_name(self, value):
        self.first_name.type(value)
        return self

    @allure.step('Заполняем фамилию: {value}')
    def fill_last_name(self, value):
        self.last_name.type(value)
        return self

    @allure.step('Заполняем почту: {value}')
    def fill_email(self, value):
        self.email.type(value)
        return self

    def select_gender(self, gender):
        with allure.step(f'Выбираем пол: {gender.value}'):
            self.gender.element_by(have.value(gender.value)).element('..').click()
        return self

    @allure.step('Заполняем номер телефона: {value}')
    def fill_mobile_number(self, value):
        self.mobile_number.type(value)
        return self

    # @allure.step('Выбираем дату рождения: {date.strftime("%d %B,%Y")}')
    def select_date_of_birth(self, date):
        self.date_of_birth.click()
        self.month_select.type(date.strftime('%B'))
        self.year_select.type(str(date.year))
        browser.element(f'.react-datepicker__day--0{str(date.day)}:not(.react-datepicker__day--outside-month)').click()
        return self

    def select_subjects(self, subjects):
        subjects_names = ', '.join(subject.value for subject in subjects)

        with allure.step(f'Выбираем предметы: {subjects_names}'):
            for subject in subjects:
                self.subjects_input.type(subject.value).press_enter()
        return self

    def select_hobbies(self, hobbies):
        hobbies_names = ', '.join(hobby.value for hobby in hobbies)

        with allure.step(f'Выбираем хобби: {hobbies_names}'):
            for hobby in hobbies:
                self.hobbies.element_by(have.exact_text(hobby.value)).click()
        return self

    @allure.step('Загружаем фото')
    def upload_picture(self, path):
        self.upload_picture_input.set_value(path)
        return self

    @allure.step('Заполняем адрес: {value}')
    def fill_current_address(self, value):
        self.current_address.type(value)
        return self

    @allure.step('Выбираем штат: {value}')
    def fill_state(self, value):
        self.state_input.type(value).press_enter()
        return self

    @allure.step('Выбираем город: {value}')
    def fill_city(self, value):
        self.city_input.type(value).press_enter()
        return self

    @allure.step('Отправляем форму')
    def submit(self):
        self.submit_button.perform(command.js.click)
        return self

    @allure.step('Проверяем заполненные данные')
    def should_have_registered(self, user: User):
        self.result_table_cells.even.should(have.exact_texts(
            f"{user.first_name} {user.last_name}",
            user.email,
            user.gender.value,
            user.number,
            user.date_of_birth.strftime('%d %B,%Y'),
            ', '.join(subject.value for subject in user.subjects),
            ', '.join(hobby.value for hobby in user.hobbies),
            user.picture,
            user.current_address,
            f"{user.state} {user.city}"
        ))
        return self

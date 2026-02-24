import os

from selene import browser, have, command

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
        self.subjects = browser.all('[class$="-option"]')
        self.hobbies = browser.all('.form-check-label')
        self.upload_picture_input = browser.element('#uploadPicture')
        self.current_address = browser.element('#currentAddress')
        self.state_input = browser.element('#state input')
        self.city_input = browser.element('#city input')
        self.submit_button = browser.element('#submit')
        self.result_table_cells = browser.element('.table-responsive').all('td')

    def open(self):
        browser.open('/automation-practice-form')

        # Удаление рекламы
        ads = browser.all('[id^=google_ads][id$=container__]')
        ads.with_(timeout=10).wait_until(have.size_greater_than_or_equal(3))
        ads.perform(command.js.remove)

        return self

    def fill_first_name(self, value):
        self.first_name.type(value)
        return self

    def fill_last_name(self, value):
        self.last_name.type(value)
        return self

    def fill_email(self, value):
        self.email.type(value)
        return self

    def select_gender(self, value):
        self.gender.element_by(have.value(value)).element('..').click()
        return self

    def fill_mobile_number(self, value):
        self.mobile_number.type(value)
        return self

    def select_date_of_birth(self, day, month, year):
        self.date_of_birth.click()
        self.month_select.type(month)
        self.year_select.type(year)
        browser.element(f'.react-datepicker__day--0{day}:not(.react-datepicker__day--outside-month)').click()
        return self

    def select_subject(self, value):
        self.subjects_input.type(value[:2])
        self.subjects.element_by(have.exact_text(value)).click()
        return self

    def select_hobby(self, value):
        self.hobbies.element_by(have.exact_text(value)).click()
        return self

    def upload_picture(self, path):
        self.upload_picture_input.set_value(os.path.abspath(path))
        return self

    def fill_current_address(self, value):
        self.current_address.type(value)
        return self

    def fill_state(self, value):
        self.state_input.type(value).press_enter()
        return self

    def fill_city(self, value):
        self.city_input.type(value).press_enter()
        return self

    def submit(self):
        self.submit_button.perform(command.js.click)
        return self

    def should_have_registered(self, data):
        self.result_table_cells.even.should(have.exact_texts(
            f"{data['first_name']} {data['last_name']}",
            data['email'],
            data['gender'],
            data['number'],
            f"{data['day']} {data['month']},{data['year']}",
            ', '.join(data['subjects']),
            ', '.join(data['hobbies']),
            data['photo'],
            data['current_address'],
            f"{data['state']} {data['city']}"
        ))
        return self

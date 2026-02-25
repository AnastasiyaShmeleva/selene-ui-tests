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

    def select_gender(self, gender):
        self.gender.element_by(have.value(gender.value)).element('..').click()
        return self

    def fill_mobile_number(self, value):
        self.mobile_number.type(value)
        return self

    def select_date_of_birth(self, date):
        self.date_of_birth.click()
        self.month_select.type(date.strftime('%B'))
        self.year_select.type(str(date.year))
        browser.element(f'.react-datepicker__day--0{str(date.day)}:not(.react-datepicker__day--outside-month)').click()
        return self

    def select_subject(self, subjects):
        for subject in subjects:
            self.subjects_input.type(subject.value).press_enter()
        return self

    def select_hobby(self, hobbies):
        for hobby in hobbies:
            self.hobbies.element_by(have.exact_text(hobby.value)).click()
        return self

    def upload_picture(self, path):
        self.upload_picture_input.set_value(path)
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

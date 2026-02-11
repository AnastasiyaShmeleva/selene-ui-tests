from selene import browser, be, have, command


def test_form_verification():
    browser.open('/')
    browser.driver.maximize_window()

    browser.execute_script("""
        document.querySelector('#fixedban')?.remove();
        document.querySelector('footer')?.remove();
    """)

    browser.element('#firstName').should(be.visible).type('Ivan')
    browser.element('#lastName').should(be.visible).type('Ivanov')
    browser.element('#userEmail').should(be.visible).type('test@test.ru')

    browser.element('#gender-radio-3').should(be.visible).scroll_to().click()

    browser.element('#userNumber').should(be.visible).type('+791099999999')

    #TODO добавить действия
    browser.element('#dateOfBirthInput').should(be.visible).scroll_to().click()
    browser.element('.subjects-auto-complete__value-container subjects-auto-complete__value-container--is-multi css-1hwfws3').should(be.visible).type('test@test.ru')

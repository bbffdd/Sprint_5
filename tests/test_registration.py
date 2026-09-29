'''
Проверяет, по условию что по результату полю юзер присваивается User, получается согласно логике бэкенда
корректней было бы, что не пустое значение.
'''
import uuid

from selenium.webdriver.support import expected_conditions as ec

from locators import (
    CREATE_ACCOUNT_BUTTON,
    EMAIL_INPUT,
    PASSWORD_INPUT,
    PASSWORD_REPEAT_INPUT,
    USER_AVATAR_BUTTON,
    USER_NAME,
    NO_ACCOUNT_BUTTON,
)


def generate_email():
    return f"user_{uuid.uuid4().hex}@testik.ru"


def fill_registration_form(driver, wait, email, password="pass123"):
    wait.until(
        ec.visibility_of_element_located(EMAIL_INPUT)
    ).send_keys(email)

    wait.until(
        ec.visibility_of_element_located(PASSWORD_INPUT)
    ).send_keys(password)

    wait.until(
        ec.visibility_of_element_located(PASSWORD_REPEAT_INPUT)
    ).send_keys(password)


def test_registration_with_valid_data(registration_page, wait):
    fill_registration_form(
        registration_page,
        wait,
        generate_email(),
    )

    button = wait.until(
        ec.element_to_be_clickable(CREATE_ACCOUNT_BUTTON)
    )

    button.click()

    wait.until(
        ec.visibility_of_element_located(USER_AVATAR_BUTTON)
    )

    user_name = wait.until(
        ec.visibility_of_element_located(USER_NAME)
    )

    assert user_name.text == "User."

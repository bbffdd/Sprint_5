from selenium.webdriver.support import expected_conditions as ec

from constants import (
    BASE_URL,
)
from data import (
    USER_EMAIL,
    USER_PASSWORD,
)

from locators import (
    AD_BUTTON,
    EMAIL_INPUT,
    LOGIN_AND_REGISTRATION_BUTTON,
    LOGIN_BUTTON,
    PASSWORD_INPUT,
    USER_AVATAR_BUTTON,
    USER_NAME,
)


class TestLogin:
    def test_login_user(self, driver, wait):
        driver.get(BASE_URL)

        wait.until(
            ec.element_to_be_clickable(
                LOGIN_AND_REGISTRATION_BUTTON
            )
        ).click()

        wait.until(
            ec.visibility_of_element_located(EMAIL_INPUT)
        ).send_keys(USER_EMAIL)

        wait.until(
            ec.visibility_of_element_located(PASSWORD_INPUT)
        ).send_keys(USER_PASSWORD)

        wait.until(
            ec.element_to_be_clickable(LOGIN_BUTTON)
        ).click()

#Корректная конструкция элемента-маркера успеха
        assert wait.until(
            ec.visibility_of_element_located(AD_BUTTON)
        ).text.strip() == "Разместить объявление"

#Корректная конструкцмя элемента-маркера успеха
        # Проверяем наличие аватара пользователя
        assert wait.until(
            ec.visibility_of_element_located(USER_AVATAR_BUTTON)
        ).is_displayed()

        # Проверяем имя пользователя
        assert wait.until(
            ec.visibility_of_element_located(USER_NAME)
        ).text.strip() == "User."

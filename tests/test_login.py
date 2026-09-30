from selenium.webdriver.support import expected_conditions as ec

from constants import (
    BASE_URL,
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


def test_login_user(driver, wait):
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

    # Проверяем наличие кнопки размещения объявления
    ad_button = wait.until(
        ec.visibility_of_element_located(AD_BUTTON)
    )

    assert ad_button.is_displayed()
    assert ad_button.text.strip() == "Разместить объявление"

    # Проверяем наличие аватара пользователя
    avatar = wait.until(
        ec.visibility_of_element_located(USER_AVATAR_BUTTON)
    )

    assert avatar.is_displayed()

    # Проверяем имя пользователя
    user_name = wait.until(
        ec.visibility_of_element_located(USER_NAME)
    )

    assert user_name.text.strip() == "User."

from selenium.webdriver.support import expected_conditions as ec

from locators import (
    AD_BUTTON,
    BASE_URL,
    EMAIL_INPUT,
    LOGIN_AND_REGISTRATION_BUTTON,
    LOGIN_BUTTON,
    PASSWORD_INPUT,
    USER_AVATAR_BUTTON,
    USER_NAME,
)


def test_login_user(driver, wait, user_data):
    driver.get(BASE_URL)

    wait.until(
        ec.element_to_be_clickable(LOGIN_AND_REGISTRATION_BUTTON)
    ).click()

    wait.until(
        ec.visibility_of_element_located(EMAIL_INPUT)
    ).send_keys(user_data["email"])

    wait.until(
        ec.visibility_of_element_located(PASSWORD_INPUT)
    ).send_keys(user_data["password"])

    wait.until(
        ec.element_to_be_clickable(LOGIN_BUTTON)
    ).click()

    # Проверяем что мы на главной странице,  по уникальной кнопке
    ad_button = wait.until(
        ec.visibility_of_element_located(AD_BUTTON)
    )

    assert ad_button.is_displayed()
    assert ad_button.text.strip() == "Разместить объявление"

    # Проверяем аватар пользователя
    avatar = wait.until(
        ec.visibility_of_element_located(USER_AVATAR_BUTTON)
    )

    assert avatar.is_displayed()

    # Проверяем имя пользователя
    user_name = wait.until(
        ec.visibility_of_element_located(USER_NAME)
    )

    assert user_name.text.strip() == "User."

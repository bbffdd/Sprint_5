from selenium.webdriver.support import expected_conditions as ec

from locators import (
    BASE_URL,
    EMAIL_INPUT,
    LOGIN_AND_REGISTRATION_BUTTON,
    LOGIN_BUTTON,
    USER_AVATAR_BUTTON,
    LOGOUT_BUTTON,
    USER_NAME,
)



def test_logout_user(set_authorized_user, wait):
    # Открываем меню пользователя
    wait.until(
        ec.element_to_be_clickable(USER_AVATAR_BUTTON)
    ).click()

    # Нажимаем «Выйти»
    wait.until(
        ec.element_to_be_clickable(LOGOUT_BUTTON)
    ).click()

    # После выхода отображается кнопка «Вход и регистрация»
    wait.until(
        ec.visibility_of_element_located(LOGIN_AND_REGISTRATION_BUTTON)
    )

    assert set_authorized_user.find_element(
        *LOGIN_AND_REGISTRATION_BUTTON
    ).is_displayed()

    assert not set_authorized_user.find_elements(*USER_AVATAR_BUTTON)
    assert not set_authorized_user.find_elements(*USER_NAME)
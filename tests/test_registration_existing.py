from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec

from locators import (
    CREATE_ACCOUNT_BUTTON,
    EMAIL_ERROR_MESSAGE,
    EMAIL_INPUT,
    PASSWORD_INPUT,
    PASSWORD_REPEAT_INPUT,
)


RED_COLOR = "rgb(255, 105, 114)"


def test_registration_existing_user(registration_page, wait, user_data):
    # Заполняем Email существующего пользователя
    wait.until(
        ec.visibility_of_element_located(EMAIL_INPUT)
    ).send_keys(user_data["email"])

    # Заполняем пароль
    wait.until(
        ec.visibility_of_element_located(PASSWORD_INPUT)
    ).send_keys(user_data["password"])

    # Повторяем пароль
    wait.until(
        ec.visibility_of_element_located(PASSWORD_REPEAT_INPUT)
    ).send_keys(user_data["password"])

    # Нажимаем «Создать аккаунт»
    wait.until(
        ec.element_to_be_clickable(CREATE_ACCOUNT_BUTTON)
    ).click()

    # Проверяем сообщение «Ошибка» под полем Email
    error_message = wait.until(
        ec.visibility_of_element_located(EMAIL_ERROR_MESSAGE)
    )

    assert error_message.text == "Ошибка"

    # Проверяем, что поля Email, Пароль и Повторите пароль выделены красным цветом
    for field_locator in (
        EMAIL_INPUT,
        PASSWORD_INPUT,
        PASSWORD_REPEAT_INPUT,
    ):
        field = wait.until(
            ec.visibility_of_element_located(field_locator)
        )

        parent = field.find_element(
            By.XPATH,
            "./parent::div[starts-with(@class, 'input_inputError')]",
        )

        assert parent.value_of_css_property(
            "border-color"
        ) == RED_COLOR

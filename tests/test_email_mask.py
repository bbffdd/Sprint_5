from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec

from locators import (
    CREATE_ACCOUNT_BUTTON,
    EMAIL_ERROR_MESSAGE,
    EMAIL_INPUT,
    PASSWORD_INPUT,
    PASSWORD_REPEAT_INPUT,
    EMAIL_ERROR_MESSAGE,
    NO_ACCOUNT_BUTTON,
)


RED_COLOR = "rgb(255, 105, 114)"


def test_registration_with_invalid_email(registration_page, wait):
    # Вводим Email, который не соответствует маске
    wait.until(
        ec.visibility_of_element_located(EMAIL_INPUT)
    ).send_keys("nodog")

    # Нажимаем «Создать аккаунт»
    wait.until(
        ec.element_to_be_clickable(CREATE_ACCOUNT_BUTTON)
    ).click()

    # Проверяем сообщение об ошибке под Email
    error_message = wait.until(
        ec.visibility_of_element_located(EMAIL_ERROR_MESSAGE)
    )

    assert error_message.text == "Ошибка"

    # Проверяем красную рамку родителя каждого поля
    for field_locator in (EMAIL_INPUT, PASSWORD_INPUT,PASSWORD_REPEAT_INPUT):
        field = registration_page.find_element(*field_locator)

        parent = field.find_element(
            By.XPATH,
            "./parent::div[starts-with(@class, 'input_inputError')]",
        )

        assert parent.value_of_css_property(
            "border-color"
        ) == RED_COLOR

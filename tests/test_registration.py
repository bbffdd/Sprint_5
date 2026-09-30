from selenium.webdriver.support import expected_conditions as ec

from constants import (
    ELEMENT_ERROR_COLOUR,
    INCORRECT_EMAIL,
    REGISTRATION_PASSWORD,
    USER_EMAIL,
)

from locators import (
    CREATE_ACCOUNT_BUTTON,
    EMAIL_ERROR_MESSAGE,
    EMAIL_INPUT,
    ERROR_INPUT_PARENT,
    PASSWORD_INPUT,
    PASSWORD_REPEAT_INPUT,
    USER_AVATAR_BUTTON,
    USER_NAME,
)


def fill_registration_form(wait, email, password):
    wait.until(
        ec.visibility_of_element_located(EMAIL_INPUT)
    ).send_keys(email)

    wait.until(
        ec.visibility_of_element_located(PASSWORD_INPUT)
    ).send_keys(password)

    wait.until(
        ec.visibility_of_element_located(PASSWORD_REPEAT_INPUT)
    ).send_keys(password)


class TestRegistration:

    def test_registration_with_valid_data(
        self,
        registration_page,
        wait,
        registration_email,
    ):
        fill_registration_form(
            wait=wait,
            email=registration_email,
            password=REGISTRATION_PASSWORD,
        )

        wait.until(
            ec.element_to_be_clickable(CREATE_ACCOUNT_BUTTON)
        ).click()

        wait.until(
            ec.visibility_of_element_located(USER_AVATAR_BUTTON)
        )

        user_name = wait.until(
            ec.visibility_of_element_located(USER_NAME)
        )

        assert user_name.is_displayed()
        assert user_name.text.strip() != ""

    def test_registration_existing_user(
        self,
        registration_page,
        wait,
    ):
        fill_registration_form(
            wait=wait,
            email=USER_EMAIL,
            password=REGISTRATION_PASSWORD,
        )

        wait.until(
            ec.element_to_be_clickable(CREATE_ACCOUNT_BUTTON)
        ).click()

        error_message = wait.until(
            ec.visibility_of_element_located(EMAIL_ERROR_MESSAGE)
        )

        assert error_message.text == "Ошибка"

        self._assert_registration_fields_have_error(
            wait
        )

    def test_registration_with_invalid_email(
        self,
        registration_page,
        wait,
    ):
        wait.until(
            ec.visibility_of_element_located(EMAIL_INPUT)
        ).send_keys(INCORRECT_EMAIL)

        wait.until(
            ec.element_to_be_clickable(CREATE_ACCOUNT_BUTTON)
        ).click()

        error_message = wait.until(
            ec.visibility_of_element_located(EMAIL_ERROR_MESSAGE)
        )

        assert error_message.text == "Ошибка"

        self._assert_registration_fields_have_error(
            wait
        )

    @staticmethod
    def _assert_registration_fields_have_error(wait):
        for field_locator in (
            EMAIL_INPUT,
            PASSWORD_INPUT,
            PASSWORD_REPEAT_INPUT,
        ):
            field = wait.until(
                ec.visibility_of_element_located(field_locator)
            )

            parent = field.find_element(*ERROR_INPUT_PARENT)

            actual_border_colour = (
                parent.value_of_css_property("border-color")
            )

            assert actual_border_colour == ELEMENT_ERROR_COLOUR

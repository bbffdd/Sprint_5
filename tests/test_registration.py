from selenium.webdriver.support import expected_conditions as ec

from data import (
    INCORRECT_EMAIL,
    REGISTRATION_PASSWORD,
    USER_EMAIL,
    ELEMENT_ERROR_COLOUR,
)

from locators import (
    CREATE_ACCOUNT_BUTTON,
    ERROR_INPUT_PARENT,
    EMAIL_ERROR_MESSAGE,
    EMAIL_INPUT,
    PASSWORD_INPUT,
    PASSWORD_REPEAT_INPUT,
    USER_AVATAR_BUTTON,
    USER_NAME,
)


class TestRegistration:

    def test_registration_with_valid_data(
        self,
        registration_page,
        wait,
        registration_email,
        fill_registration_form,
    ):
        fill_registration_form(
            email=registration_email,
            password=REGISTRATION_PASSWORD,
        )

        wait.until(
            ec.element_to_be_clickable(CREATE_ACCOUNT_BUTTON)
        ).click()

        assert wait.until(
            ec.visibility_of_element_located(USER_AVATAR_BUTTON)
        ).is_displayed()

        assert wait.until(
            ec.visibility_of_element_located(USER_NAME)
        ).text.strip() != ""

    def test_registration_existing_user(
        self,
        registration_page,
        wait,
        fill_registration_form,
    ):
        fill_registration_form(
            email=USER_EMAIL,
            password=REGISTRATION_PASSWORD,
        )

        wait.until(
            ec.element_to_be_clickable(CREATE_ACCOUNT_BUTTON)
        ).click()

        assert wait.until(
            ec.visibility_of_element_located(EMAIL_ERROR_MESSAGE)
        ).text == "Ошибка"

        for field_locator in (
            EMAIL_INPUT,
            PASSWORD_INPUT,
            PASSWORD_REPEAT_INPUT,
        ):
            field = wait.until(
                ec.visibility_of_element_located(field_locator)
            )

            parent = field.find_element(*ERROR_INPUT_PARENT)

            assert (
                parent.value_of_css_property("border-color")
                == ELEMENT_ERROR_COLOUR
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

        assert wait.until(
            ec.visibility_of_element_located(EMAIL_ERROR_MESSAGE)
        ).text == "Ошибка"

        for field_locator in (
            EMAIL_INPUT,
            PASSWORD_INPUT,
            PASSWORD_REPEAT_INPUT,
        ):
            field = wait.until(
                ec.visibility_of_element_located(field_locator)
            )

            parent = field.find_element(*ERROR_INPUT_PARENT)

            assert (
                parent.value_of_css_property("border-color")
                == ELEMENT_ERROR_COLOUR
            )

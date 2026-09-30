from selenium.webdriver.support import expected_conditions as ec

from locators import (
    LOGIN_AND_REGISTRATION_BUTTON,
    LOGOUT_BUTTON,
    USER_AVATAR_BUTTON,
    USER_NAME,
)


class TestLogout:

    def test_logout_user(
        self,
        set_authorized_user,
        wait,
    ):
        wait.until(
            ec.element_to_be_clickable(USER_AVATAR_BUTTON)
        ).click()

        wait.until(
            ec.element_to_be_clickable(LOGOUT_BUTTON)
        ).click()

        login_button = wait.until(
            ec.visibility_of_element_located(
                LOGIN_AND_REGISTRATION_BUTTON
            )
        )

        assert login_button.is_displayed()

        assert not set_authorized_user.find_elements(
            *USER_AVATAR_BUTTON
        )

        assert not set_authorized_user.find_elements(
            *USER_NAME
        )

import pytest

from selenium import webdriver
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait

from locators import (
    AD_TITLES,
    BASE_URL,
    EMAIL_INPUT,
    LOGIN_AND_REGISTRATION_BUTTON,
    LOGIN_BUTTON,
    MY_ADS_TITLE,
    NEXT_ADS_PAGE_BUTTON,
    NO_ACCOUNT_BUTTON,
    PASSWORD_INPUT,
    PROFILE_URL,
    USER_AVATAR_BUTTON,
)


@pytest.fixture
def driver():
    browser = webdriver.Chrome()
    browser.maximize_window()

    yield browser

    browser.quit()


@pytest.fixture
def wait(driver):
    return WebDriverWait(driver, 15)


@pytest.fixture
def registration_page(driver, wait):
    driver.get(BASE_URL)

    wait.until(
        ec.element_to_be_clickable(
            LOGIN_AND_REGISTRATION_BUTTON
        )
    ).click()

    wait.until(
        ec.element_to_be_clickable(NO_ACCOUNT_BUTTON)
    ).click()

    return driver


@pytest.fixture
def user_data():
    return {
        "email": "tester@account2.gov",
        "password": "govgov123",
    }


@pytest.fixture
def set_authorized_user(driver, wait, user_data):
    driver.get(BASE_URL)

    wait.until(
        ec.element_to_be_clickable(
            LOGIN_AND_REGISTRATION_BUTTON
        )
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

    wait.until(
        ec.visibility_of_element_located(USER_AVATAR_BUTTON)
    )

    return driver


@pytest.fixture
def get_all_ad_titles(driver, wait):
    def collect_titles():
        driver.get(PROFILE_URL)

        wait.until(
            ec.visibility_of_element_located(MY_ADS_TITLE)
        )

        all_ad_titles = []

        while True:
            current_ad_titles = wait.until(
                ec.presence_of_all_elements_located(AD_TITLES)
            )

            all_ad_titles.extend(
                title.text.strip()
                for title in current_ad_titles
                if title.text.strip()
            )

            next_page_buttons = driver.find_elements(
                *NEXT_ADS_PAGE_BUTTON
            )

            if not next_page_buttons:
                break

            next_page_button = next_page_buttons[0]

            if (
                next_page_button.get_attribute("disabled")
                is not None
                or next_page_button.get_attribute(
                    "aria-disabled"
                ) == "true"
            ):
                break

            previous_first_title = current_ad_titles[0]

            next_page_button.click()

            wait.until(
                ec.staleness_of(previous_first_title)
            )

        return list(dict.fromkeys(all_ad_titles))

    return collect_titles

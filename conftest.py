import time
import uuid

import pytest
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait

from constants import (
    BASE_URL,
    PROFILE_URL,
)

from data import (
    USER_EMAIL,
    USER_PASSWORD,
    ELEMENT_ERROR_COLOUR,
)

from locators import (
    AD_TITLES,
    EMAIL_INPUT,
    ERROR_INPUT_PARENT,
    LOGIN_AND_REGISTRATION_BUTTON,
    LOGIN_BUTTON,
    MY_ADS_TITLE,
    NEXT_ADS_PAGE_BUTTON,
    NO_ACCOUNT_BUTTON,
    PASSWORD_INPUT,
    PASSWORD_REPEAT_INPUT,
    USER_AVATAR_BUTTON,
)


@pytest.fixture
def driver():
    start = time.time()
    print("\nСоздание Chrome")

    browser = webdriver.Chrome()

    print(f"Chrome запущен за {time.time() - start:.2f} сек")

    browser.set_page_load_timeout(5)
    browser.set_script_timeout(5)
    browser.implicitly_wait(0)

    yield browser

    start = time.time()
    browser.quit()
    print(f"Chrome закрыт за {time.time() - start:.2f} сек")


@pytest.fixture
def wait(driver):
    return WebDriverWait(driver, 3)


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
def set_authorized_user(driver, wait):
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
            current_ad_titles = driver.find_elements(*AD_TITLES)

            for title in current_ad_titles:
                title_text = title.text.strip()

                if title_text:
                    all_ad_titles.append(title_text)

            next_page_buttons = driver.find_elements(
                *NEXT_ADS_PAGE_BUTTON
            )

            if not next_page_buttons:
                break

            next_page_button = next_page_buttons[0]

            is_disabled = (
                next_page_button.get_attribute("disabled") is not None
                or next_page_button.get_attribute("aria-disabled") == "true"
            )

            if is_disabled:
                break

            previous_first_title = (
                current_ad_titles[0]
                if current_ad_titles
                else None
            )

            next_page_button.click()

            if previous_first_title:
                wait.until(
                    ec.staleness_of(previous_first_title)
                )

        return list(dict.fromkeys(all_ad_titles))

    return collect_titles



@pytest.fixture
def get_error_field_parent():
    def find_parent(field):
        return field.find_element(*ERROR_INPUT_PARENT)

    return find_parent


@pytest.fixture
def registration_email():
    return f"user_{uuid.uuid4().hex}@testik.ru"


@pytest.fixture
def ad_name():
    return f"test-{uuid.uuid4().hex[:8]}"

#добавлена фикстура заполнения формы регистрации теста регистрации
@pytest.fixture
def fill_registration_form(wait):
    def fill_form(email, password):
        wait.until(
            ec.visibility_of_element_located(EMAIL_INPUT)
        ).send_keys(email)

        wait.until(
            ec.visibility_of_element_located(PASSWORD_INPUT)
        ).send_keys(password)

        wait.until(
            ec.visibility_of_element_located(PASSWORD_REPEAT_INPUT)
        ).send_keys(password)

    return fill_form

@pytest.fixture
def has_error_border():
    def create_check(field_locator):
        def check_border(driver):
            field = driver.find_element(*field_locator)

            parent = field.find_element(*ERROR_INPUT_PARENT)

            return (
                parent.value_of_css_property("border-color")
                == ELEMENT_ERROR_COLOUR
            )

        return check_border

    return create_check
from selenium.webdriver.support import expected_conditions as ec

from locators import (
    AD_BUTTON,
    AD_AUTHORIZATION_TITLE,
    BASE_URL,
)


def test_create_ad_by_unauthorized_user(driver, wait):
    driver.get(BASE_URL)

    wait.until(
        ec.element_to_be_clickable(AD_BUTTON)
    ).click()

    modal_title = wait.until(
        ec.visibility_of_element_located(AD_AUTHORIZATION_TITLE)
    )

    assert modal_title.text == (
        "Чтобы разместить объявление, авторизуйтесь"
    )

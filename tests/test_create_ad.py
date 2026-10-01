from selenium.webdriver.support import expected_conditions as ec

from constants import (
    BASE_URL,
)

from data import (
    AD_DESCRIPTION,
    AD_PRICE,
)

from locators import (
    AD_AUTHORIZATION_TITLE,
    AD_BUTTON,
    AD_CATEGORY_BUTTON,
    AD_CATEGORY_OPTION,
    AD_CITY_BUTTON,
    AD_CITY_OPTION,
    AD_CONDITION_NEW_INPUT,
    AD_CONDITION_NEW_LABEL,
    AD_DESCRIPTION_INPUT,
    AD_NAME_INPUT,
    AD_PRICE_INPUT,
    AD_PUBLISH_BUTTON,
)


class TestCreateAd:

    def test_create_ad_by_unauthorized_user(
        self,
        driver,
        wait,
    ):
        driver.get(BASE_URL)

        wait.until(
            ec.element_to_be_clickable(AD_BUTTON)
        ).click()

# Поправлен ассерт 
        assert wait.until(
            ec.visibility_of_element_located(AD_AUTHORIZATION_TITLE)
        ).text.strip() == (
            "Чтобы разместить объявление, авторизуйтесь"
        )


def test_create_ad_authorized_user(
    set_authorized_user,
    wait,
    get_all_ad_titles,
    ad_name,
):
    wait.until(
        ec.element_to_be_clickable(AD_BUTTON)
    ).click()

    wait.until(
        ec.visibility_of_element_located(AD_NAME_INPUT)
    ).send_keys(ad_name)

    wait.until(
        ec.visibility_of_element_located(AD_DESCRIPTION_INPUT)
    ).send_keys(AD_DESCRIPTION)

    wait.until(
        ec.visibility_of_element_located(AD_PRICE_INPUT)
    ).send_keys(AD_PRICE)

    wait.until(
        ec.element_to_be_clickable(AD_CATEGORY_BUTTON)
    ).click()

    wait.until(
        ec.element_to_be_clickable(AD_CATEGORY_OPTION)
    ).click()

    wait.until(
        ec.element_to_be_clickable(AD_CITY_BUTTON)
    ).click()

    wait.until(
        ec.element_to_be_clickable(AD_CITY_OPTION)
    ).click()

    wait.until(
        ec.element_to_be_clickable(AD_CONDITION_NEW_LABEL)
    ).click()

    wait.until(
        ec.element_located_to_be_selected(
            AD_CONDITION_NEW_INPUT
        )
    )

    wait.until(
        ec.element_to_be_clickable(AD_PUBLISH_BUTTON)
    ).click()

    assert wait.until(
        lambda _: ad_name in get_all_ad_titles()
    )

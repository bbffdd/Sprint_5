import uuid

from selenium.webdriver.support import expected_conditions as ec

from locators import (
    AD_BUTTON,
    AD_CATEGORY_BUTTON,
    AD_CONDITION_NEW_INPUT,
    AD_CONDITION_NEW_LABEL,
    AD_DESCRIPTION_INPUT,
    AD_NAME_INPUT,
    AD_PRICE_INPUT,
    AD_PUBLISH_BUTTON,
    AD_CITY_BUTTON,
    AD_CATEGORY_OPTION,
    AD_CITY_OPTION,
)


def test_create_ad_authorized_user(
    set_authorized_user,
    wait,
    get_all_ad_titles,
):
    ad_name = f"test-{uuid.uuid4().hex[:8]}"

    wait.until(
        ec.element_to_be_clickable(AD_BUTTON)
    ).click()

    wait.until(
        ec.visibility_of_element_located(AD_NAME_INPUT)
    ).send_keys(ad_name)

    wait.until(
        ec.visibility_of_element_located(AD_DESCRIPTION_INPUT)
    ).send_keys("Тестовое описание товара")

    wait.until(
        ec.visibility_of_element_located(AD_PRICE_INPUT)
    ).send_keys("1123")

    wait.until(
        ec.element_to_be_clickable(AD_CATEGORY_BUTTON)
    ).click()

    wait.until(
        ec.element_to_be_clickable(
            AD_CATEGORY_OPTION
        )
    ).click()

    wait.until(
        ec.element_to_be_clickable(AD_CITY_BUTTON)
    ).click()

    wait.until(
        ec.element_to_be_clickable(
            AD_CITY_OPTION
        )
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

    actual_ad_titles = get_all_ad_titles()
    expected_ad_title = ad_name

    assert expected_ad_title in actual_ad_titles

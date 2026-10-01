from selenium.webdriver.common.by import By


LOGIN_AND_REGISTRATION_BUTTON = (
    By.XPATH,
    "//button[contains(normalize-space(.), 'Вход и регистрация')]",
)

LOGIN_BUTTON = (
    By.XPATH,
    "//button[@type='submit' and normalize-space(.)='Войти']",
)

LOGOUT_BUTTON = (
    By.XPATH,
    "//button[@type='button' "
    "and contains(@class, 'btnSmall') "
    "and normalize-space(.)='Выйти']",
)

NO_ACCOUNT_BUTTON = (
    By.XPATH,
    "//button[contains(normalize-space(.), 'Нет аккаунта')]",
)

CREATE_ACCOUNT_BUTTON = (
    By.XPATH,
    "//button[@type='submit' and normalize-space(.)='Создать аккаунт']",
)

EMAIL_INPUT = (
    By.CSS_SELECTOR,
    "input[name='email']",
)

PASSWORD_INPUT = (
    By.CSS_SELECTOR,
    "input[name='password']",
)

PASSWORD_REPEAT_INPUT = (
    By.CSS_SELECTOR,
    "input[name='submitPassword']",
)

USER_NAME = (
    By.CSS_SELECTOR,
    "h3.profileText.name",
)

USER_AVATAR_BUTTON = (
    By.CSS_SELECTOR,
    "button.circleSmall",
)

EMAIL_ERROR_MESSAGE = (
    By.XPATH,
    "//*[normalize-space(.)='Ошибка']",
)

ERROR_INPUT_PARENT = (
    By.XPATH,
    "./parent::div[starts-with(@class, 'input_inputError')]",
)

AD_AUTHORIZATION_TITLE = (
    By.CSS_SELECTOR,
    "h1.h1",
)

AD_BUTTON = (
    By.XPATH,
    "//button[@type='button' "
    "and normalize-space(.)='Разместить объявление']",
)

AD_NAME_INPUT = (
    By.CSS_SELECTOR,
    "input[name='name'][placeholder='Название']",
)

AD_DESCRIPTION_INPUT = (
    By.CSS_SELECTOR,
    "textarea[name='description'][placeholder='Описание товара']",
)

AD_PRICE_INPUT = (
    By.CSS_SELECTOR,
    "input[name='price'][placeholder='Стоимость']",
)

AD_CATEGORY_BUTTON = (
    By.XPATH,
    "//input[@name='category']/parent::*//button",
)

AD_CITY_BUTTON = (
    By.XPATH,
    "//input[@name='city']/parent::*//button",
)

AD_CONDITION_NEW_LABEL = (
    By.XPATH,
    "//fieldset[.//h3[normalize-space()='Состояние товара:']]"
    "//label[normalize-space()='Новый']",
)

AD_CONDITION_NEW_INPUT = (
    By.XPATH,
    "//input[@name='condition' and @value='Новый']",
)

AD_PUBLISH_BUTTON = (
    By.CSS_SELECTOR,
    "button[type='submit'].buttonPrimary",
)

MY_ADS_TITLE = (
    By.XPATH,
    "//h1[normalize-space()='Мои объявления']",
)

AD_TITLES = (
    By.XPATH,
    "//div[contains(@class, 'card')]"
    "//div[contains(@class, 'about')]/h2",
)

NEXT_ADS_PAGE_BUTTON = (
    By.CSS_SELECTOR,
    "button.arrowButton--right",
)

AD_CATEGORY_OPTION = (
    By.XPATH,
    "//*[normalize-space(.)='Технологии']",
)

AD_CITY_OPTION = (
    By.XPATH,
    "//*[normalize-space(.)='Новосибирск']",
)

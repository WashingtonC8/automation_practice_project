import pytest
from ui.page_static import main_page_static
from ui.page_static import login_page_static
from ui.pages.login_page import LoginPage
from ui.pages.main_page import MainPage
from ui.pages.account_created_page import AccountCreatedPage
from ui.pages.signup_page import SignupPage
from ui.pages.account_delete_page import AccountDeletePage
from data.fixtures.generate_user_data_fixtures import generate_user_data
from data.fixtures.generate_adress_information_data_fixtures import generate_address_information_data


@pytest.fixture(scope='function')
def setup(browser, generate_user_data, generate_address_information_data):
    login_page = LoginPage(browser, url=login_page_static.LOGIN_PAGE_URL)  # инициализируем главную регистрации
    login_page.open()  # открываем браузер
    login_page.should_be_login_page()  # набор проверок того, что открыта страница логина
    user_data = generate_user_data  # получение словаря со сгенерированными данными
    login_page.enter_name_and_email_to_sign_up_form_test(user_data)  # ввод name и email на странице
    login_page.click_sign_up_form_button()  # клик по кнопке "signup"
    signup_page = SignupPage(browser, browser.current_url)  # инициализация открытой страницы регистрации
    signup_page.should_be_enter_account_information_is_visible()  # Надпись "ENTER ACCOUNT INFORMATION" видна
    signup_page.fill_details_enter_account_information(user_data)  # Заполняем информацию о пользователе
    signup_page.select_newsletter_checkbox()  # Установить чек-бокс рассылки
    signup_page.select_offers_from_partners_checkbox()  # Установить чек-бокс партнерам
    address_information = generate_address_information_data  # получение словаря со сгенерированными данными
    signup_page.fill_details_enter_address_information(address_information)  # Заполняем данные полей адреса
    signup_page.click_create_account_button()  # клик по кнопке "создать аккаунт"
    account_created_page = AccountCreatedPage(browser, browser.current_url)  # инициализация открытой страницы
    # успешного создания аккаунта
    account_created_page.should_be_account_created_is_visible()  # Надпись "ACCOUNT CREATED" видна
    account_created_page.click_continue_button()  # клик по кнопке "continue"
    page = MainPage(browser, browser.current_url)  # инициализируем главную страницу
    page.should_be_expected_name(user_data)  # сравниваем имя в хедере "logged in ..." с именем при регистрации
    page.click_to_logout_link()  # выходим из аккаунта
    yield


@pytest.fixture(scope='function')
def teardown(browser):
    yield
    page = MainPage(browser, browser.current_url)
    page.click_to_delete_account_link()  # нажать на кнопку удаления аккаунта
    account_deleted_page = AccountDeletePage(browser, browser.current_url)  # инициализируем страницу удаления аккаунта
    account_deleted_page.should_be_account_deleted_is_visible()  # проверка наличия надписи о том, что акк удален


@pytest.fixture(scope='function')
def teardown_after_logout(browser, generate_user_data):
    yield
    page = MainPage(browser, url=main_page_static.MAIN_PAGE_URL)  # инициализируем главную страницу
    page.open()  # открываем браузер
    page.should_be_main_page()  # набор проверок того, что открыта главная
    page.go_to_login_page()  # метод перехода на страницу регистрации
    login_page = LoginPage(browser, browser.current_url)  # инициализация открытой страницы логина
    login_page.should_be_login_page()  # набор проверок того, что открыта страница логина
    user_data = generate_user_data  # получение словаря со сгенерированными данными
    login_page.enter_name_and_email_to_login_form(user_data)  # вводим данные ранее зарегистрированного пользователя
    login_page.click_login_form_button()  # клик по кнопке "Login"
    page = MainPage(browser, browser.current_url)  # инициализируем главную страницу
    page.should_be_expected_name(user_data)  # сравниваем имя в хедере "logged in ..." с именем при регистрации
    page.click_to_delete_account_link()  # нажать на кнопку удаления аккаунта
    account_deleted_page = AccountDeletePage(browser, browser.current_url)  # инициализируем страницу удаления аккаунта
    account_deleted_page.should_be_account_deleted_is_visible()  # проверка наличия надписи о том, что акк удален


@pytest.mark.usefixtures("teardown")
def test_register_user(browser, generate_user_data, generate_address_information_data):
    page = MainPage(browser, url=main_page_static.MAIN_PAGE_URL)  # инициализируем главную страницу
    page.open()  # открываем браузер
    page.should_be_main_page()  # набор проверок того, что открыта главная
    page.go_to_login_page()  # метод перехода на страницу регистрации
    login_page = LoginPage(browser, browser.current_url)  # инициализация открытой страницы логина
    login_page.should_be_login_page()  # набор проверок того, что открыта страница логина
    user_data = generate_user_data  # получение словаря со сгенерированными данными
    login_page.enter_name_and_email_to_sign_up_form_test(user_data)  # ввод name и email на странице
    login_page.click_sign_up_form_button()  # клик по кнопке "signup"
    signup_page = SignupPage(browser, browser.current_url)  # инициализация открытой страницы регистрации
    signup_page.should_be_enter_account_information_is_visible()  # Надпись "ENTER ACCOUNT INFORMATION" видна
    signup_page.fill_details_enter_account_information(user_data)  # Заполняем информацию о пользователе
    signup_page.select_newsletter_checkbox()  # Установить чек-бокс рассылки
    signup_page.select_offers_from_partners_checkbox()  # Установить чек-бокс партнерам
    address_information = generate_address_information_data  # получение словаря со сгенерированными данными
    signup_page.fill_details_enter_address_information(address_information)  # Заполняем данные полей адреса
    signup_page.click_create_account_button()  # клик по кнопке "создать аккаунт"
    account_created_page = AccountCreatedPage(browser, browser.current_url)  # инициализация открытой страницы
    # успешного создания аккаунта
    account_created_page.should_be_account_created_is_visible()  # Надпись "ACCOUNT CREATED" видна
    account_created_page.click_continue_button()  # клик по кнопке "continue"
    page = MainPage(browser, browser.current_url)  # инициализируем главную страницу
    page.should_be_expected_name(user_data)  # сравниваем имя в хедере "logged in ..." с именем при регистрации


@pytest.mark.usefixtures("setup", "teardown")
def test_login_user_with_correct_email_and_password(browser, generate_user_data):
    page = MainPage(browser, url=main_page_static.MAIN_PAGE_URL)  # инициализируем главную страницу
    page.open()  # открываем браузер
    page.should_be_main_page()  # набор проверок того, что открыта главная
    page.go_to_login_page()  # метод перехода на страницу регистрации
    login_page = LoginPage(browser, browser.current_url)  # инициализация открытой страницы логина
    login_page.should_be_login_page()  # набор проверок того, что открыта страница логина
    user_data = generate_user_data  # получение словаря со сгенерированными данными
    login_page.enter_name_and_email_to_login_form(user_data)  # вводим данные ранее зарегистрированного пользователя
    login_page.click_login_form_button()  # клик по кнопке "Login"
    page = MainPage(browser, browser.current_url)  # инициализируем главную страницу
    page.should_be_expected_name(user_data)  # сравниваем имя в хедере "logged in ..." с именем при регистрации


def test_login_user_with_incorrect_email_and_password(browser, generate_user_data):
    page = MainPage(browser, url=main_page_static.MAIN_PAGE_URL)  # инициализируем главную страницу
    page.open()  # открываем браузер
    page.should_be_main_page()  # набор проверок того, что открыта главная
    page.go_to_login_page()  # метод перехода на страницу регистрации
    login_page = LoginPage(browser, browser.current_url)  # инициализация открытой страницы логина
    login_page.should_be_login_page()  # набор проверок того, что открыта страница логина
    user_data = generate_user_data  # получение словаря со сгенерированными данными
    login_page.enter_name_and_email_to_login_form(user_data)  # вводим данные ранее зарегистрированного
    # пользователя
    login_page.click_login_form_button()  # клик по кнопке "Login"
    login_page.should_be_incorrect_email_login_form_error()  # проверка наличия ошибки о вводе некорректного email


@pytest.mark.usefixtures("setup", "teardown_after_logout")
def test_logout_user(browser, generate_user_data):
    page = MainPage(browser, url=main_page_static.MAIN_PAGE_URL)  # инициализируем главную страницу
    page.open()  # открываем браузер
    page.should_be_main_page()  # набор проверок того, что открыта главная
    page.go_to_login_page()  # метод перехода на страницу регистрации
    login_page = LoginPage(browser, browser.current_url)  # инициализация открытой страницы логина
    login_page.should_be_login_page()  # набор проверок того, что открыта страница логина
    user_data = generate_user_data  # получение словаря со сгенерированными данными
    login_page.enter_name_and_email_to_login_form(user_data)  # вводим данные ранее зарегистрированного пользователя
    login_page.click_login_form_button()  # клик по кнопке "Login"
    page = MainPage(browser, browser.current_url)  # инициализируем главную страницу
    page.should_be_expected_name(user_data)  # сравниваем имя в хедере "logged in ..." с именем при регистрации
    page.click_to_logout_link()  # выходим из аккаунта
    login_page = LoginPage(browser, browser.current_url)  # инициализация открытой страницы логина
    login_page.should_be_login_page()  # набор проверок того, что открыта страница логина


@pytest.mark.usefixtures("setup")
def test_register_user_with_existing_email(browser, generate_user_data):
    page = MainPage(browser, url=main_page_static.MAIN_PAGE_URL)  # инициализируем главную страницу
    page.open()  # открываем браузер
    page.should_be_main_page()  # набор проверок того, что открыта главная
    page.go_to_login_page()  # метод перехода на страницу регистрации
    login_page = LoginPage(browser, browser.current_url)  # инициализация открытой страницы логина
    login_page.should_be_login_page()  # набор проверок того, что открыта страница логина
    user_data = generate_user_data  # получение словаря со сгенерированными данными
    login_page.enter_name_and_email_to_sign_up_form_test(user_data)  # ввод name и email на странице
    login_page.click_sign_up_form_button()  # клик по кнопке "signup"
    signup_page = SignupPage(browser, browser.current_url) # инициализация открытой страницы регистрации
    signup_page.should_be_email_already_exist_signup_form_error() # проверка наличия ошибки о вводе существующего email
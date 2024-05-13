import time
import pytest
from pages.variables import Pages
from pages.login_page import LoginPage
from pages.main_page import MainPage
from pages.account_created_page import AccountCreatedPage
from pages.signup_page import SignupPage
from pages.account_delete_page import AccountDeletePage
from fixtures.generate_user_data_fixtures import generate_user_data, generate_address_information_data


@pytest.fixture(scope='function')
def teardown(browser):
    yield
    page = MainPage(browser, browser.current_url)
    page.click_to_delete_account_link() # нажать на кнопку удаления аккаунта
    account_deleted_page = AccountDeletePage(browser, browser.current_url) # инициализируем страницу удаления аккаунта
    account_deleted_page.should_be_account_deleted_is_visible() # проверка наличия надписи о том, что акк удален


@pytest.mark.usefixtures("teardown")
def test_register_user(browser,generate_user_data, generate_address_information_data):
    page = MainPage(browser, url=Pages.MAIN_PAGE_URL) # инициализируем главную страницу
    page.open() # открываем браузер
    page.should_be_main_page() # набор проверок того, что открыта главная
    page.go_to_login_page() # метод перехода на страницу регистрации
    login_page = LoginPage(browser, browser.current_url) # инициализация открытой страницы логина
    login_page.should_be_login_page() # набор проверок того, что открыта страница логина
    user_data = generate_user_data # получение словаря со сгенерированными данными
    login_page.enter_name_and_email_to_sign_up_form(user_data) # ввод name и email на странице
    login_page.click_sign_up_form_button() # клик по кнопке "signup"
    signup_page = SignupPage(browser, browser.current_url) # инициализация открытой страницы регистрации
    signup_page.should_be_enter_account_information_is_visible() # Надпись "ENTER ACCOUNT INFORMATION" видна
    signup_page.fill_details_enter_account_information(user_data) # Заполняем информацию о пользователе
    signup_page.select_newsletter_checkbox() # Установить чек-бокс рассылки
    signup_page.select_offers_from_partners_checkbox() # Установить чек-бокс партнерам
    address_information = generate_address_information_data # получение словаря со сгенерированными данными
    signup_page.fill_details_enter_address_information(address_information) # Заполняем данные полей адреса
    signup_page.click_create_account_button() # клик по кнопке "создать аккаунт"
    account_created_page = AccountCreatedPage(browser, browser.current_url) # инициализация открытой страницы
                                                                            # успешного создания аккаунта
    account_created_page.should_be_account_created_is_visible() # Надпись "ACCOUNT CREATED" видна
    account_created_page.click_continue_button() # клик по кнопке "continue"
    page = MainPage(browser, browser.current_url) # инициализируем главную страницу
    page.should_be_expected_name(user_data) # сравниваем имя в хедере "logged in ..." с именем при регистрации


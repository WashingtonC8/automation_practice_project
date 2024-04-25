import time

from pages.variables import Pages
from pages.login_page import LoginPage
from pages.main_page import MainPage
from pages.base_page import BasePage
from pages.signup_page import SignupPage


def test_register_user(browser,generate_user_data, generate_address_information_data):
    page = MainPage(browser, url=Pages.MAIN_PAGE_URL) # инициализируем страницу
    page.open() # открываем браузер
    page.should_be_main_page() # набор проверок того, что открыта главная
    page.go_to_login_page() # метод перехода на страницу регистрации
    login_page = LoginPage(browser, browser.current_url) # инициализация открытой страницы логина
    login_page.should_be_login_page() # набор проверок того, что открыта страница логина
    user_data = generate_user_data # получение списка со сгенерированными данными
    login_page.enter_name_and_email_to_sign_up_form(user_data["name"],
                                                    user_data["email"]) # ввод name и email на странице
    login_page.click_sign_up_form_button() # клик по кнопке "signup"
    signup_page = SignupPage(browser, browser.current_url) # инициализация открытой страницы регистрации
    signup_page.should_be_enter_account_information_is_visible() # Надпись "ENTER ACCOUNT INFORMATION" видна
    signup_page.fill_details_enter_account_information(user_data["title"],
                                                       user_data["password"],
                                                       user_data["day_of_birth"],
                                                       user_data["month_of_birth"],
                                                       user_data["year_of_birth"]) # Заполняем информацию о пользователе


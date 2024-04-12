from pages.variables import Pages
from pages.login_page import LoginPage
from pages.main_page import MainPage
from pages.base_page import BasePage


def test_register_user(browser):
    page = MainPage(browser, url=Pages.MAIN_PAGE_URL) # инициализируем страницу
    page.open() # открываем браузер
    page.should_be_main_page() # набор проверок того. что открыта главная
    page.go_to_login_page() # метод перехода на страницу регистрации
    login_page = LoginPage(browser, browser.current_url) # инициализация открытой страницы егистрации
    login_page.should_be_login_page() # набор проверок того. что открыта страница логина


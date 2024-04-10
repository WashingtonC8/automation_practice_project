from pages.variables import Pages
from pages.login_page import LoginPage
import pytest


def test_register_user(browser):
    page = LoginPage(browser, url=Pages.MAIN_PAGE_URL)
    page.open()
from .base_page import BasePage
from pages.variables import Pages
from pages.variables import Titles
from .locators import MainPageLocators


class MainPage(BasePage):
    def __init__(self, *args, **kwargs):
        super(MainPage, self).__init__(*args, **kwargs)

    def should_be_main_page(self):
        self.should_be_expected_url(Pages.MAIN_PAGE_URL)
        self.should_be_expected_title(Titles.MAIN_PAGE_TITLE)
        self.should_be_slider_carousel_main_page()

    def should_be_slider_carousel_main_page(self):
        assert self.is_element_present(*MainPageLocators.SLIDER_CAROUSEL_MAIN)
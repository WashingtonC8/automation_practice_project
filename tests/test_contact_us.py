import pytest
from ui.pages.contact_us_page import ContactUsPage
from ui.pages.main_page import MainPage
from ui.page_static import main_page_static
from data.fixtures.generate_data_contact_us_fixtures import generate_user_data_contact_us


def test_contact_us_form(browser, generate_user_data_contact_us):
    main_page = MainPage(browser, url=main_page_static.MAIN_PAGE_URL)
    main_page.open()
    main_page.should_be_main_page()
    main_page.go_to_contact_us_page()
    contact_us_page = ContactUsPage(browser, browser.current_url)
    contact_us_page.should_be_get_in_touch_title_is_visible()
    user_data_contact_us = generate_user_data_contact_us
    contact_us_page.enter_data_contact_us_form(user_data_contact_us)
    contact_us_page.enter_file_path_contact_us_form(user_data_contact_us)
    contact_us_page.click_to_submit_button_contact_us_form()
    contact_us_page.accept_to_confirm_window_contact_us_form()
    contact_us_page.should_be_success_alert_is_visible()
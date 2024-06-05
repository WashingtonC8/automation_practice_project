from ui.pages.main_page import MainPage
from ui.locators import contact_us_page_locators
from data.models.user_data_contact_us_model import UserDataContactUs


class ContactUsPage(MainPage):
    def __init__(self, *args, **kwargs):
        super(ContactUsPage, self).__init__(*args, **kwargs)

    def should_be_get_in_touch_title_is_visible(self):
        assert self.is_element_present(*contact_us_page_locators.GET_IN_TOUCH_LABEL), 'Label "New Get in Touch!" is not'\
                                                                                     'present'

    def enter_data_contact_us_form(self, user_data_contact_us=UserDataContactUs):
        self.enter_name_contact_us_form(user_data_contact_us)
        self.enter_email_contact_us_form(user_data_contact_us)
        self.enter_subject_contact_us_form(user_data_contact_us)
        self.enter_message_contact_us_form(user_data_contact_us)
        self.enter_file_path_contact_us_form(user_data_contact_us)

    def enter_name_contact_us_form(self, user_data_contact_us=UserDataContactUs):
        self.pasted_text(*contact_us_page_locators.NAME_INPUT_CONTACT_FORM, user_data_contact_us.name)

    def enter_email_contact_us_form(self, user_data_contact_us=UserDataContactUs):
        self.pasted_text(*contact_us_page_locators.EMAIL_INPUT_CONTACT_FORM, user_data_contact_us.email)

    def enter_subject_contact_us_form(self, user_data_contact_us=UserDataContactUs):
        self.pasted_text(*contact_us_page_locators.SUBJECT_INPUT_CONTACT_FORM, user_data_contact_us.subject)

    def enter_message_contact_us_form(self, user_data_contact_us=UserDataContactUs):
        self.pasted_text(*contact_us_page_locators.MESSAGE_INPUT_CONTACT_FORM, user_data_contact_us.message)

    def enter_file_path_contact_us_form(self, user_data_contact_us=UserDataContactUs):
        self.pasted_text(*contact_us_page_locators.UPLOAD_FILE_CONTACT_FORM, user_data_contact_us.file_path)

    def click_to_submit_button_contact_us_form(self):
        self.click_element(*contact_us_page_locators.SUBMIT_BUTTON_CONTACT_FORM)
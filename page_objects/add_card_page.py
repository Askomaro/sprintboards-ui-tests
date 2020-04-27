from __future__ import annotations

from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions

from config.config import Config
from page_objects.base_page import BasePageMixin


class AddCardPage(BasePageMixin):
    __CARD_TITLE = '//div[@id="add-card-modal"]'
    __TITLE_TEXT = '//h5[contains(text(), "Title")]'
    __TITLE_INPUT = f'{__TITLE_TEXT}/..//input'
    __DESCRIPTION_TEXT = '//h5[contains(text(), "Description")]'
    __DESCRIPTION_INPUT = f'{__DESCRIPTION_TEXT}/..//textarea'
    __ADD_CARD = '//button[contains(text(), "Add Card")]'

    def __init__(self, driver):
        super(AddCardPage, self).__init__(driver)

        self._is_visible(self.__CARD_TITLE)

    def set_title(self, title):
        self._send_keys(self.__TITLE_INPUT, title)

        return self

    def set_description(self, description):
        self._send_keys(self.__DESCRIPTION_INPUT, description)

        return self

    def confirm_adding_a_card(self):
        self._click_via_script_by(self.__ADD_CARD)

        return self

    def get_card_page_title(self):
        return self._find_by(self.__CARD_TITLE).text

    def wait_card_disappear(self):
        self._wait.until(expected_conditions.invisibility_of_element_located((By.XPATH, self.__CARD_TITLE)))

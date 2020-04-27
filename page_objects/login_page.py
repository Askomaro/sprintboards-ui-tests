import logging

from config.config import Config
from page_objects.base_page import BasePageMixin
from page_objects.main_page import MainPage


logger = logging.getLogger(__name__)


class LoginPage(BasePageMixin):
    __EMAIL = '//input[@type="email"]'
    __PASSWORD = '//input[@type="password"]'
    __LOGIN_BTN = '//button[@type="submit"][contains(text(), "Login")]'

    def __init__(self, driver):
        super(LoginPage, self).__init__(driver)
        self.__START_PAGE_URL = Config['start_page']

    def sign_in(self) -> MainPage:
        logger.info(f'open start page: {self.__START_PAGE_URL}')
        self._driver.get(self.__START_PAGE_URL)

        return self._sign_in(Config['login'], Config['password'])

    def _sign_in(self, username: str, password: str) -> MainPage:
        self._send_keys(self.__EMAIL, username)
        self._send_keys(self.__PASSWORD, password)

        self._click_via_script_by(self.__LOGIN_BTN)

        return MainPage(self._driver)

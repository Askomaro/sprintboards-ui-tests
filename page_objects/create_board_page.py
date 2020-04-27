from page_objects.base_page import BasePageMixin
from page_objects.board_page import BoardPage


class CreateBoardPage(BasePageMixin):
    __PAGE_TITLE = '//div[@id="primary-hero"]//h1'
    __SESSION_NAME = '//input[@placeholder="Session Name"]'
    __OWNER_SELECTOR = '//option[contains(text(), "Choose Owner...")]/..'
    __OWNER_SENDER = '//option[text()="Sennder"]'
    __CREATE_BTN = '//button[contains(text(), "Create Board")]'
    __POP_UP = '//div[@class="swal-title"][contains(text(), "Created")]'

    def __init__(self, driver):
        super(CreateBoardPage, self).__init__(driver)

    def set_session_name(self, name: str):
        self._send_keys(self.__SESSION_NAME, name)

        return self

    def choose_owner_is_sender(self):
        self._click(self.__OWNER_SENDER)

        return self

    def create_board(self) -> BoardPage:
        self._click_via_script_by(self.__CREATE_BTN)

        return BoardPage(self._driver)

    def get_page_title(self) -> str:
        return self._find_by(self.__PAGE_TITLE).text

    def created_pop_up_is_appeared(self) -> bool:
        return self._exists(self.__POP_UP)

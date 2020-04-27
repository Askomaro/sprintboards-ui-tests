from page_objects.base_page import BasePageMixin
from page_objects.create_board_page import CreateBoardPage


class MainPage(BasePageMixin):
    __CREATE_BOARD = '//a[@class="nav-link"][contains(text(), "Create Board")]'

    def __init__(self, driver):
        super(MainPage, self).__init__(driver)

    def create_board(self) -> CreateBoardPage:
        self._click_via_script_by(self.__CREATE_BOARD)

        return CreateBoardPage(self._driver)

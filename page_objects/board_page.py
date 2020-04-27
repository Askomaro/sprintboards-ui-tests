from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions

from models.card_model import CardModel
from page_objects.add_card_page import AddCardPage
from page_objects.base_page import BasePageMixin


class BoardPage(BasePageMixin):
    __WENT_WELL_TITLE = '//span[contains(text(), "Went well")]'
    __DID_NOT_GO_WELL_TITLE = '//span[contains(text(), "Didn\'t go well")]'
    __WENT_WELL_BTN = f'{__WENT_WELL_TITLE}/../button[contains(class, "text-success"])'
    __CARD_DESK = '/../../div/div'
    __CARD_TITLE = '//h6[contains(@class, "card-header")]'
    __CARD_BODY = '//div[contains(@class, "card-body")]'
    __CARD_DESCRIPTION = f'{__CARD_BODY}/p'
    __THUMBS_UP = f'{__CARD_BODY}//*[contains(@class, "fa-thumbs-up")]'
    __LIKES_COUNT = f'{__THUMBS_UP}/..'
    __DELETE_CARD = f'{__CARD_BODY}//*[contains(@class, "times-circle")]/..'
    __MODAL_HEADER = '//div[contains(@class, "modal-title")]'
    __MODAL_BODY = '//div[contains(@class, "modal-body")]/p'
    __MODAL_CONFIRM = '//div[contains(@class, "modal-footer")]/button'
    __ADD_NEW_CARD = '/../../div/button'

    def __init__(self, driver):
        super(BoardPage, self).__init__(driver)

    def add_went_well_card(self) -> AddCardPage:
        self._click_via_script_by(f'{self.__WENT_WELL_TITLE}{self.__ADD_NEW_CARD}')
        return AddCardPage(self._driver)

    def add_did_not_go_well_card(self) -> AddCardPage:
        self._click_via_script_by(f'{self.__DID_NOT_GO_WELL_TITLE}{self.__ADD_NEW_CARD}')
        return AddCardPage(self._driver)

    def get_went_well_card_desk(self) -> [CardModel]:
        cards: [WebElement] = self._find_elements(f'{self.__WENT_WELL_TITLE}{self.__CARD_DESK}')
        cards_model = self._populate_card_desk(cards)

        return cards_model

    def get_did_not_go_well_card_desk(self) -> [CardModel]:
        cards: [WebElement] = self._find_elements(f'{self.__DID_NOT_GO_WELL_TITLE}{self.__CARD_DESK}')
        cards_model = self._populate_card_desk(cards)

        return cards_model

    def get_modal_title(self) -> str:
        return self._find_by(self.__MODAL_HEADER).text

    def get_modal_description(self) -> str:
        return self._find_by(self.__MODAL_BODY).text

    def confirm_modal_operation(self):
        self._click_via_script_by(self.__MODAL_CONFIRM)
        self._wait_a_modal_disappear()

    def wait_a_modal_appeared(self):
        self._wait.until(expected_conditions.visibility_of_all_elements_located((By.XPATH, self.__MODAL_CONFIRM)))

    def _wait_a_modal_disappear(self):
        self._wait.until(expected_conditions.invisibility_of_element_located((By.XPATH, self.__MODAL_CONFIRM)))

    def _populate_card_desk(self, cards: [WebElement]) -> [CardModel]:
        cards_model = []

        for card in cards:
            cards_model.append(CardModel(
                title=card.find_element_by_xpath(self.__CARD_TITLE).text,
                description=card.find_element_by_xpath(self.__CARD_DESCRIPTION).text,
                thumbs_up_we=card.find_element_by_xpath(self.__THUMBS_UP),
                likes_count_we=card.find_element_by_xpath(self.__LIKES_COUNT),
                delete_we=card.find_element_by_xpath(self.__DELETE_CARD)
            ))

        return cards_model

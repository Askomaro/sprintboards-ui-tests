from selenium.webdriver.remote.webelement import WebElement

from helper.waiter import wait_conditions


class CardModel:
    def __init__(self,
                 title: str,
                 description: str,
                 thumbs_up_we: WebElement,
                 likes_count_we: WebElement,
                 delete_we: WebElement):
        self.title = title
        self.description = description
        self._thumbs_up_we = thumbs_up_we
        self._likes_count_we = likes_count_we
        self._delete_we = delete_we

    def __eq__(self, other):
        """Overrides the default implementation"""
        if isinstance(other, CardModel):
            return (self.title == other.title and
                    self.description == other.description)

        return False

    def thumbs_up(self):
        initial_count = self.likes_count
        self._thumbs_up_we.click()
        wait_conditions(lambda: self.likes_count != initial_count)

    @property
    def likes_count(self):
        return int(self._likes_count_we.text)

    def delete(self):
        self._delete_we.click()

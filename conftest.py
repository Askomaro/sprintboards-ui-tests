import logging

import pytest
from selenium import webdriver

from config.config import Config
from page_objects.board_page import BoardPage
from page_objects.login_page import LoginPage


logger = logging.getLogger(__name__)


@pytest.yield_fixture(scope='function')
def driver():
    logger.info('initializing WebDriver')
    _driver = webdriver.Chrome()

    _driver.implicitly_wait(Config['implicitly_wait'])

    yield _driver

    logger.info('close WebDriver')
    _driver.quit()


@pytest.fixture()
def board_page(driver, cli_credentials) -> BoardPage:
    login_page = LoginPage(driver)
    main_page = login_page.sign_in()

    create_board_page = main_page.create_board()
    return (create_board_page
            .set_session_name('My first board')
            .choose_owner_is_sender()
            .create_board())


@pytest.fixture()
def board_page_with_cards(board_page: BoardPage) -> BoardPage:
    title_card = 'Goal was achieved'
    description_card = 'Sprint was well planned'

    add_card_page = board_page.add_went_well_card()
    (add_card_page
     .set_title(title_card)
     .set_description(description_card)
     .confirm_adding_a_card()
     .wait_card_disappear())

    add_card_page_bad = board_page.add_did_not_go_well_card()
    (add_card_page_bad
     .set_title('Goal was not achieved')
     .confirm_adding_a_card()
     .wait_card_disappear())

    return board_page


def pytest_addoption(parser):
    parser.addoption(
        "--login",
        action="store",
        default=None,
        help="login name to a platform"
    )

    parser.addoption(
        "--password",
        action="store",
        default=None,
        help="password to a platform"
    )


@pytest.fixture(scope="session")
def cli_credentials(pytestconfig):
    Config['login'] = pytestconfig.getoption('--login', skip=True)
    Config['password'] = pytestconfig.getoption('--password', skip=True)


@pytest.fixture
def cli_opts(request):
    return request.config.getoption("--cmdopt")

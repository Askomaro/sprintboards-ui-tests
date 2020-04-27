from page_objects.login_page import LoginPage


def test__create_a_board_is_available(driver, cli_credentials):
    login_page = LoginPage(driver)
    main_page = login_page.sign_in()
    create_board_page = main_page.create_board()

    assert create_board_page.get_current_url() == 'https://sprintboards.io/boards/create'
    assert create_board_page.get_page_title() == 'Create a Board'


def test__a_board_is_created(driver, cli_credentials):
    login_page = LoginPage(driver)
    main_page = login_page.sign_in()

    create_board_page = main_page.create_board()
    board_page = (create_board_page
                  .set_session_name('My first board')
                  .choose_owner_is_sender()
                  .create_board())

    assert create_board_page.created_pop_up_is_appeared()
    assert 'https://sprintboards.io/boards' in board_page.get_current_url()


def test__a_card_went_well_successfully_added(board_page):
    title_card = 'Goal was achieved'
    description_card = 'Sprint was well planned'

    add_card_page = board_page.add_went_well_card()
    assert add_card_page.get_card_page_title() == 'Add a Card'

    (add_card_page
     .set_title(title_card)
     .set_description(description_card)
     .confirm_adding_a_card())

    good_card_desk = board_page.get_went_well_card_desk()
    assert len(good_card_desk) == 1

    card = good_card_desk[0]
    assert card.title == title_card
    assert card.description == description_card


def test__a_card_did_not_go_well_successfully_added(board_page):
    title_card = 'Goal was not achieved'

    add_card_page = board_page.add_did_not_go_well_card()
    assert add_card_page.get_card_page_title() == 'Add a Card'

    (add_card_page
     .set_title(title_card)
     .confirm_adding_a_card())
    bad_card_desk = board_page.get_did_not_go_well_card_desk()
    assert len(bad_card_desk) == 1

    card = bad_card_desk[0]
    assert card.title == title_card
    assert card.description == 'No description provided.'


def test__thumbs_up_action_increases_likes_count(board_page_with_cards):
    good_card_desk = board_page_with_cards.get_went_well_card_desk()
    card = good_card_desk[0]
    initial_likes_count = card.likes_count

    card.thumbs_up()
    assert card.likes_count == initial_likes_count + 1


def test__a_card_is_successfully_deleted(board_page_with_cards):
    good_card_desk = board_page_with_cards.get_went_well_card_desk()
    card = good_card_desk[0]

    card.delete()
    assert board_page_with_cards.get_modal_title() == 'Delete Card'
    assert board_page_with_cards.get_modal_description() == 'Are you sure you want to continue?'

    board_page_with_cards.confirm_modal_operation()
    good_card_desk = board_page_with_cards.get_went_well_card_desk()

    assert len(good_card_desk) == 0

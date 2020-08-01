import datetime

import pytest
from unittest.mock import create_autospec, patch
from slot_booking.interactors.presenters.user_login_presenter_interface import LoginPresenterInterface
from slot_booking.interactors.storages.user_login_storage_interface import LoginStorageInterface
from slot_booking.interactors.user_login_details_interactor import UserLoginInteractor
from slot_booking.exceptions.exceptions import InvalidUsernameException, InvalidPasswordException
from common.oauth2_storage import OAuth2SQLStorage

from common.dtos import UserAuthTokensDTO


def test_to_check_the_userdetails_with_invalid_user_name_raise_exception_error():
    username = 123
    password = "susmitha"

    presenter = create_autospec(LoginPresenterInterface)
    storage = create_autospec(LoginStorageInterface)
    oauth_storage = create_autospec(OAuth2SQLStorage)

    storage.validate_username.return_value = False
    presenter.raise_invalid_username_exception.side_effect = InvalidUsernameException

    interactors = UserLoginInteractor(
        storage=storage,
        presenter=presenter,
        oauth_storage=oauth_storage
    )


    with pytest.raises(InvalidUsernameException) as err:
        interactors.user_login_interactor(
                username=username,
                password=password)

    storage.validate_username.assert_called_once_with(
                username=username)

def test_to_check_the_userdetails_with_invalid_password_raise_exception_error():
    username = "susmitha"
    password = 2234

    presenter = create_autospec(LoginPresenterInterface)
    storage = create_autospec(LoginStorageInterface)
    oauth_storage = create_autospec(OAuth2SQLStorage)

    storage.validate_username.return_value = True
    storage.validate_password.return_value = False
    presenter.raise_invalid_password_exception.side_effect = InvalidPasswordException

    interactors = UserLoginInteractor(
        storage=storage,
        presenter=presenter,
        oauth_storage=oauth_storage
    )


    with pytest.raises(InvalidPasswordException) as err:
        interactors.user_login_interactor(
                username=username,
                password=password)

    storage.validate_password.assert_called_once_with(
                username=username,
                password=password)

@patch('common.oauth_user_auth_tokens_service.OAuthUserAuthTokensService.create_user_auth_tokens')
def test_to_get_access_token_with_the_given_user_id(oauth_mock):

    username = "susmnitha"
    password = "admin1234"
    user_id = 1
    access_token = "1234567890"
    excepted_output = {"access_token": access_token}

    presenter = create_autospec(LoginPresenterInterface)
    storage = create_autospec(LoginStorageInterface)
    oauth_storage = create_autospec(OAuth2SQLStorage)
    oauth_mock.return_value = UserAuthTokensDTO(user_id = "1",
                access_token = "1234567890",
                refresh_token = "abcdefghi",
                expires_in = "abdcdc",
                role=False)

    storage.get_user_id.return_value = user_id
    presenter.get_response.return_value = excepted_output

    interactor = UserLoginInteractor(
        storage=storage,
        presenter=presenter,
        oauth_storage=oauth_storage
    )

    resulted_access_token = interactor.user_login_interactor(
        username=username,
        password=password)

    assert resulted_access_token == excepted_output
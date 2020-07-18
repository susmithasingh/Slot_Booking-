from slot_booking.interactors.storages.user_login_storage_interface import \
    LoginStorageInterface
from slot_booking.exceptions.exceptions import *
from slot_booking.interactors.presenters. \
    user_login_presenter_interface import LoginPresenterInterface
from common.oauth_user_auth_tokens_service import OAuthUserAuthTokensService
from common.oauth2_storage import OAuth2SQLStorage

class UserLoginInteractor:

    def __init__(self,
                 storage: LoginStorageInterface,
                 presenter: LoginPresenterInterface,
                 oauth_storage: OAuth2SQLStorage
                 ):

        self.storage = storage
        self.presenter = presenter
        self.oauth_storage = oauth_storage

    def user_login_interactor(self,
                               username: str,
                               password: str
                               ):

        is_valid_username = self.storage.validate_username(
                username=username
            )
        not_valid_username = not is_valid_username

        if not_valid_username:
            self.presenter.raise_invalid_username_exception()
            return

        is_valid_password = self.storage.validate_password(
                username=username,
                password=password
            )

        if is_valid_password:

            self.presenter.raise_invalid_password_exception()
            return



        user_id = self.storage.get_user_id(
                username=username,
                password=password)

        # return user_id

        interactor = OAuthUserAuthTokensService(
            oauth2_storage = self.oauth_storage
            )
        dto = interactor.create_user_auth_tokens(user_id=user_id)
        print("*******************************************8")
        print(dto)

        response = self.presenter.get_response(
            dto=dto
            )
        return response

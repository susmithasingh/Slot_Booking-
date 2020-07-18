from slot_booking.interactors.presenters.user_login_presenter_interface import \
    LoginPresenterInterface
from slot_booking.constants.exception_messages import \
    (
        INVALID_USER_NAME,
        INVALID_PASSWORD
    )
from slot_booking.interactors.storages.dtos import UserAuthTokensDTO
from django_swagger_utils.drf_server.exceptions import NotFound

class LoginDetailsPresenterImplementation(LoginPresenterInterface):


    def raise_invalid_username_exception(self):
        raise NotFound(*INVALID_USER_NAME)


    def raise_invalid_password_exception(self):
        raise NotFound(*INVALID_PASSWORD)

    def get_response(self, dto: UserAuthTokensDTO):
        return {"access_token": dto.access_token}
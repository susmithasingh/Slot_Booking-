from abc import ABC
from abc import abstractmethod
from slot_booking.interactors.storages.dtos import UserAuthTokensDTO


class LoginPresenterInterface(ABC):

    @abstractmethod
    def raise_invalid_username_exception(self):
        pass

    @abstractmethod
    def raise_invalid_password_exception(self):
        pass

    @abstractmethod
    def get_response(self, dto: UserAuthTokensDTO) -> dict:
        pass
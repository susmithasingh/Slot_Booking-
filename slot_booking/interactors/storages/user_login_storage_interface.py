from abc import ABC
from abc import abstractmethod


class LoginStorageInterface(ABC):

    @abstractmethod
    def validate_username(self, username: str) -> bool:
        pass


    @abstractmethod
    def validate_password(self, username: str, password: str) -> bool:
        pass

    @abstractmethod
    def get_user_id(self, username: str, password: str) -> int:
        pass
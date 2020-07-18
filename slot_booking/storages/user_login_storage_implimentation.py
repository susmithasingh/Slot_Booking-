from slot_booking.models import User
from slot_booking.interactors.storages.user_login_storage_interface import \
    LoginStorageInterface


class UserLoginStorageImplimentation(LoginStorageInterface):

    def validate_username(self, username: str) -> bool:
        is_valid_username = User.objects.filter(username=username).exists()
        return is_valid_username

    def validate_password(self, username: str, password: str) -> bool:
        user = User.objects.filter(username=username).first()
        print(user.password)
        is_valid_password = user.check_password(user.password)
        print(is_valid_password)
        return is_valid_password


    def get_user_id(self, username: str, password: str) -> int:
        user_id = User.objects.get(username=username).id
        return user_id


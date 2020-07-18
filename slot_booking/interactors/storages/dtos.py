from dataclasses import dataclass
import datetime

@dataclass
class UserAuthTokensDTO:
    user_id: str
    access_token: str
    refresh_token: str
    expires_in: datetime
from dataclasses import dataclass
import datetime

@dataclass
class UserAuthTokensDTO:
    user_id: str
    access_token: str
    refresh_token: str
    role: bool
    expires_in: datetime

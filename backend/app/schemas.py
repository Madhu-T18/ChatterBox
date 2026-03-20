from pydantic import BaseModel
from typing import Optional
from datetime import datetime



# ===============================
# USER SCHEMAS
# ===============================
class UserCreate(BaseModel):
    username: str
    email: str
    password: str



class UserLogin(BaseModel):
	email: str
	password: str


class UserResponse(BaseModel):
	id: int
	username: str
	full_name: str
	is_admin: bool
	is_blocked: bool
	warning_count: int
	created_at: datetime
	class Config:
		from_attributes = True


# ===============================
# TOKEN SCHEMA
# ===============================
class TokenResponse(BaseModel):
	access_token: str
	token_type: str


# ===============================
# MESSAGE SCHEMA
# ===============================
class MessageResponse(BaseModel):
	id: int
	sender_id: int
	receiver_id: Optional[int]
	room: Optional[str]
	content: str
	timestamp: datetime

	class Config:
		from_attributes = True

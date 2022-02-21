from typing import Optional

from pydantic import BaseModel


class RequestBody(BaseModel):
    username: str
    password: str
    tries: int = 3
    secret_answer: Optional[str]
    authenticator_secret_key: Optional[str]


class User(BaseModel):
    name: str
    surname: str

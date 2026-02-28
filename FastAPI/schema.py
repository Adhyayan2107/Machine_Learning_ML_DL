from pydantic import BaseModel
from typing import Optional


class Greet(BaseModel):
    name: str
    age: int
    desc: Optional[str] = None


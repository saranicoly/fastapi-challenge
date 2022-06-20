from pydantic import BaseModel

class Person(BaseModel):
  name: str
  friends: list
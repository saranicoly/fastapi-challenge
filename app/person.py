from pydantic import BaseModel

class Person(BaseModel):
  name: str
  friends: list = []

  def __init__(self, name, friends=[]):
    self.name = name
    self.friends = friends
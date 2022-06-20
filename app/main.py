import json

from pydantic import BaseModel
from fastapi import FastAPI
from grafo import Grafo

app = FastAPI()

grafo = Grafo()

class Person(BaseModel):
  name: str
  friends: list = []

@app.get("/")
def read_root():
  return show_dict(grafo)

@app.get("/friends/{name}")
def get_friends(name: str):
  all_friends = []
  for person, is_friend in grafo.matriz_adj[name].items():
    if is_friend == 1 and person != name:
      all_friends.append(person)
  return all_friends

@app.get("/possible_friends/{name}")
def get_possible_friends(name: str):
  all_friends = set(get_friends(name))
  all_friends.add(name)
  possible_friends = set()
  for person in all_friends:
    temp_friends = set(get_friends(person))
    possible_friends = possible_friends.union(temp_friends.difference(all_friends))
  return possible_friends

@app.post("/add_person/")
def create_person(person: Person):
  grafo.matriz_adj[person.name] = {key: 0 for key in grafo.matriz_adj.keys()}
  for friend in person.friends:
    grafo.matriz_adj[person.name][friend] = 1
    grafo.matriz_adj[friend][person.name] = 1
  return {"Nova pessoa adicionada com sucesso!"}

def show_dict(grafo):
  adj_list = list(grafo.matriz_adj.keys())
  return json.dumps(adj_list, ensure_ascii=False).encode('utf8')
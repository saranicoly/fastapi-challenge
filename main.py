import json

from fastapi import FastAPI
from grafo import Grafo

app = FastAPI()

grafo = Grafo()

@app.get("/")
def read_root():
  return show_dict(grafo)

@app.get("/friends/{name}")
def read_pessoa(name: str):
  all_friends = []
  for person, is_friend in grafo.matriz_adj[name].items():
    if is_friend == 1 and person != name:
      all_friends.append(person)
  return all_friends

  # @app.get("/unknown_friends/{name}")
  # def read_pessoa(name: str):
  #   known_people = []
  #   for known_person, is_knwon in grafo.matriz_adj[name].items():
  #     if is_knwon == 1 and known_person != name:
  #       known_people.append(known_person)
  #   return known_people

# @app.put("/items/{item_id}")
# def update_item(item_id: int, item: Item):
#   return {"item_name": item.name, "item_id": item_id}

def show_dict(grafo):
  adj_list = list(grafo.matriz_adj.keys())
  return json.dumps(adj_list, ensure_ascii=False).encode('utf8')
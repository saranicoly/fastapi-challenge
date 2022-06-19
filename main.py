import json
from typing import Union

from fastapi import FastAPI
from pydantic import BaseModel
from grafo import Grafo

app = FastAPI()

grafo = Grafo()

class Item(BaseModel):
  name: str
  price: float
  is_offer: Union[bool, None] = None

@app.get("/")
def read_root():
  return {show_dict(grafo)}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
  return {"item_id": item_id, "q": q}

@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
  return {"item_name": item.name, "item_id": item_id}

def show_dict(grafo):
  adj_list = list(grafo.matriz_adj.keys())
  return json.dumps(adj_list, ensure_ascii=False).encode('utf8')
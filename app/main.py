from fastapi import FastAPI
from grafo import Graph
from person import Person

app = FastAPI()
grafo = Graph()

@app.get("/")
def get_current_graph():
  return grafo.get_nodes()

@app.get("/friends/{name}")
def get_friends(name: str):
  return grafo.get_edges(name)

@app.get("/possible_friends/{name}")
def get_possible_friends(name: str):
  # possible friends are those who you may know but are not your friends
  return grafo.get_second_degree_edges(name)

@app.post("/add_connection/")
def create_connection(person: Person):
  return grafo.add_node(person)
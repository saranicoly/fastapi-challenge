import json

class Grafo():
  matriz_adj = dict()

  def __init__(self):
    grafo_inicial = ["Ana", "Maria", "Vinicius", "Luiza", "João", "Carlos"]
    for i in grafo_inicial:
      self.matriz_adj[i] = None

    self.matriz_adj["Ana"] = {
      "Maria": 1,
      "Vinicius": 1,
      "Carlos": 1,
      "João": 1,
      "Ana": 0,
      "Luiza": 0,
    }
    self.matriz_adj["Maria"] = {
      "Maria": 0,
      "Vinicius": 1,
      "Carlos": 0,
      "João": 0,
      "Ana": 1,
      "Luiza": 0,
    }
    self.matriz_adj["Vinicius"] = {
      "Maria": 1,
      "Vinicius": 0,
      "Carlos": 0,
      "João": 0,
      "Ana": 1,
      "Luiza": 0,
    }
    self.matriz_adj["Luiza"] = {
      "Maria": 0,
      "Vinicius": 0,
      "Carlos": 0,
      "João": 1,
      "Ana": 0,
      "Luiza": 0,
    }
    self.matriz_adj["João"] = {
      "Maria": 0,
      "Vinicius": 0,
      "Carlos": 0,
      "João": 0,
      "Ana": 1,
      "Luiza": 1,
    }
    self.matriz_adj["Carlos"] = {
      "Maria": 0,
      "Vinicius": 0,
      "Carlos": 0,
      "João": 0,
      "Ana": 1,
      "Luiza": 0,
    }

  def show_graph(self):
    # Shows the current state of the graph (all the people)
    adj_list = list(self.matriz_adj.keys())
    return json.dumps(adj_list, ensure_ascii=False).encode('utf8')
  
  def add_node(self, person):
    # Adds a new person(node) to the graph
    self.matriz_adj[person.name] = {key: 0 for key in self.matriz_adj.keys()}
    for friend in person.friends:
      self.matriz_adj[person.name][friend] = 1
      self.matriz_adj[friend][person.name] = 1
    return {"Nova pessoa adicionada com sucesso!"}
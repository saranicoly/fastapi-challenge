from fastapi import HTTPException
class Graph():
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

  def get_nodes(self):
    # Shows the nodes (all the people)
    adj_list = list(self.matriz_adj)
    return adj_list
  
  def add_node(self, person):
    # Adds a new person(node) to the graph
    self.matriz_adj[person.name] = {}
    for friend in person.friends:
      if friend not in self.matriz_adj:
        raise HTTPException(status_code=404, detail=f"Friend {friend} not found")
      self.matriz_adj[person.name][friend] = 1
      self.matriz_adj[friend][person.name] = 1
    return "Pessoa adicionada com sucesso"
  
  def get_edges(self, name):
    # Shows the edges(friends) of a person
    if name not in self.matriz_adj:
      raise HTTPException(status_code=404, detail=f"Person {name} not found")
    edges = []
    for friend in self.matriz_adj[name]:
      if self.matriz_adj[name][friend] == 1:
        edges.append(friend)
    return edges
  
  def get_second_degree_edges(self, name):
    # Shows the second degree edges(friends of friends) of a person
    if name not in self.matriz_adj:
      raise HTTPException(status_code=404, detail=f"Person {name} not found")
    edges = set(self.get_edges(name))
    edges.add(name) # Adds the person to the list of edges, so it won't be added in the second degree friends
    second_degree_edges = set()
    for friend in edges:
      temp = set(self.get_edges(friend))
      second_degree_edges = second_degree_edges.union(temp.difference(edges))
    return second_degree_edges
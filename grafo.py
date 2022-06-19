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
      "Ana": 1,
      "Luiza": 0,
    }
    self.matriz_adj["Maria"] = {
      "Maria": 1,
      "Vinicius": 1,
      "Carlos": 0,
      "João": 0,
      "Ana": 1,
      "Luiza": 0,
    }
    self.matriz_adj["Vinicius"] = {
      "Maria": 1,
      "Vinicius": 1,
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
      "Luiza": 1,
    }
    self.matriz_adj["João"] = {
      "Maria": 0,
      "Vinicius": 0,
      "Carlos": 0,
      "João": 1,
      "Ana": 1,
      "Luiza": 1,
    }
    self.matriz_adj["Carlos"] = {
      "Maria": 0,
      "Vinicius": 0,
      "Carlos": 1,
      "João": 0,
      "Ana": 1,
      "Luiza": 0,
    }
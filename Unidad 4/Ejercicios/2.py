class UndirectedGraphAdjList:
  """Grafo no dirigido representado mediante listas de adyacencia."""

  def __init__(self):
    self._adj_list = {}

  def add_vertex(self, vertex):
    """Agrega un vértice al grafo."""
    if vertex not in self._adj_list:
      self._adj_list[vertex] = {}

  def add_edge(self, u, v, weight=1):
    """Agrega una arista bidireccional entre u y v con un peso."""
    self.add_vertex(u)
    self.add_vertex(v)
    self._adj_list[u][v] = weight
    self._adj_list[v][u] = weight

  def remove_vertex(self, vertex):
    """Elimina un vértice y sus conexiones en ambos sentidos."""
    if vertex not in self._adj_list:
      raise KeyError(f"El vértice {vertex} no existe.")

    for neighbor in list(self._adj_list[vertex]):
      del self._adj_list[neighbor][vertex]

    del self._adj_list[vertex]

  def remove_edge(self, u, v):
    """Elimina la arista entre u y v en ambas direcciones."""
    if u in self._adj_list and v in self._adj_list[u]:
      del self._adj_list[u][v]
    if v in self._adj_list and u in self._adj_list[v]:
      del self._adj_list[v][u]

  def get_neighbors(self, vertex):
    """Devuelve los vecinos y los pesos de las aristas."""
    if vertex not in self._adj_list:
      raise KeyError(f"El vértice {vertex} no existe.")
    return self._adj_list[vertex]

  def __str__(self):
    """Visualización en texto de la lista de adyacencia."""
    result = "Grafo No Dirigido (Lista de Adyacencia):\n"
    for vertex, neighbors in self._adj_list.items():
      result += f"  {vertex} <-> {neighbors}\n"
    return result


if __name__ == "__main__":
    # 3. Prueba Grafo No Dirigido - Lista de Adyacencia
    g_undir_list = UndirectedGraphAdjList()
    g_undir_list.add_edge("X", "Y", 10)
    g_undir_list.add_edge("Y", "Z", 7)
    print(g_undir_list)
    print("Vecinos de Y:", g_undir_list.get_neighbors("Y"))
    print("-" * 50)
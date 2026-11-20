class DirectedGraphAdjList:
  """Grafo dirigido representado mediante listas de adyacencia (diccionarios)."""

  def __init__(self):
    self._adj_list = {}

  def add_vertex(self, vertex):
    """Agrega un vértice al grafo si no existe."""
    if vertex not in self._adj_list:
      self._adj_list[vertex] = {}

  def add_edge(self, u, v, weight=1):
    """Agrega una arista dirigida de u hacia v con un peso opcional."""
    self.add_vertex(u)
    self.add_vertex(v)
    self._adj_list[u][v] = weight

  def remove_vertex(self, vertex):
    """Elimina un vértice y todas las aristas entrantes y salientes."""
    if vertex not in self._adj_list:
      raise KeyError(f"El vértice {vertex} no existe.")

    # Eliminar aristas salientes
    del self._adj_list[vertex]

    # Eliminar aristas entrantes desde otros vértices
    for node in self._adj_list:
      if vertex in self._adj_list[node]:
        del self._adj_list[node][vertex]

  def remove_edge(self, u, v):
    """Elimina la arista dirigida entre u y v."""
    if u in self._adj_list and v in self._adj_list[u]:
      del self._adj_list[u][v]

  def get_neighbors(self, vertex):
    """Devuelve los vecinos salientes y los pesos de las aristas."""
    if vertex not in self._adj_list:
      raise KeyError(f"El vértice {vertex} no existe.")
    return self._adj_list[vertex]

  def bfs(self, start_vertex):
    """Recorrido en anchura (BFS)."""
    if start_vertex not in self._adj_list:
      raise KeyError(f"El vértice {start_vertex} no existe.")

    visited = {start_vertex}
    order = []
    queue = [start_vertex]

    while queue:
      vertex = queue.pop(0)
      order.append(vertex)
      for neighbor in self._adj_list[vertex]:
        if neighbor not in visited:
          visited.add(neighbor)
          queue.append(neighbor)
    return order

  def __str__(self):
    """Visualización en texto de la lista de adyacencia."""
    result = "Grafo Dirigido (Lista de Adyacencia):\n"
    for vertex, neighbors in self._adj_list.items():
      result += f"  {vertex} -> {neighbors}\n"
    return result


if __name__ == "__main__":
    # 1. Prueba Grafo Dirigido - Lista de Adyacencia
    g_dir_list = DirectedGraphAdjList()
    g_dir_list.add_edge("A", "B", 3)
    g_dir_list.add_edge("A", "C", 5)
    g_dir_list.add_edge("B", "C", 2)
    print(g_dir_list)
    print("BFS desde A:", g_dir_list.bfs("A"))
    print("-" * 50)
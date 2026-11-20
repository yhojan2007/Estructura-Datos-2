class DirectedGraphAdjMatrix:
  """Grafo dirigido representado mediante matriz de adyacencia."""

  def __init__(self):
    self._vertices = []
    self._matrix = []

  def add_vertex(self, vertex):
    """Agrega un vértice al grafo."""
    if vertex not in self._vertices:
      self._vertices.append(vertex)
      # Expandir matriz existente con filas/columnas de ceros
      for row in self._matrix:
        row.append(0)
      new_row = [0] * len(self._vertices)
      self._matrix.append(new_row)

  def add_edge(self, u, v, weight=1):
    """Agrega una arista dirigida de u hacia v con un peso."""
    self.add_vertex(u)
    self.add_vertex(v)
    i = self._vertices.index(u)
    j = self._vertices.index(v)
    self._matrix[i][j] = weight

  def remove_vertex(self, vertex):
    """Elimina un vértice y actualiza la matriz de adyacencia."""
    if vertex not in self._vertices:
      raise KeyError(f"El vértice {vertex} no existe.")

    idx = self._vertices.index(vertex)
    self._vertices.pop(idx)
    self._matrix.pop(idx)
    for row in self._matrix:
      row.pop(idx)

  def remove_edge(self, u, v):
    """Elimina la arista dirigida entre u y v (establece peso en 0)."""
    if u in self._vertices and v in self._vertices:
      i = self._vertices.index(u)
      j = self._vertices.index(v)
      self._matrix[i][j] = 0

  def get_neighbors(self, vertex):
    """Devuelve los vecinos y sus pesos en formato de diccionario."""
    if vertex not in self._vertices:
      raise KeyError(f"El vértice {vertex} no existe.")

    i = self._vertices.index(vertex)
    neighbors = {}
    for j, weight in enumerate(self._matrix[i]):
      if weight != 0:
        neighbors[self._vertices[j]] = weight
    return neighbors

  def __str__(self):
    """Visualización en texto de la matriz de adyacencia."""
    res = "Grafo Dirigido (Matriz de Adyacencia):\n"
    res += "     " + " ".join(f"{v:>4}" for v in self._vertices) + "\n"
    for i, row in enumerate(self._matrix):
      row_str = " ".join(f"{w:>4}" for w in row)
      res += f"  {self._vertices[i]} [{row_str}]\n"
    return res


if __name__ == "__main__":
    # 2. Prueba Grafo Dirigido - Matriz de Adyacencia
    g_dir_mat = DirectedGraphAdjMatrix()
    g_dir_mat.add_edge("A", "B", 4)
    g_dir_mat.add_edge("B", "C", 1)
    print(g_dir_mat)
    print("Vecinos de B:", g_dir_mat.get_neighbors("B"))
    print("-" * 50)
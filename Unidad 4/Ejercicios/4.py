class UndirectedGraphAdjMatrix:
  """Grafo no dirigido representado mediante matriz de adyacencia simétrica."""

  def __init__(self):
    self._vertices = []
    self._matrix = []

  def add_vertex(self, vertex):
    """Agrega un vértice al grafo."""
    if vertex not in self._vertices:
      self._vertices.append(vertex)
      for row in self._matrix:
        row.append(0)
      new_row = [0] * len(self._vertices)
      self._matrix.append(new_row)

  def add_edge(self, u, v, weight=1):
    """Agrega una arista simétrica entre u y v."""
    self.add_vertex(u)
    self.add_vertex(v)
    i = self._vertices.index(u)
    j = self._vertices.index(v)
    self._matrix[i][j] = weight
    self._matrix[j][i] = weight

  def remove_vertex(self, vertex):
    """Elimina un vértice y ajusta la matriz simétrica."""
    if vertex not in self._vertices:
      raise KeyError(f"El vértice {vertex} no existe.")

    idx = self._vertices.index(vertex)
    self._vertices.pop(idx)
    self._matrix.pop(idx)
    for row in self._matrix:
      row.pop(idx)

  def remove_edge(self, u, v):
    """Elimina la arista simétrica entre u y v."""
    if u in self._vertices and v in self._vertices:
      i = self._vertices.index(u)
      j = self._vertices.index(v)
      self._matrix[i][j] = 0
      self._matrix[j][i] = 0

  def get_neighbors(self, vertex):
    """Devuelve los vecinos y pesos en formato de diccionario."""
    if vertex not in self._vertices:
      raise KeyError(f"El vértice {vertex} no existe.")

    i = self._vertices.index(vertex)
    neighbors = {}
    for j, weight in enumerate(self._matrix[i]):
      if weight != 0:
        neighbors[self._vertices[j]] = weight
    return neighbors

  def __str__(self):
    """Visualización en texto de la matriz de adyacencia simétrica."""
    res = "Grafo No Dirigido (Matriz de Adyacencia):\n"
    res += "     " + " ".join(f"{v:>4}" for v in self._vertices) + "\n"
    for i, row in enumerate(self._matrix):
      row_str = " ".join(f"{w:>4}" for w in row)
      res += f"  {self._vertices[i]} [{row_str}]\n"
    return res


if __name__ == "__main__":
    # 4. Prueba Grafo No Dirigido - Matriz de Adyacencia
    g_undir_mat = UndirectedGraphAdjMatrix()
    g_undir_mat.add_edge("P", "Q", 6)
    g_undir_mat.add_edge("Q", "R", 8)
    print(g_undir_mat)
    print("Vecinos de Q:", g_undir_mat.get_neighbors("Q"))
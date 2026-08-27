# =====================================================================
# Unidad I: Árbol Binario de Búsqueda (ABB) - Implementación Iterativa
# =====================================================================

from __future__ import annotations

from collections import deque
from typing import Any


class Nodo:
    """Nodo de un árbol binario."""

    def __init__(self, dato: Any) -> None:
        self.dato: Any = dato
        self.izquierdo: Nodo | None = None
        self.derecho: Nodo | None = None

    def __repr__(self) -> str:
        """Representación en cadena del nodo."""
        return f"Nodo({self.dato})"


class ArbolBinarioBusqueda:
    """
    Implementación iterativa del Árbol Binario de Búsqueda (ABB).

    Propiedad ABB: para cada nodo N,
        - subárbol izquierdo < N.dato
        - subárbol derecho  > N.dato

    Todas las operaciones recorren el árbol con bucles (pila o cola),
    sin llamadas recursivas.
    """

    def __init__(self) -> None:
        """Inicializa el árbol vacío."""
        self._raiz: Nodo | None = None
        self._tamanio: int = 0

    # ------------------------------------------------------------------
    # Propiedades
    # ------------------------------------------------------------------

    def esta_vacio(self) -> bool:
        """Retorna True si el árbol no tiene nodos."""
        return self._raiz is None

    def __len__(self) -> int:
        """Retorna la cantidad de nodos del árbol."""
        return self._tamanio

    # ------------------------------------------------------------------
    # Inserción
    # ------------------------------------------------------------------

    def insertar(self, dato: Any) -> None:
        """
        Inserta un nuevo dato manteniendo la propiedad ABB.
        Los valores duplicados son ignorados.

        Complejidad: O(h) donde h = altura del árbol.
        """
        nuevo = Nodo(dato)

        if self._raiz is None:
            self._raiz = nuevo
            self._tamanio += 1
            return

        actual = self._raiz
        while True:
            if dato < actual.dato:
                if actual.izquierdo is None:
                    actual.izquierdo = nuevo
                    self._tamanio += 1
                    return
                actual = actual.izquierdo
            elif dato > actual.dato:
                if actual.derecho is None:
                    actual.derecho = nuevo
                    self._tamanio += 1
                    return
                actual = actual.derecho
            else:
                # dato == actual.dato → duplicado, ignorar
                return

    # ------------------------------------------------------------------
    # Búsqueda
    # ------------------------------------------------------------------

    def buscar(self, dato: Any) -> bool:
        """
        Busca un dato en el árbol.

        Retorna:
            True si el dato existe, False en caso contrario.

        Complejidad: O(h)
        """
        return self.obtener_nodo(dato) is not None

    def obtener_nodo(self, dato: Any) -> Nodo | None:
        """
        Retorna el nodo que contiene el dato, o None si no existe.

        Complejidad: O(h)
        """
        actual = self._raiz
        while actual is not None:
            if dato == actual.dato:
                return actual
            if dato < actual.dato:
                actual = actual.izquierdo
            else:
                actual = actual.derecho
        return None

    def _buscar_con_padre(self, dato: Any) -> tuple[Nodo | None, Nodo | None]:
        """
        Localiza un dato y su padre.

        Retorna:
            (padre, nodo). Si el dato no existe, nodo es None.
            Si el dato está en la raíz, padre es None.
        """
        padre: Nodo | None = None
        actual = self._raiz
        while actual is not None:
            if dato == actual.dato:
                return padre, actual
            padre = actual
            if dato < actual.dato:
                actual = actual.izquierdo
            else:
                actual = actual.derecho
        return padre, None

    # ------------------------------------------------------------------
    # Mínimo y Máximo
    # ------------------------------------------------------------------

    def minimo(self) -> Any:
        """
        Retorna el valor mínimo del árbol.
        El mínimo siempre es el nodo más a la izquierda.

        Raises:
            ValueError: si el árbol está vacío.
        """
        if self.esta_vacio():
            raise ValueError("El árbol está vacío")
        return self._minimo_nodo(self._raiz).dato

    def _minimo_nodo(self, nodo: Nodo) -> Nodo:
        """Retorna el nodo con el valor mínimo del subárbol."""
        actual = nodo
        while actual.izquierdo is not None:
            actual = actual.izquierdo
        return actual

    def maximo(self) -> Any:
        """
        Retorna el valor máximo del árbol.
        El máximo siempre es el nodo más a la derecha.

        Raises:
            ValueError: si el árbol está vacío.
        """
        if self.esta_vacio():
            raise ValueError("El árbol está vacío")
        return self._maximo_nodo(self._raiz).dato

    def _maximo_nodo(self, nodo: Nodo) -> Nodo:
        """Retorna el nodo con el valor máximo del subárbol."""
        actual = nodo
        while actual.derecho is not None:
            actual = actual.derecho
        return actual

    # ------------------------------------------------------------------
    # Eliminación
    # ------------------------------------------------------------------

    def eliminar(self, dato: Any) -> bool:
        """
        Elimina un nodo con el dato dado.

        Casos:
            1. Nodo es hoja → eliminación directa.
            2. Nodo tiene 1 hijo → el padre apunta al hijo.
            3. Nodo tiene 2 hijos → reemplazar con sucesor inorden.

        Retorna:
            True si eliminó, False si el dato no existía.

        Complejidad: O(h)
        """
        padre, nodo = self._buscar_con_padre(dato)
        if nodo is None:
            return False

        # Caso 3: dos hijos → copiar el sucesor inorden y eliminar ese sucesor
        # (el sucesor no tiene hijo izquierdo: es hoja o solo tiene hijo derecho).
        if nodo.izquierdo is not None and nodo.derecho is not None:
            sucesor_padre = nodo
            sucesor = nodo.derecho
            while sucesor.izquierdo is not None:
                sucesor_padre = sucesor
                sucesor = sucesor.izquierdo
            nodo.dato = sucesor.dato
            padre, nodo = sucesor_padre, sucesor

        # Casos 1 y 2: nodo es hoja o tiene un solo hijo
        hijo = nodo.izquierdo if nodo.izquierdo is not None else nodo.derecho
        self._reemplazar_hijo(padre, nodo, hijo)
        self._tamanio -= 1
        return True

    def _reemplazar_hijo(
        self,
        padre: Nodo | None,
        hijo_actual: Nodo,
        nuevo_hijo: Nodo | None,
    ) -> None:
        """Sustituye hijo_actual por nuevo_hijo en el padre (o en la raíz)."""
        if padre is None:
            self._raiz = nuevo_hijo
        elif padre.izquierdo is hijo_actual:
            padre.izquierdo = nuevo_hijo
        else:
            padre.derecho = nuevo_hijo

    # ------------------------------------------------------------------
    # Información del árbol
    # ------------------------------------------------------------------

    def altura(self) -> int:
        """
        Calcula la altura del árbol (recorrido por niveles).
        La altura de un árbol vacío es -1, la de un árbol con solo raíz es 0.
        """
        if self._raiz is None:
            return -1

        altura_actual = -1
        cola: deque[Nodo] = deque([self._raiz])

        while cola:
            altura_actual += 1
            for _ in range(len(cola)):
                nodo = cola.popleft()
                if nodo.izquierdo is not None:
                    cola.append(nodo.izquierdo)
                if nodo.derecho is not None:
                    cola.append(nodo.derecho)

        return altura_actual

    def es_balanceado(self) -> bool:
        """
        Verifica si el árbol está balanceado.
        Un árbol es balanceado si para cada nodo, la diferencia
        de altura entre sus subárboles es a lo sumo 1.

        Recorre el árbol en post-orden iterativo para calcular
        las alturas de abajo hacia arriba.
        """
        alturas: dict[Nodo, int] = {}
        pila: list[Nodo] = []
        actual = self._raiz
        ultimo_visitado: Nodo | None = None

        while pila or actual is not None:
            if actual is not None:
                pila.append(actual)
                actual = actual.izquierdo
            else:
                cima = pila[-1]
                if cima.derecho is not None and ultimo_visitado is not cima.derecho:
                    actual = cima.derecho
                else:
                    alt_izq = alturas[cima.izquierdo] if cima.izquierdo is not None else -1
                    alt_der = alturas[cima.derecho] if cima.derecho is not None else -1
                    if abs(alt_izq - alt_der) > 1:
                        return False
                    alturas[cima] = 1 + max(alt_izq, alt_der)
                    ultimo_visitado = pila.pop()

        return True

    # ------------------------------------------------------------------
    # Recorridos
    # ------------------------------------------------------------------

    def en_orden(self) -> list[Any]:
        """Recorrido en-orden: izq → raíz → der. Produce lista ordenada."""
        resultado: list[Any] = []
        pila: list[Nodo] = []
        actual = self._raiz

        while pila or actual is not None:
            while actual is not None:
                pila.append(actual)
                actual = actual.izquierdo
            actual = pila.pop()
            resultado.append(actual.dato)
            actual = actual.derecho

        return resultado

    def pre_orden(self) -> list[Any]:
        """Recorrido pre-orden: raíz → izq → der."""
        if self._raiz is None:
            return []

        resultado: list[Any] = []
        pila: list[Nodo] = [self._raiz]

        while pila:
            nodo = pila.pop()
            resultado.append(nodo.dato)
            # Derecho primero para que el izquierdo se procese antes (LIFO)
            if nodo.derecho is not None:
                pila.append(nodo.derecho)
            if nodo.izquierdo is not None:
                pila.append(nodo.izquierdo)

        return resultado

    def post_orden(self) -> list[Any]:
        """Recorrido post-orden: izq → der → raíz."""
        if self._raiz is None:
            return []

        pila_recorrido: list[Nodo] = [self._raiz]
        pila_salida: list[Nodo] = []

        while pila_recorrido:
            nodo = pila_recorrido.pop()
            pila_salida.append(nodo)
            if nodo.izquierdo is not None:
                pila_recorrido.append(nodo.izquierdo)
            if nodo.derecho is not None:
                pila_recorrido.append(nodo.derecho)

        return [nodo.dato for nodo in reversed(pila_salida)]

    def por_niveles(self) -> list[Any]:
        """Recorrido por niveles (BFS) usando una cola."""
        if self.esta_vacio():
            return []

        resultado: list[Any] = []
        cola: deque[Nodo] = deque([self._raiz])

        while cola:
            nodo = cola.popleft()
            resultado.append(nodo.dato)
            if nodo.izquierdo is not None:
                cola.append(nodo.izquierdo)
            if nodo.derecho is not None:
                cola.append(nodo.derecho)

        return resultado

    # ------------------------------------------------------------------
    # Visualización
    # ------------------------------------------------------------------

    def imprimir(self) -> None:
        """
        Imprime el árbol en formato visual (rotado 90°).
        Recorrido inverso en-orden: der → raíz → izq.
        """
        pila: list[tuple[Nodo, int]] = []
        actual = self._raiz
        nivel = 0

        while pila or actual is not None:
            while actual is not None:
                pila.append((actual, nivel))
                actual = actual.derecho
                nivel += 1
            actual, nivel = pila.pop()
            print("    " * nivel + f"[{actual.dato}]")
            actual = actual.izquierdo
            nivel += 1


# ------------------------------------------------------------------
# Demo
# ------------------------------------------------------------------

if __name__ == "__main__":
    abb = ArbolBinarioBusqueda()

    valores = [50, 30, 70, 20, 40, 60, 80, 10, 35, 45]
    print("=== Árbol Binario de Búsqueda (iterativo) ===")
    print(f"Insertando: {valores}")
    for v in valores:
        abb.insertar(v)

    print("\nÁrbol (leer de abajo hacia arriba = de izq a der):")
    abb.imprimir()

    print(f"\nAltura: {abb.altura()}")
    print(f"Tamaño: {len(abb)}")
    print(f"Mínimo: {abb.minimo()}")
    print(f"Máximo: {abb.maximo()}")
    print(f"¿Balanceado? {abb.es_balanceado()}")

    print("\nRecorridos:")
    print(f"  En-orden   : {abb.en_orden()}")
    print(f"  Pre-orden  : {abb.pre_orden()}")
    print(f"  Post-orden : {abb.post_orden()}")
    print(f"  Por niveles: {abb.por_niveles()}")

    print(f"\n¿Existe 40? {abb.buscar(40)}")
    print(f"¿Existe 99? {abb.buscar(99)}")

    print("\nEliminando 30 (tiene 2 hijos)...")
    abb.eliminar(30)
    abb.imprimir()
    print(f"En-orden tras eliminar 30: {abb.en_orden()}")

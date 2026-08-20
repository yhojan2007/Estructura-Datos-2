from abc import ABC, abstractmethod
from typing import Any, Optional


class EstructuraDatos(ABC):
    """Interfaz base para todas las estructuras de datos."""
    
    @abstractmethod
    def insertar(self, dato: Any) -> None:
        """Inserta un elemento en la estructura."""
        pass
    
    @abstractmethod
    def eliminar(self, dato: Any) -> None:
        """Elimina un elemento de la estructura."""
        pass
    
    @abstractmethod
    def buscar(self, dato: Any) -> bool:
        """Busca un elemento. Retorna True si existe."""
        pass
    
    @abstractmethod
    def esta_vacia(self) -> bool:
        """Retorna True si la estructura no tiene elementos."""
        pass
    
    @abstractmethod
    def __len__(self) -> int:
        """Retorna la cantidad de elementos."""
        pass


class Nodo:
    """Clase que representa un nodo individual en el árbol binario."""
    
    def __init__(self, dato: Any) -> None:
        """
        Inicializa un nuevo nodo con el dato proporcionado.
        
        Args:
            dato: El valor a almacenar en el nodo.
        """
        self.dato: Any = dato
        self.izquierdo: Optional['Nodo'] = None
        self.derecho: Optional['Nodo'] = None


class ArbolBinarioBusqueda(EstructuraDatos):
    """
    Implementación de un Árbol Binario de Búsqueda (BST).
    
    No admite valores duplicados. Los valores menores se insertan
    a la izquierda del nodo actual y los mayores a la derecha.
    """
    
    def __init__(self) -> None:
        """Inicializa un árbol binario vacío."""
        self.raiz: Optional[Nodo] = None
        self._tamano: int = 0

    def insertar(self, dato: Any) -> None:
        """Inserta un elemento en el árbol."""
        if self.raiz is None:
            self.raiz = Nodo(dato)
            self._tamano += 1
        else:
            self._insertar_recursivo(self.raiz, dato)

    def _insertar_recursivo(self, nodo: Nodo, dato: Any) -> None:
        """Método auxiliar recursivo para insertar un nodo."""
        if dato < nodo.dato:
            if nodo.izquierdo is None:
                nodo.izquierdo = Nodo(dato)
                self._tamano += 1
            else:
                self._insertar_recursivo(nodo.izquierdo, dato)
        elif dato > nodo.dato:
            if nodo.derecho is None:
                nodo.derecho = Nodo(dato)
                self._tamano += 1
            else:
                self._insertar_recursivo(nodo.derecho, dato)

    def eliminar(self, dato: Any) -> None:
        """Elimina un elemento del árbol, si existe."""
        if self.buscar(dato):
            self.raiz = self._eliminar_recursivo(self.raiz, dato)
            self._tamano -= 1

    def _eliminar_recursivo(self, nodo: Optional[Nodo], dato: Any) -> Optional[Nodo]:
        """Método auxiliar recursivo para eliminar un nodo."""
        if nodo is None:
            return None
        
        if dato < nodo.dato:
            nodo.izquierdo = self._eliminar_recursivo(nodo.izquierdo, dato)
        elif dato > nodo.dato:
            nodo.derecho = self._eliminar_recursivo(nodo.derecho, dato)
        else:
            if nodo.izquierdo is None:
                return nodo.derecho
            if nodo.derecho is None:
                return nodo.izquierdo
            
            sucesor = self._obtener_minimo(nodo.derecho)
            nodo.dato = sucesor.dato
            nodo.derecho = self._eliminar_recursivo(nodo.derecho, sucesor.dato)
            
        return nodo

    def _obtener_minimo(self, nodo: Nodo) -> Nodo:
        """Obtiene el nodo con el valor más bajo a partir de un nodo dado."""
        actual = nodo
        while actual.izquierdo is not None:
            actual = actual.izquierdo
        return actual

    def buscar(self, dato: Any) -> bool:
        """Busca un elemento en la estructura."""
        return self._buscar_recursivo(self.raiz, dato)

    def _buscar_recursivo(self, nodo: Optional[Nodo], dato: Any) -> bool:
        """Método auxiliar recursivo para buscar un nodo."""
        if nodo is None:
            return False
        if dato == nodo.dato:
            return True
        if dato < nodo.dato:
            return self._buscar_recursivo(nodo.izquierdo, dato)
        return self._buscar_recursivo(nodo.derecho, dato)

    def esta_vacia(self) -> bool:
        """Verifica si el árbol está vacío."""
        return self.raiz is None

    def __len__(self) -> int:
        """Devuelve la cantidad de elementos almacenados en el árbol."""
        return self._tamano

    def obtener_altura(self) -> int:
        """
        Calcula la altura máxima del árbol.
        (Un árbol vacío tiene altura 0, con solo la raíz tiene altura 1).
        
        :return: Entero que representa la altura del árbol.
        """
        return self._altura_recursiva(self.raiz)

    def _altura_recursiva(self, nodo: Optional[Nodo]) -> int:
        """Método auxiliar para calcular la altura."""
        if nodo is None:
            return 0
        
        altura_izq = self._altura_recursiva(nodo.izquierdo)
        altura_der = self._altura_recursiva(nodo.derecho)
        
        return 1 + max(altura_izq, altura_der)

    def obtener_nivel(self, dato: Any) -> int:
        """
        Encuentra el nivel (profundidad) en el que se encuentra un nodo.
        La raíz se encuentra en el nivel 0.
        
        :param dato: El valor del nodo a evaluar.
        :return: El nivel del nodo si existe, o -1 si no se encuentra.
        """
        return self._nivel_recursivo(self.raiz, dato, 0)

    def _nivel_recursivo(self, nodo: Optional[Nodo], dato: Any, nivel_actual: int) -> int:
        """Método auxiliar para buscar el nivel de un nodo."""
        if nodo is None:
            return -1  # No se encontró el dato
        
        if dato == nodo.dato:
            return nivel_actual
        elif dato < nodo.dato:
            return self._nivel_recursivo(nodo.izquierdo, dato, nivel_actual + 1)
        else:
            return self._nivel_recursivo(nodo.derecho, dato, nivel_actual + 1)


# EJEMPLO DE USO
if __name__ == "__main__":
    # 1. Crear el árbol
    mi_arbol = ArbolBinarioBusqueda()
    print(f"¿El árbol está vacío? {mi_arbol.esta_vacia()}")  # True

    # 2. Insertar datos (estructura balanceada idealmente para el ejemplo)
    datos_a_insertar = [50, 30, 70, 20, 40, 60, 80, 10, 25]
    for dato in datos_a_insertar:
        mi_arbol.insertar(dato)
        
    print(f"\nSe insertaron {len(mi_arbol)} elementos.")
    print(f"¿El árbol está vacío ahora? {mi_arbol.esta_vacia()}")

    # 3. Buscar datos
    print("\n--- Búsquedas ---")
    print(f"¿Existe el número 40? {mi_arbol.buscar(40)}")  # True
    print(f"¿Existe el número 99? {mi_arbol.buscar(99)}")  # False

    # 4. Altura y Nivel
    print("\n--- Altura ---")
    print(f"La altura total del árbol es: {mi_arbol.obtener_altura()}")
    
    # 5. Eliminar datos
    print("\n--- Eliminación ---")
    print("Eliminando el nodo 30 (que tiene dos hijos: 20 y 40)...")
    mi_arbol.eliminar(30)
    print(f"Elementos restantes: {len(mi_arbol)}")
    print(f"¿Existe el número 30 tras eliminarlo? {mi_arbol.buscar(30)}")
"""
Implementación de Grafos en Python
Ejemplos de lista de adyacencia y matriz de adyacencia
"""

from collections import deque
import sys

# ============================================================================
# PARTE 1: REPRESENTACIÓN CON LISTA DE ADYACENCIA
# ============================================================================

class GrafoListaAdyacencia:
    """
    Representación de un grafo usando lista de adyacencia.
    Ideal para grafos dispersos (pocas aristas).
    """
    
    def __init__(self):
        """Inicializa un grafo vacío usando un diccionario."""
        self.grafo = {}
    
    def agregar_vertice(self, vertice):
        """Agrega un vértice al grafo."""
        if vertice not in self.grafo:
            self.grafo[vertice] = []
    
    def agregar_arista(self, u, v, bidireccional=True):
        """
        Agrega una arista entre dos vértices.
        
        Args:
            u: Vértice origen
            v: Vértice destino
            bidireccional: Si True, crea arista en ambas direcciones
        """
        if u not in self.grafo:
            self.agregar_vertice(u)
        if v not in self.grafo:
            self.agregar_vertice(v)
        
        if v not in self.grafo[u]:
            self.grafo[u].append(v)
        
        if bidireccional and u not in self.grafo[v]:
            self.grafo[v].append(u)
    
    def obtener_vecinos(self, vertice):
        """Retorna los vértices adyacentes a un vértice dado."""
        return self.grafo.get(vertice, [])
    
    def __str__(self):
        """Representación en string del grafo."""
        resultado = "Lista de Adyacencia:\n"
        for vertice, vecinos in sorted(self.grafo.items()):
            resultado += f"{vertice}: {vecinos}\n"
        return resultado


# ============================================================================
# PARTE 2: REPRESENTACIÓN CON MATRIZ DE ADYACENCIA
# ============================================================================

class GrafoMatrizAdyacencia:
    """
    Representación de un grafo usando matriz de adyacencia.
    Ideal para grafos densos (muchas aristas).
    """
    
    def __init__(self, num_vertices):
        """Inicializa un grafo con num_vertices vértices."""
        self.num_vertices = num_vertices
        self.matriz = [[0] * num_vertices for _ in range(num_vertices)]
        self.etiquetas = {}  # Mapeo de etiquetas a índices
        self.indices_inversos = {}  # Mapeo de índices a etiquetas
    
    def agregar_vertice(self, etiqueta, indice):
        """Agrega un vértice con etiqueta y asigna un índice."""
        self.etiquetas[etiqueta] = indice
        self.indices_inversos[indice] = etiqueta
    
    def agregar_arista(self, u, v, peso=1, bidireccional=True):
        """
        Agrega una arista entre dos vértices.
        
        Args:
            u: Vértice origen (etiqueta)
            v: Vértice destino (etiqueta)
            peso: Peso de la arista
            bidireccional: Si True, crea arista en ambas direcciones
        """
        if u in self.etiquetas and v in self.etiquetas:
            i = self.etiquetas[u]
            j = self.etiquetas[v]
            self.matriz[i][j] = peso
            
            if bidireccional:
                self.matriz[j][i] = peso
    
    def existe_arista(self, u, v):
        """Verifica si existe una arista entre u y v."""
        if u in self.etiquetas and v in self.etiquetas:
            i = self.etiquetas[u]
            j = self.etiquetas[v]
            return self.matriz[i][j] != 0
        return False
    
    def __str__(self):
        """Representación en string de la matriz."""
        resultado = "Matriz de Adyacencia:\n"
        
        # Encabezado
        resultado += "   "
        for j in range(self.num_vertices):
            resultado += f"{self.indices_inversos[j]:3} "
        resultado += "\n"
        
        # Filas
        for i in range(self.num_vertices):
            resultado += f"{self.indices_inversos[i]}  "
            for j in range(self.num_vertices):
                resultado += f"{self.matriz[i][j]:3} "
            resultado += "\n"
        
        return resultado


# ============================================================================
# PARTE 3: ALGORITMOS DE RECORRIDO
# ============================================================================

class AlgoritmosGrafos:
    """Contiene algoritmos para trabajar con grafos."""
    
    @staticmethod
    def bfs(grafo, inicio):
        """
        Búsqueda en Amplitud (BFS - Breadth-First Search).
        
        Args:
            grafo: GrafoListaAdyacencia
            inicio: Vértice inicial
        
        Returns:
            Lista con el orden de visita de los vértices
        """
        visitado = set()
        cola = deque([inicio])
        resultado = []
        
        visitado.add(inicio)
        
        while cola:
            vertice = cola.popleft()
            resultado.append(vertice)
            
            for vecino in grafo.obtener_vecinos(vertice):
                if vecino not in visitado:
                    cola.append(vecino)
                    visitado.add(vecino)
        
        return resultado
    
    @staticmethod
    def dfs_recursivo(grafo, vertice, visitado=None, resultado=None):
        """
        Búsqueda en Profundidad recursiva (DFS - Depth-First Search).
        
        Args:
            grafo: GrafoListaAdyacencia
            vertice: Vértice actual
            visitado: Set de vértices visitados
            resultado: Lista con el orden de visita
        
        Returns:
            Lista con el orden de visita de los vértices
        """
        if visitado is None:
            visitado = set()
            resultado = []
        
        visitado.add(vertice)
        resultado.append(vertice)
        
        for vecino in grafo.obtener_vecinos(vertice):
            if vecino not in visitado:
                AlgoritmosGrafos.dfs_recursivo(grafo, vecino, visitado, resultado)
        
        return resultado
    
    @staticmethod
    def dfs_iterativo(grafo, inicio):
        """
        Búsqueda en Profundidad iterativa usando pila (DFS).
        
        Args:
            grafo: GrafoListaAdyacencia
            inicio: Vértice inicial
        
        Returns:
            Lista con el orden de visita de los vértices
        """
        visitado = set()
        pila = [inicio]
        resultado = []
        
        while pila:
            vertice = pila.pop()
            
            if vertice not in visitado:
                visitado.add(vertice)
                resultado.append(vertice)
                
                # Agregar vecinos en orden inverso para mantener consistencia
                for vecino in reversed(grafo.obtener_vecinos(vertice)):
                    if vecino not in visitado:
                        pila.append(vecino)
        
        return resultado
    
    @staticmethod
    def detectar_ciclos(grafo, vertice, visitado=None, pila_recursion=None):
        """
        Detecta ciclos en un grafo dirigido.
        
        Args:
            grafo: GrafoListaAdyacencia
            vertice: Vértice a verificar
            visitado: Set de vértices visitados
            pila_recursion: Set de vértices en la pila de recursión actual
        
        Returns:
            True si hay ciclo, False en caso contrario
        """
        if visitado is None:
            visitado = set()
            pila_recursion = set()
        
        visitado.add(vertice)
        pila_recursion.add(vertice)
        
        for vecino in grafo.obtener_vecinos(vertice):
            if vecino not in visitado:
                if AlgoritmosGrafos.detectar_ciclos(grafo, vecino, visitado, pila_recursion):
                    return True
            elif vecino in pila_recursion:
                return True
        
        pila_recursion.remove(vertice)
        return False


# ============================================================================
# PARTE 4: EJEMPLOS DE USO
# ============================================================================

def ejemplo_lista_adyacencia():
    """Ejemplo de uso con lista de adyacencia."""
    print("=" * 60)
    print("EJEMPLO 1: LISTA DE ADYACENCIA")
    print("=" * 60)
    
    grafo = GrafoListaAdyacencia()
    
    # Agregar vértices
    vertices = ['A', 'B', 'C', 'D', 'E']
    for v in vertices:
        grafo.agregar_vertice(v)
    
    # Agregar aristas
    aristas = [('A', 'B'), ('A', 'D'), ('B', 'C'), ('B', 'E'), 
               ('C', 'E'), ('D', 'E')]
    for u, v in aristas:
        grafo.agregar_arista(u, v)
    
    print("\n" + str(grafo))
    
    # Algoritmos
    print("\nBFS desde A:", AlgoritmosGrafos.bfs(grafo, 'A'))
    print("DFS recursivo desde A:", AlgoritmosGrafos.dfs_recursivo(grafo, 'A'))
    print("DFS iterativo desde A:", AlgoritmosGrafos.dfs_iterativo(grafo, 'A'))


def ejemplo_matriz_adyacencia():
    """Ejemplo de uso con matriz de adyacencia."""
    print("\n" + "=" * 60)
    print("EJEMPLO 2: MATRIZ DE ADYACENCIA")
    print("=" * 60)
    
    grafo = GrafoMatrizAdyacencia(5)
    
    # Agregar vértices con etiquetas
    etiquetas = ['A', 'B', 'C', 'D', 'E']
    for i, etiqueta in enumerate(etiquetas):
        grafo.agregar_vertice(etiqueta, i)
    
    # Agregar aristas
    aristas = [('A', 'B'), ('A', 'D'), ('B', 'C'), ('B', 'E'), 
               ('C', 'E'), ('D', 'E')]
    for u, v in aristas:
        grafo.agregar_arista(u, v)
    
    print("\n" + str(grafo))
    
    # Verificar aristas
    print("\nVerificación de aristas:")
    print(f"¿Existe arista A-B? {grafo.existe_arista('A', 'B')}")
    print(f"¿Existe arista A-C? {grafo.existe_arista('A', 'C')}")
    print(f"¿Existe arista B-E? {grafo.existe_arista('B', 'E')}")


def ejemplo_deteccion_ciclos():
    """Ejemplo de detección de ciclos."""
    print("\n" + "=" * 60)
    print("EJEMPLO 3: DETECCIÓN DE CICLOS")
    print("=" * 60)
    
    # Grafo sin ciclos
    grafo1 = GrafoListaAdyacencia()
    for v in ['A', 'B', 'C', 'D']:
        grafo1.agregar_vertice(v)
    
    aristas1 = [('A', 'B'), ('B', 'C'), ('C', 'D')]
    for u, v in aristas1:
        grafo1.agregar_arista(u, v, bidireccional=False)
    
    print("\nGrafo sin ciclos:")
    print(grafo1)
    
    tiene_ciclo = False
    for v in grafo1.grafo:
        if AlgoritmosGrafos.detectar_ciclos(grafo1, v):
            tiene_ciclo = True
            break
    print(f"¿Tiene ciclos? {tiene_ciclo}")
    
    # Grafo con ciclo
    grafo2 = GrafoListaAdyacencia()
    for v in ['A', 'B', 'C', 'D']:
        grafo2.agregar_vertice(v)
    
    aristas2 = [('A', 'B'), ('B', 'C'), ('C', 'D'), ('D', 'A')]
    for u, v in aristas2:
        grafo2.agregar_arista(u, v, bidireccional=False)
    
    print("\nGrafo con ciclo:")
    print(grafo2)
    
    tiene_ciclo = False
    for v in grafo2.grafo:
        if AlgoritmosGrafos.detectar_ciclos(grafo2, v):
            tiene_ciclo = True
            break
    print(f"¿Tiene ciclos? {tiene_ciclo}")


# ============================================================================
# MAIN
# ============================================================================

if __name__ == "__main__":
    print("\n" + "=" * 60)
    print("IMPLEMENTACIÓN COMPLETA DE GRAFOS EN PYTHON")
    print("=" * 60)
    
    ejemplo_lista_adyacencia()
    ejemplo_matriz_adyacencia()
    ejemplo_deteccion_ciclos()
    
    print("\n" + "=" * 60)
    print("FIN DE LOS EJEMPLOS")
    print("=" * 60 + "\n")

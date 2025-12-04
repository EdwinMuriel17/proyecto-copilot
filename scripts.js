// Definición de los posts
const posts = {
    post1: {
        title: "Introducción a los Grafos: Nodos, Aristas y Tipos",
        content: `
            <div class="post-full">
                <h2>Introducción a los Grafos: Nodos, Aristas y Tipos</h2>
                
                <h3>¿Qué es un Grafo?</h3>
                <p>
                    Un <span class="highlight">grafo</span> es una estructura de datos abstracta que se utiliza para representar 
                    relaciones entre objetos. Formalmente, un grafo G se define como un conjunto de dos componentes:
                </p>
                <ul>
                    <li><strong>V (Vértices o Nodos):</strong> Un conjunto de puntos o elementos.</li>
                    <li><strong>E (Aristas o Ejes):</strong> Un conjunto de conexiones entre los vértices.</li>
                </ul>
                
                <div class="info-box">
                    <strong>Notación Matemática:</strong><br>
                    G = (V, E) donde V es el conjunto de vértices y E es el conjunto de aristas.
                </div>

                <h3>Componentes Fundamentales</h3>
                
                <h4>1. Vértices o Nodos</h4>
                <p>
                    Los <strong>vértices</strong> son los elementos básicos del grafo. Cada vértice representa una entidad 
                    o concepto. Por ejemplo:
                </p>
                <ul>
                    <li>En una red social: cada vértice representa una persona.</li>
                    <li>En un mapa: cada vértice representa una ciudad.</li>
                    <li>En una red de computadoras: cada vértice representa un servidor.</li>
                </ul>

                <h4>2. Aristas o Ejes</h4>
                <p>
                    Las <strong>aristas</strong> son las conexiones entre vértices. Cada arista conecta dos vértices 
                    y representa una relación entre ellos. Por ejemplo:
                </p>
                <ul>
                    <li>En una red social: una arista representa una amistad entre dos personas.</li>
                    <li>En un mapa: una arista representa una carretera entre dos ciudades.</li>
                    <li>En una red de computadoras: una arista representa una conexión entre dos servidores.</li>
                </ul>

                <h3>Tipos de Grafos</h3>

                <h4>1. Grafos Dirigidos (Directed Graphs)</h4>
                <p>
                    En un <strong>grafo dirigido</strong>, cada arista tiene una dirección. Se representa como una flecha 
                    que va de un vértice a otro. La dirección importa: una arista de A a B no es lo mismo que una arista de B a A.
                </p>
                <p><strong>Ejemplos de uso:</strong> Redes de citas académicas, flujos de procesos, seguimiento en redes sociales.</p>

                <h4>2. Grafos No Dirigidos (Undirected Graphs)</h4>
                <p>
                    En un <strong>grafo no dirigido</strong>, las aristas no tienen dirección. La conexión es bidireccional: 
                    si hay una arista entre A y B, la relación es simétrica.
                </p>
                <p><strong>Ejemplos de uso:</strong> Redes de amigos, carreteras de doble sentido, moléculas químicas.</p>

                <h4>3. Grafos Ponderados (Weighted Graphs)</h4>
                <p>
                    Los <strong>grafos ponderados</strong> tienen un valor numérico asociado a cada arista. Este valor 
                    se llama <span class="highlight">peso</span> y representa un costo, distancia o capacidad.
                </p>
                <p><strong>Ejemplos de uso:</strong> Mapas con distancias, redes con ancho de banda, costos de transporte.</p>

                <h3>Ejemplo Visual: Grafo No Dirigido con 5 Nodos</h3>
                <div class="diagram">
                    <svg width="400" height="300" viewBox="0 0 400 300" xmlns="http://www.w3.org/2000/svg">
                        <!-- Aristas -->
                        <line x1="100" y1="50" x2="200" y2="100" stroke="#2563eb" stroke-width="2" />
                        <line x1="100" y1="50" x2="150" y2="200" stroke="#2563eb" stroke-width="2" />
                        <line x1="200" y1="100" x2="300" y2="100" stroke="#2563eb" stroke-width="2" />
                        <line x1="200" y1="100" x2="250" y2="200" stroke="#2563eb" stroke-width="2" />
                        <line x1="150" y1="200" x2="250" y2="200" stroke="#2563eb" stroke-width="2" />
                        <line x1="300" y1="100" x2="250" y2="200" stroke="#2563eb" stroke-width="2" />
                        
                        <!-- Vértices -->
                        <circle cx="100" cy="50" r="15" fill="#f59e0b" stroke="#2563eb" stroke-width="2" />
                        <text x="100" y="55" text-anchor="middle" font-weight="bold" fill="white">A</text>
                        
                        <circle cx="200" cy="100" r="15" fill="#f59e0b" stroke="#2563eb" stroke-width="2" />
                        <text x="200" y="105" text-anchor="middle" font-weight="bold" fill="white">B</text>
                        
                        <circle cx="300" cy="100" r="15" fill="#f59e0b" stroke="#2563eb" stroke-width="2" />
                        <text x="300" y="105" text-anchor="middle" font-weight="bold" fill="white">C</text>
                        
                        <circle cx="150" cy="200" r="15" fill="#f59e0b" stroke="#2563eb" stroke-width="2" />
                        <text x="150" y="205" text-anchor="middle" font-weight="bold" fill="white">D</text>
                        
                        <circle cx="250" cy="200" r="15" fill="#f59e0b" stroke="#2563eb" stroke-width="2" />
                        <text x="250" y="205" text-anchor="middle" font-weight="bold" fill="white">E</text>
                    </svg>
                    <p><strong>Grafo No Dirigido:</strong> 5 vértices (A, B, C, D, E) con 6 aristas</p>
                </div>

                <h3>Conceptos Adicionales</h3>

                <h4>Grado de un Vértice</h4>
                <p>
                    El <strong>grado</strong> de un vértice es el número de aristas conectadas a él. En el ejemplo anterior:
                </p>
                <ul>
                    <li>Vértice A: grado 2</li>
                    <li>Vértice B: grado 3</li>
                    <li>Vértice C: grado 2</li>
                    <li>Vértice D: grado 2</li>
                    <li>Vértice E: grado 3</li>
                </ul>

                <h4>Camino y Ciclo</h4>
                <ul>
                    <li><strong>Camino:</strong> Una secuencia de vértices conectados por aristas.</li>
                    <li><strong>Ciclo:</strong> Un camino que comienza y termina en el mismo vértice.</li>
                </ul>

                <div class="success-box">
                    <strong>Conclusión:</strong><br>
                    Los grafos son estructuras fundamentales en ciencias de la computación que permiten modelar 
                    relaciones complejas entre datos. Su comprensión es esencial para resolver problemas de redes, 
                    rutas y conectividad.
                </div>
            </div>
        `
    },

    post2: {
        title: "Representación de Grafos",
        content: `
            <div class="post-full">
                <h2>Representación de Grafos</h2>
                
                <h3>Introducción</h3>
                <p>
                    Una vez que comprendemos qué son los grafos, debemos aprender cómo almacenarlos en la memoria 
                    de una computadora. Existen dos formas principales de representar un grafo, cada una con sus 
                    propias ventajas y desventajas según el caso de uso.
                </p>

                <h3>1. Lista de Adyacencia</h3>
                
                <h4>Concepto</h4>
                <p>
                    Una <span class="highlight">lista de adyacencia</span> es una colección de listas donde cada vértice 
                    tiene una lista de todos los vértices adyacentes (conectados) a él.
                </p>

                <h4>Representación</h4>
                <p>Para un grafo con n vértices, se mantiene un array o diccionario donde:</p>
                <ul>
                    <li>Cada índice representa un vértice.</li>
                    <li>Cada valor es una lista de vértices conectados al vértice correspondiente.</li>
                </ul>

                <h4>Ejemplo en Python</h4>
                <div class="code-block">
# Lista de Adyacencia usando un Diccionario
grafo = {
    'A': ['B', 'D'],
    'B': ['A', 'C', 'E'],
    'C': ['B', 'E'],
    'D': ['A', 'E'],
    'E': ['B', 'C', 'D']
}
                </div>

                <h4>Ejemplo en Python (usando list)</h4>
                <div class="code-block">
# Lista de Adyacencia usando una Lista
# Suponiendo vértices numerados del 0 al 4
grafo = [
    [1, 3],      # Vértice 0 conectado a 1 y 3
    [0, 2, 4],   # Vértice 1 conectado a 0, 2 y 4
    [1, 4],      # Vértice 2 conectado a 1 y 4
    [0, 4],      # Vértice 3 conectado a 0 y 4
    [1, 2, 3]    # Vértice 4 conectado a 1, 2 y 3
]
                </div>

                <h4>Ventajas de la Lista de Adyacencia</h4>
                <ul>
                    <li><strong>Eficiencia de Espacio:</strong> Usa O(V + E) espacio, ideal para grafos dispersos.</li>
                    <li><strong>Iteración Eficiente:</strong> Fácil recorrer todos los vecinos de un vértice.</li>
                    <li><strong>Flexible:</strong> Permite grafos con números de vértices dinámicos.</li>
                </ul>

                <h4>Desventajas</h4>
                <ul>
                    <li>Consultar si existe una arista entre dos vértices requiere buscar en la lista: O(grado del vértice).</li>
                </ul>

                <h3>2. Matriz de Adyacencia</h3>
                
                <h4>Concepto</h4>
                <p>
                    Una <span class="highlight">matriz de adyacencia</span> es una matriz cuadrada de tamaño V × V 
                    donde V es el número de vértices. Cada celda [i][j] indica si existe una arista entre el vértice i y j.
                </p>

                <h4>Representación</h4>
                <ul>
                    <li>Para un grafo no ponderado: 1 indica arista, 0 indica no arista.</li>
                    <li>Para un grafo ponderado: el valor de la celda es el peso de la arista, 0 o ∞ indica no arista.</li>
                </ul>

                <h4>Ejemplo en Python (Grafo No Ponderado)</h4>
                <div class="code-block">
# Matriz de Adyacencia (Grafo No Ponderado)
# Vértices: 0=A, 1=B, 2=C, 3=D, 4=E
grafo = [
    [0, 1, 0, 1, 0],  # A
    [1, 0, 1, 0, 1],  # B
    [0, 1, 0, 0, 1],  # C
    [1, 0, 0, 0, 1],  # D
    [0, 1, 1, 1, 0]   # E
]
                </div>

                <h4>Ejemplo en Python (Grafo Ponderado)</h4>
                <div class="code-block">
# Matriz de Adyacencia (Grafo Ponderado)
# 0 indica no existe arista
import math
grafo = [
    [0,     5,  math.inf, 2,  math.inf],
    [5,     0,  3,        math.inf, 1],
    [math.inf, 3, 0,      math.inf, 4],
    [2,     math.inf, math.inf, 0, 6],
    [math.inf, 1, 4,      6,  0]
]
                </div>

                <h4>Ventajas de la Matriz de Adyacencia</h4>
                <ul>
                    <li><strong>Consulta Rápida:</strong> Verificar si existe arista entre i y j es O(1).</li>
                    <li><strong>Simple de Implementar:</strong> Muy clara y directa.</li>
                    <li><strong>Operaciones de Matriz:</strong> Permite usar álgebra lineal para análisis.</li>
                </ul>

                <h4>Desventajas</h4>
                <ul>
                    <li><strong>Eficiencia de Espacio:</strong> Usa O(V²) espacio, ineficiente para grafos dispersos.</li>
                    <li><strong>Tamaño Fijo:</strong> Difícil modificar si los vértices cambian dinámicamente.</li>
                </ul>

                <h3>Comparación Visual</h3>
                <div class="diagram">
                    <svg width="500" height="400" viewBox="0 0 500 400" xmlns="http://www.w3.org/2000/svg">
                        <!-- Grafo Original -->
                        <text x="250" y="30" text-anchor="middle" font-size="18" font-weight="bold">Grafo Original</text>
                        <line x1="80" y1="80" x2="150" y2="120" stroke="#2563eb" stroke-width="2" />
                        <line x1="80" y1="80" x2="130" y2="170" stroke="#2563eb" stroke-width="2" />
                        <line x1="150" y1="120" x2="220" y2="120" stroke="#2563eb" stroke-width="2" />
                        <circle cx="80" cy="80" r="12" fill="#f59e0b" />
                        <text x="80" y="85" text-anchor="middle" font-size="12" font-weight="bold" fill="white">0</text>
                        <circle cx="150" cy="120" r="12" fill="#f59e0b" />
                        <text x="150" y="125" text-anchor="middle" font-size="12" font-weight="bold" fill="white">1</text>
                        <circle cx="220" cy="120" r="12" fill="#f59e0b" />
                        <text x="220" y="125" text-anchor="middle" font-size="12" font-weight="bold" fill="white">2</text>
                        <circle cx="130" cy="170" r="12" fill="#f59e0b" />
                        <text x="130" y="175" text-anchor="middle" font-size="12" font-weight="bold" fill="white">3</text>

                        <!-- Lista de Adyacencia -->
                        <text x="80" y="250" text-anchor="start" font-size="14" font-weight="bold">Lista de Adyacencia:</text>
                        <text x="80" y="275" text-anchor="start" font-size="12">0: [1, 3]</text>
                        <text x="80" y="295" text-anchor="start" font-size="12">1: [0, 2]</text>
                        <text x="80" y="315" text-anchor="start" font-size="12">2: [1]</text>
                        <text x="80" y="335" text-anchor="start" font-size="12">3: [0]</text>

                        <!-- Matriz de Adyacencia -->
                        <text x="300" y="250" text-anchor="start" font-size="14" font-weight="bold">Matriz de Adyacencia:</text>
                        <rect x="300" y="260" width="150" height="100" fill="none" stroke="#2563eb" stroke-width="1" />
                        <text x="310" y="280" font-size="11" font-family="monospace">  0 1 2 3</text>
                        <text x="310" y="295" font-size="11" font-family="monospace">0 0 1 0 1</text>
                        <text x="310" y="310" font-size="11" font-family="monospace">1 1 0 1 0</text>
                        <text x="310" y="325" font-size="11" font-family="monospace">2 0 1 0 0</text>
                        <text x="310" y="340" font-size="11" font-family="monospace">3 1 0 0 0</text>
                    </svg>
                    <p><strong>Comparación:</strong> El mismo grafo representado de dos formas diferentes</p>
                </div>

                <h3>¿Cuál Usar?</h3>
                <div class="info-box">
                    <strong>Usa Lista de Adyacencia cuando:</strong><br>
                    - El grafo es disperso (pocas aristas respecto a V²)<br>
                    - Necesitas iterar sobre vecinos frecuentemente<br>
                    - El número de vértices puede cambiar
                </div>

                <div class="info-box">
                    <strong>Usa Matriz de Adyacencia cuando:</strong><br>
                    - El grafo es denso (muchas aristas)<br>
                    - Necesitas consultar rápidamente si existe una arista<br>
                    - El número de vértices es fijo y relativamente pequeño<br>
                    - Necesitas aplicar algoritmos de álgebra lineal
                </div>

                <div class="success-box">
                    <strong>Conclusión:</strong><br>
                    La elección entre lista y matriz de adyacencia depende de las características del problema 
                    y las operaciones que necesites realizar con mayor frecuencia.
                </div>
            </div>
        `
    },

    post3: {
        title: "Algoritmos Fundamentales de Recorrido",
        content: `
            <div class="post-full">
                <h2>Algoritmos Fundamentales de Recorrido</h2>
                
                <h3>Introducción</h3>
                <p>
                    Los algoritmos de recorrido son técnicas fundamentales para explorar grafos. Permiten visitar 
                    todos los vértices de un grafo de manera sistemática. Los dos algoritmos más importantes son 
                    <span class="highlight">BFS (Breadth-First Search)</span> y 
                    <span class="highlight">DFS (Depth-First Search)</span>.
                </p>

                <h3>1. Búsqueda en Amplitud (BFS - Breadth-First Search)</h3>
                
                <h4>Concepto</h4>
                <p>
                    BFS es un algoritmo que explora el grafo <strong>nivel por nivel</strong>. Comienza desde un vértice 
                    inicial y explora todos sus vecinos antes de pasar a los vecinos de esos vecinos.
                </p>

                <h4>Características</h4>
                <ul>
                    <li>Utiliza una <strong>cola (queue)</strong> para mantener el orden de exploración.</li>
                    <li>Explora primero los vértices más cercanos (en términos de número de aristas).</li>
                    <li>Ideal para encontrar el camino más corto en grafos no ponderados.</li>
                    <li>Complejidad temporal: O(V + E)</li>
                </ul>

                <h4>Algoritmo (Pseudocódigo)</h4>
                <div class="code-block">
BFS(grafo, inicio):
    cola ← nueva Cola()
    visitado ← conjunto vacío
    
    cola.encolar(inicio)
    visitado.agregar(inicio)
    
    mientras cola no esté vacía:
        vertice ← cola.desencolar()
        procesar(vertice)
        
        para cada vecino en grafo[vertice]:
            si vecino no está en visitado:
                cola.encolar(vecino)
                visitado.agregar(vecino)
                </div>

                <h4>Implementación en Python</h4>
                <div class="code-block">
from collections import deque

def bfs(grafo, inicio):
    """
    Realiza una búsqueda en amplitud en el grafo.
    grafo: diccionario con lista de adyacencia
    inicio: vértice inicial
    """
    cola = deque([inicio])
    visitado = {inicio}
    resultado = []
    
    while cola:
        vertice = cola.popleft()
        resultado.append(vertice)
        
        for vecino in grafo[vertice]:
            if vecino not in visitado:
                cola.append(vecino)
                visitado.add(vecino)
    
    return resultado

# Ejemplo
grafo = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

print(bfs(grafo, 'A'))  # Salida: ['A', 'B', 'C', 'D', 'E', 'F']
                </div>

                <h4>Visualización del Proceso BFS</h4>
                <div class="diagram">
                    <p><strong>Paso a paso:</strong></p>
                    <svg width="450" height="250" viewBox="0 0 450 250" xmlns="http://www.w3.org/2000/svg">
                        <!-- Grafo -->
                        <line x1="80" y1="80" x2="150" y2="80" stroke="#2563eb" stroke-width="2" />
                        <line x1="80" y1="80" x2="110" y2="150" stroke="#2563eb" stroke-width="2" />
                        <line x1="150" y1="80" x2="180" y2="150" stroke="#2563eb" stroke-width="2" />
                        <line x1="110" y1="150" x2="180" y2="150" stroke="#2563eb" stroke-width="2" />
                        
                        <circle cx="80" cy="80" r="12" fill="#f59e0b" />
                        <text x="80" y="85" text-anchor="middle" font-size="12" font-weight="bold" fill="white">A</text>
                        
                        <circle cx="150" cy="80" r="12" fill="#f59e0b" />
                        <text x="150" y="85" text-anchor="middle" font-size="12" font-weight="bold" fill="white">B</text>
                        
                        <circle cx="110" cy="150" r="12" fill="#f59e0b" />
                        <text x="110" y="155" text-anchor="middle" font-size="12" font-weight="bold" fill="white">C</text>
                        
                        <circle cx="180" cy="150" r="12" fill="#f59e0b" />
                        <text x="180" y="155" text-anchor="middle" font-size="12" font-weight="bold" fill="white">D</text>
                        
                        <!-- Orden de visita -->
                        <text x="20" y="200" font-size="12" font-weight="bold">Orden BFS:</text>
                        <text x="20" y="220" font-size="11">1. A (inicio)</text>
                        <text x="120" y="220" font-size="11">2. B, C</text>
                        <text x="250" y="220" font-size="11">3. D</text>
                    </svg>
                </div>

                <h3>2. Búsqueda en Profundidad (DFS - Depth-First Search)</h3>
                
                <h4>Concepto</h4>
                <p>
                    DFS es un algoritmo que explora el grafo <strong>lo más profundo posible</strong> antes de retroceder. 
                    Comienza desde un vértice inicial y sigue un camino hasta el final antes de explorar otros caminos.
                </p>

                <h4>Características</h4>
                <ul>
                    <li>Utiliza una <strong>pila (stack)</strong> o <strong>recursión</strong>.</li>
                    <li>Explora un camino completamente antes de pasar a otro.</li>
                    <li>Útil para detectar ciclos y componentes conexas.</li>
                    <li>Complejidad temporal: O(V + E)</li>
                </ul>

                <h4>Algoritmo (Pseudocódigo)</h4>
                <div class="code-block">
DFS(grafo, vertice, visitado):
    visitado.agregar(vertice)
    procesar(vertice)
    
    para cada vecino en grafo[vertice]:
        si vecino no está en visitado:
            DFS(grafo, vecino, visitado)
                </div>

                <h4>Implementación en Python (Recursiva)</h4>
                <div class="code-block">
def dfs_recursivo(grafo, vertice, visitado=None):
    """
    Realiza una búsqueda en profundidad recursiva.
    """
    if visitado is None:
        visitado = set()
    
    visitado.add(vertice)
    resultado = [vertice]
    
    for vecino in grafo[vertice]:
        if vecino not in visitado:
            resultado.extend(dfs_recursivo(grafo, vecino, visitado))
    
    return resultado

# Ejemplo
grafo = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

print(dfs_recursivo(grafo, 'A'))  # Salida: ['A', 'B', 'D', 'E', 'F', 'C']
                </div>

                <h4>Implementación en Python (Iterativa)</h4>
                <div class="code-block">
def dfs_iterativo(grafo, inicio):
    """
    Realiza una búsqueda en profundidad iterativa usando pila.
    """
    pila = [inicio]
    visitado = {inicio}
    resultado = []
    
    while pila:
        vertice = pila.pop()
        resultado.append(vertice)
        
        for vecino in reversed(grafo[vertice]):
            if vecino not in visitado:
                pila.append(vecino)
                visitado.add(vecino)
    
    return resultado
                </div>

                <h4>Visualización del Proceso DFS</h4>
                <div class="diagram">
                    <p><strong>Paso a paso:</strong></p>
                    <svg width="450" height="250" viewBox="0 0 450 250" xmlns="http://www.w3.org/2000/svg">
                        <!-- Grafo -->
                        <line x1="80" y1="80" x2="150" y2="80" stroke="#2563eb" stroke-width="2" />
                        <line x1="80" y1="80" x2="110" y2="150" stroke="#2563eb" stroke-width="2" />
                        <line x1="150" y1="80" x2="180" y2="150" stroke="#2563eb" stroke-width="2" />
                        <line x1="110" y1="150" x2="180" y2="150" stroke="#2563eb" stroke-width="2" />
                        
                        <circle cx="80" cy="80" r="12" fill="#f59e0b" />
                        <text x="80" y="85" text-anchor="middle" font-size="12" font-weight="bold" fill="white">A</text>
                        
                        <circle cx="150" cy="80" r="12" fill="#f59e0b" />
                        <text x="150" y="85" text-anchor="middle" font-size="12" font-weight="bold" fill="white">B</text>
                        
                        <circle cx="110" cy="150" r="12" fill="#f59e0b" />
                        <text x="110" y="155" text-anchor="middle" font-size="12" font-weight="bold" fill="white">C</text>
                        
                        <circle cx="180" cy="150" r="12" fill="#f59e0b" />
                        <text x="180" y="155" text-anchor="middle" font-size="12" font-weight="bold" fill="white">D</text>
                        
                        <!-- Orden de visita -->
                        <text x="20" y="200" font-size="12" font-weight="bold">Orden DFS:</text>
                        <text x="20" y="220" font-size="11">1. A (inicio)</text>
                        <text x="120" y="220" font-size="11">2. B</text>
                        <text x="170" y="220" font-size="11">3. D, C</text>
                    </svg>
                </div>

                <h3>Comparación BFS vs DFS</h3>
                <table border="1" style="width: 100%; border-collapse: collapse; margin: 1.5rem 0;">
                    <tr style="background-color: #dbeafe;">
                        <th style="padding: 10px; text-align: left;"><strong>Aspecto</strong></th>
                        <th style="padding: 10px; text-align: left;"><strong>BFS</strong></th>
                        <th style="padding: 10px; text-align: left;"><strong>DFS</strong></th>
                    </tr>
                    <tr>
                        <td style="padding: 10px;">Estructura</td>
                        <td style="padding: 10px;">Cola (FIFO)</td>
                        <td style="padding: 10px;">Pila (LIFO) o Recursión</td>
                    </tr>
                    <tr style="background-color: #f9fafb;">
                        <td style="padding: 10px;">Exploración</td>
                        <td style="padding: 10px;">Por niveles</td>
                        <td style="padding: 10px;">Por profundidad</td>
                    </tr>
                    <tr>
                        <td style="padding: 10px;">Camino más corto</td>
                        <td style="padding: 10px;">Sí (sin pesos)</td>
                        <td style="padding: 10px;">No garantizado</td>
                    </tr>
                    <tr style="background-color: #f9fafb;">
                        <td style="padding: 10px;">Espacio</td>
                        <td style="padding: 10px;">O(V) en peor caso</td>
                        <td style="padding: 10px;">O(h) profundidad</td>
                    </tr>
                    <tr>
                        <td style="padding: 10px;">Uso común</td>
                        <td style="padding: 10px;">Distancias, niveles</td>
                        <td style="padding: 10px;">Ciclos, topología</td>
                    </tr>
                </table>

                <h3>Aplicaciones Prácticas</h3>
                
                <h4>Aplicaciones de BFS</h4>
                <ul>
                    <li>Encontrar el camino más corto en redes sociales</li>
                    <li>Análisis de redes y conectividad</li>
                    <li>Búsqueda en laberintos</li>
                    <li>Resolución de puzzles (como el cubo de Rubik)</li>
                </ul>

                <h4>Aplicaciones de DFS</h4>
                <ul>
                    <li>Detectar ciclos en grafos</li>
                    <li>Ordenamiento topológico</li>
                    <li>Resolver problemas de backtracking</li>
                    <li>Análisis de conectividad fuerte en grafos dirigidos</li>
                </ul>

                <div class="success-box">
                    <strong>Conclusión:</strong><br>
                    BFS y DFS son algoritmos fundamentales en el estudio de grafos. La elección entre uno u otro 
                    depende del problema específico y de lo que necesites investigar del grafo. Ambos tienen 
                    complejidad O(V + E) y son esenciales para cualquier programador.
                </div>
            </div>
        `
    }
};

// Función para mostrar un post completo
function showPost(postId) {
    const modal = document.getElementById('postModal');
    const postContent = document.getElementById('postContent');
    const post = posts[postId];
    
    if (post) {
        postContent.innerHTML = post.content;
        modal.classList.add('active');
        document.body.style.overflow = 'hidden'; // Prevenir scroll del body
    }
}

// Función para cerrar el modal
function closePost() {
    const modal = document.getElementById('postModal');
    modal.classList.remove('active');
    document.body.style.overflow = 'auto';
}

// Cerrar modal al hacer clic fuera del contenido
window.onclick = function(event) {
    const modal = document.getElementById('postModal');
    if (event.target === modal) {
        closePost();
    }
}

// Cerrar modal con tecla Escape
document.addEventListener('keydown', function(event) {
    if (event.key === 'Escape') {
        closePost();
    }
});

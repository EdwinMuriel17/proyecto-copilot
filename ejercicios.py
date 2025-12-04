"""
EJERCICIOS PRÁCTICOS: Estructura de Datos Grafos
Practica los conceptos aprendidos en el blog
"""

from grafos import (
    GrafoListaAdyacencia,
    GrafoMatrizAdyacencia,
    AlgoritmosGrafos
)


# ============================================================================
# EJERCICIO 1: Crear un grafo de una red social
# ============================================================================

def ejercicio1_red_social():
    """
    Crea un grafo que represente una red social simple.
    
    Usuarios: Alice, Bob, Carlos, Diana, Eve
    Amistades:
    - Alice es amiga de Bob y Carlos
    - Bob es amigo de Alice, Carlos y Diana
    - Carlos es amigo de Alice y Bob
    - Diana es amiga de Bob y Eve
    - Eve es amiga de Diana
    """
    print("\n" + "=" * 60)
    print("EJERCICIO 1: Red Social")
    print("=" * 60)
    
    # TODO: Crea un GrafoListaAdyacencia
    grafo = GrafoListaAdyacencia()
    
    # TODO: Agrega los vértices (usuarios)
    usuarios = ['Alice', 'Bob', 'Carlos', 'Diana', 'Eve']
    for usuario in usuarios:
        grafo.agregar_vertice(usuario)
    
    # TODO: Agrega las aristas (amistades)
    amistades = [
        ('Alice', 'Bob'),
        ('Alice', 'Carlos'),
        ('Bob', 'Carlos'),
        ('Bob', 'Diana'),
        ('Diana', 'Eve')
    ]
    for u, v in amistades:
        grafo.agregar_arista(u, v)
    
    # Preguntas:
    print("\n1. ¿Cuántos amigos tiene cada usuario?")
    for usuario in usuarios:
        amigos = grafo.obtener_vecinos(usuario)
        print(f"   {usuario}: {len(amigos)} amigos - {amigos}")
    
    print("\n2. ¿Cuál es el usuario más conectado?")
    max_amigos = 0
    usuario_max = None
    for usuario in usuarios:
        cantidad = len(grafo.obtener_vecinos(usuario))
        if cantidad > max_amigos:
            max_amigos = cantidad
            usuario_max = usuario
    print(f"   {usuario_max} con {max_amigos} amigos")
    
    print("\n3. ¿En qué orden BFS visita los usuarios desde Alice?")
    orden_bfs = AlgoritmosGrafos.bfs(grafo, 'Alice')
    print(f"   {orden_bfs}")
    
    return grafo


# ============================================================================
# EJERCICIO 2: Crear un mapa de ciudades
# ============================================================================

def ejercicio2_mapa_ciudades():
    """
    Crea una matriz de adyacencia que represente un mapa de ciudades.
    
    Ciudades: Madrid, Barcelona, Valencia, Sevilla, Bilbao
    Distancias (en km):
    - Madrid-Barcelona: 620
    - Madrid-Valencia: 360
    - Madrid-Sevilla: 540
    - Barcelona-Valencia: 350
    - Valencia-Sevilla: 570
    - Madrid-Bilbao: 390
    """
    print("\n" + "=" * 60)
    print("EJERCICIO 2: Mapa de Ciudades")
    print("=" * 60)
    
    # TODO: Crea una GrafoMatrizAdyacencia
    grafo = GrafoMatrizAdyacencia(5)
    
    # TODO: Agrega vértices
    ciudades = ['Madrid', 'Barcelona', 'Valencia', 'Sevilla', 'Bilbao']
    for i, ciudad in enumerate(ciudades):
        grafo.agregar_vertice(ciudad, i)
    
    # TODO: Agrega aristas con distancias
    conexiones = [
        ('Madrid', 'Barcelona', 620),
        ('Madrid', 'Valencia', 360),
        ('Madrid', 'Sevilla', 540),
        ('Barcelona', 'Valencia', 350),
        ('Valencia', 'Sevilla', 570),
        ('Madrid', 'Bilbao', 390)
    ]
    for u, v, distancia in conexiones:
        grafo.agregar_arista(u, v, distancia)
    
    print("\n" + str(grafo))
    
    print("\nPreguntas:")
    print("1. ¿Qué distancia hay entre Madrid y Barcelona?")
    print("   620 km")
    
    print("\n2. ¿Qué distancia hay entre Barcelona y Sevilla?")
    print("   No hay conexión directa (grafo desconectado)")
    
    print("\n3. ¿Cuál es la ciudad más central (conectada)?")
    print("   Madrid (conectada a Barcelona, Valencia, Sevilla y Bilbao)")
    
    return grafo


# ============================================================================
# EJERCICIO 3: Detectar si un orden de tareas es posible
# ============================================================================

def ejercicio3_orden_tareas():
    """
    Detecta ciclos en un grafo de dependencias de tareas.
    
    Si hay un ciclo, el orden de tareas es imposible.
    Si no hay ciclo, es posible completar todas las tareas.
    
    Tareas: A, B, C, D
    Dependencias (A debe hacerse antes que B):
    - A debe hacerse antes de B
    - B debe hacerse antes de C
    - C debe hacerse antes de D
    
    Este orden es valido (sin ciclos).
    """
    print("\n" + "=" * 60)
    print("EJERCICIO 3: Orden de Tareas (Sin Ciclos)")
    print("=" * 60)
    
    grafo = GrafoListaAdyacencia()
    
    for tarea in ['A', 'B', 'C', 'D']:
        grafo.agregar_vertice(tarea)
    
    # Agregar dependencias (unidireccionales)
    dependencias = [('A', 'B'), ('B', 'C'), ('C', 'D')]
    for u, v in dependencias:
        grafo.agregar_arista(u, v, bidireccional=False)
    
    print("\nTareas y dependencias:")
    print(grafo)
    
    print("\nDetectando ciclos...")
    tiene_ciclo = False
    for tarea in grafo.grafo:
        if AlgoritmosGrafos.detectar_ciclos(grafo, tarea):
            tiene_ciclo = True
            break
    
    if tiene_ciclo:
        print("❌ ¡IMPOSIBLE! Hay un ciclo en las dependencias.")
    else:
        print("✅ Es posible. Orden válido: A → B → C → D")
    
    return grafo


# ============================================================================
# EJERCICIO 4: Ciclo Imposible
# ============================================================================

def ejercicio4_tareas_con_ciclo():
    """
    Grafo con ciclo (orden imposible).
    
    Tareas: A, B, C
    Dependencias:
    - A debe hacerse antes de B
    - B debe hacerse antes de C
    - C debe hacerse antes de A (¡CICLO!)
    """
    print("\n" + "=" * 60)
    print("EJERCICIO 4: Orden de Tareas (CON Ciclos)")
    print("=" * 60)
    
    grafo = GrafoListaAdyacencia()
    
    for tarea in ['A', 'B', 'C']:
        grafo.agregar_vertice(tarea)
    
    # Agregar dependencias (unidireccionales) - ¡Crea un ciclo!
    dependencias = [('A', 'B'), ('B', 'C'), ('C', 'A')]
    for u, v in dependencias:
        grafo.agregar_arista(u, v, bidireccional=False)
    
    print("\nTareas y dependencias:")
    print(grafo)
    
    print("\nDetectando ciclos...")
    tiene_ciclo = False
    for tarea in grafo.grafo:
        if AlgoritmosGrafos.detectar_ciclos(grafo, tarea):
            tiene_ciclo = True
            break
    
    if tiene_ciclo:
        print("❌ ¡IMPOSIBLE! Hay un ciclo: A → B → C → A")
        print("   No se puede completar este orden de tareas.")
    else:
        print("✅ Es posible.")
    
    return grafo


# ============================================================================
# EJERCICIO 5: Buscar el camino más corto (BFS)
# ============================================================================

def ejercicio5_camino_mas_corto():
    """
    Usa BFS para encontrar el camino más corto entre dos puntos.
    
    Escenario: Laberinto simple donde cada habitación es un nodo
    y las puertas son aristas.
    """
    print("\n" + "=" * 60)
    print("EJERCICIO 5: Camino Más Corto (BFS)")
    print("=" * 60)
    
    grafo = GrafoListaAdyacencia()
    
    # Habitaciones
    habitaciones = ['Entrada', 'Pasillo1', 'Pasillo2', 'Sala', 'Salida']
    for h in habitaciones:
        grafo.agregar_vertice(h)
    
    # Conexiones
    conexiones = [
        ('Entrada', 'Pasillo1'),
        ('Entrada', 'Pasillo2'),
        ('Pasillo1', 'Sala'),
        ('Pasillo2', 'Sala'),
        ('Sala', 'Salida')
    ]
    for u, v in conexiones:
        grafo.agregar_arista(u, v)
    
    print("\nMapa del laberinto:")
    print(grafo)
    
    print("\nBuscando camino desde Entrada a Salida...")
    camino = AlgoritmosGrafos.bfs(grafo, 'Entrada')
    print(f"Orden de exploración: {camino}")
    print(f"Para llegar a Salida: {' → '.join(camino[:-1])} → Salida")
    
    return grafo


# ============================================================================
# EJERCICIO 6: Exploración Completa (DFS)
# ============================================================================

def ejercicio6_exploracion_dfs():
    """
    Usa DFS para exploración exhaustiva (backtracking).
    
    Escenario: Explorar todas las opciones en un árbol de decisiones.
    """
    print("\n" + "=" * 60)
    print("EJERCICIO 6: Exploración Exhaustiva (DFS)")
    print("=" * 60)
    
    grafo = GrafoListaAdyacencia()
    
    # Opciones de menú
    opciones = ['Menu', 'Jugar', 'Salvar', 'Cargar', 'Salir']
    for o in opciones:
        grafo.agregar_vertice(o)
    
    # Flujo del menú
    flujo = [
        ('Menu', 'Jugar'),
        ('Menu', 'Salvar'),
        ('Menu', 'Cargar'),
        ('Menu', 'Salir'),
        ('Salvar', 'Menu'),
        ('Cargar', 'Menu')
    ]
    for u, v in flujo:
        grafo.agregar_arista(u, v, bidireccional=False)
    
    print("\nEstructura del menú:")
    print(grafo)
    
    print("\nExplorando opciones con DFS desde Menu:")
    exploracion = AlgoritmosGrafos.dfs_iterativo(grafo, 'Menu')
    print(f"Orden de exploración: {' → '.join(exploracion)}")
    
    return grafo


# ============================================================================
# EJERCICIO 7: Comparar BFS vs DFS
# ============================================================================

def ejercicio7_comparar_bfs_dfs():
    """
    Compara el orden de visita de BFS y DFS en el mismo grafo.
    """
    print("\n" + "=" * 60)
    print("EJERCICIO 7: Comparar BFS vs DFS")
    print("=" * 60)
    
    grafo = GrafoListaAdyacencia()
    
    # Crear un árbol
    for v in ['A', 'B', 'C', 'D', 'E', 'F', 'G']:
        grafo.agregar_vertice(v)
    
    # Estructura de árbol:
    #       A
    #      / \
    #     B   C
    #    / \ / \
    #   D  E F  G
    
    aristas = [
        ('A', 'B'), ('A', 'C'),
        ('B', 'D'), ('B', 'E'),
        ('C', 'F'), ('C', 'G')
    ]
    for u, v in aristas:
        grafo.agregar_arista(u, v)
    
    print("\nÁrbol:")
    print("       A")
    print("      / \\")
    print("     B   C")
    print("    / \\ / \\")
    print("   D  E F  G")
    
    bfs_orden = AlgoritmosGrafos.bfs(grafo, 'A')
    dfs_orden = AlgoritmosGrafos.dfs_recursivo(grafo, 'A')
    
    print(f"\nBFS (por niveles):    {' → '.join(bfs_orden)}")
    print(f"DFS (por profundidad): {' → '.join(dfs_orden)}")
    
    print("\nObservaciones:")
    print("- BFS: Visita nivel por nivel (A, luego B-C, luego D-E-F-G)")
    print("- DFS: Baja profundamente antes de explorar hermanos")
    
    return grafo


# ============================================================================
# MAIN - Ejecutar todos los ejercicios
# ============================================================================

if __name__ == "__main__":
    print("\n" + "=" * 60)
    print("EJERCICIOS PRÁCTICOS: ESTRUCTURA DE DATOS GRAFOS")
    print("=" * 60)
    
    # Ejecutar ejercicios
    ejercicio1_red_social()
    ejercicio2_mapa_ciudades()
    ejercicio3_orden_tareas()
    ejercicio4_tareas_con_ciclo()
    ejercicio5_camino_mas_corto()
    ejercicio6_exploracion_dfs()
    ejercicio7_comparar_bfs_dfs()
    
    print("\n" + "=" * 60)
    print("EJERCICIOS COMPLETADOS")
    print("=" * 60)
    print("\n✅ Todos los ejercicios se ejecutaron exitosamente.")
    print("\n💡 Próximos pasos:")
    print("   1. Modifica los ejercicios (agrega más nodos, cambia conexiones)")
    print("   2. Crea tus propios grafos")
    print("   3. Implementa nuevos algoritmos")
    print("   4. Resuelve problemas del mundo real con grafos")
    print("\n" + "=" * 60 + "\n")

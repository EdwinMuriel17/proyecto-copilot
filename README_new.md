# 📊 Blog Técnico: Grafos - Estructura de Datos

> Un blog web completo dedicado a la estructura de datos **Grafos**, con artículos técnicos, diagramas visuales y ejemplos de código en Python.

## 🎯 Objetivo

Este proyecto combina el desarrollo de contenido técnico de alta calidad con la aplicación de herramientas de desarrollo web modernas (HTML/CSS/JavaScript) y control de versiones (Git/GitHub).

## 📝 Artículos Incluidos

### 1. **Introducción a los Grafos: Nodos, Aristas y Tipos**
- Definición formal de un grafo
- Conceptos clave: vértices y aristas
- Tipos de grafos (dirigidos, no dirigidos, ponderados)
- Diagrama visual de un grafo no dirigido con 5 nodos
- Conceptos de grado, camino y ciclo

### 2. **Representación de Grafos**
- **Lista de Adyacencia**: Eficiencia de espacio para grafos dispersos
  - Implementación con diccionario
  - Implementación con listas
- **Matriz de Adyacencia**: Eficiencia de tiempo para consultas
  - Grafos no ponderados
  - Grafos ponderados
- Comparación visual de ambas representaciones
- Guía de cuándo usar cada una

### 3. **Algoritmos Fundamentales de Recorrido**
- **BFS (Breadth-First Search - Búsqueda en Amplitud)**
  - Concepto y características
  - Pseudocódigo
  - Implementación en Python
  - Visualización del proceso
  - Aplicaciones prácticas
  
- **DFS (Depth-First Search - Búsqueda en Profundidad)**
  - Concepto y características
  - Versión recursiva e iterativa
  - Implementación en Python
  - Visualización del proceso
  - Aplicaciones prácticas

- **Comparación BFS vs DFS**: Tabla comparativa completa

## 🚀 Características Técnicas

### Tecnologías Utilizadas
- **HTML5**: Estructura semántica y moderna
- **CSS3**: Diseño responsive y animaciones
- **JavaScript (Vanilla)**: Interactividad sin dependencias externas
- **Git/GitHub**: Control de versiones

### Características del Blog
✅ Diseño responsivo (mobile-first)
✅ Navegación suave y modal interactivo
✅ Diagramas SVG integrados
✅ Fragmentos de código con sintaxis clara
✅ Cajas de información y notas destacadas
✅ Animaciones fluidas
✅ Interfaz intuitiva y profesional

## 📁 Estructura del Proyecto

```
proyecto-copilot/
├── index.html          # Página principal del blog
├── styles.css          # Estilos CSS completos
├── scripts.js          # JavaScript interactivo
├── cola.py             # (Archivo de datos/código)
├── README.md           # Este archivo
└── .git/               # Repositorio Git
```

## 🎨 Diseño Visual

### Paleta de Colores
- **Primario**: Azul (#2563eb) - Encabezados y botones principales
- **Secundario**: Azul oscuro (#1e40af) - Gradientes
- **Acento**: Naranja (#f59e0b) - Call-to-action y enfasis
- **Texto**: Gris oscuro (#1f2937) - Legibilidad

### Componentes
- Barra de navegación adhesiva
- Sección hero con call-to-action
- Grid de tarjetas de posts
- Modal para visualizar artículos completos
- Pie de página con información

## 💻 Cómo Usar

### Abrir el Blog
1. Descarga o clona el repositorio
2. Abre el archivo `index.html` en tu navegador web
3. O utiliza un servidor local:
   ```bash
   # Con Python 3
   python -m http.server 8000
   
   # Con Node.js
   npx http-server
   ```
4. Accede a `http://localhost:8000`

### Interactividad
- **Haz clic en cualquier tarjeta** de artículo para ver el contenido completo
- **Usa la barra de navegación** para desplazarse suavemente
- **El botón CTA** lleva directamente a los artículos
- **Presiona ESC** para cerrar un artículo abierto

## 📚 Contenido Técnico

### Ejemplos de Código Incluidos

#### Lista de Adyacencia (Python)
```python
grafo = {
    'A': ['B', 'D'],
    'B': ['A', 'C', 'E'],
    'C': ['B', 'E'],
    'D': ['A', 'E'],
    'E': ['B', 'C', 'D']
}
```

#### Matriz de Adyacencia (Python)
```python
grafo = [
    [0, 1, 0, 1, 0],
    [1, 0, 1, 0, 1],
    [0, 1, 0, 0, 1],
    [1, 0, 0, 0, 1],
    [0, 1, 1, 1, 0]
]
```

#### BFS (Python)
```python
from collections import deque

def bfs(grafo, inicio):
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
```

#### DFS Recursivo (Python)
```python
def dfs_recursivo(grafo, vertice, visitado=None):
    if visitado is None:
        visitado = set()
    
    visitado.add(vertice)
    resultado = [vertice]
    
    for vecino in grafo[vertice]:
        if vecino not in visitado:
            resultado.extend(dfs_recursivo(grafo, vecino, visitado))
    
    return resultado
```

## 🌐 Diagramas y Visualizaciones

El blog incluye:
- Diagrama de grafo no dirigido (5 nodos)
- Comparación visual de lista vs matriz de adyacencia
- Visualización paso a paso de BFS
- Visualización paso a paso de DFS

## ✨ Características Avanzadas

### CSS Moderno
- Gradientes lineales
- Box shadows con depth
- Transiciones suaves
- Grid responsive
- Media queries para mobile

### JavaScript Vanilla
- Gestión de modal sin jQuery
- Navegación smooth scroll
- Event listeners optimizados
- Cierre de modal con ESC
- Interactividad sin dependencies

## 📊 Complejidad Algorítmica

| Algoritmo | Complejidad Temporal | Complejidad Espacial | Caso de Uso |
|-----------|--------------------|--------------------|------------|
| BFS | O(V + E) | O(V) | Camino más corto |
| DFS | O(V + E) | O(h) | Ciclos, topología |

## 🔧 Optimizaciones

- Carga rápida sin dependencias externas
- CSS minificado conceptualmente
- JavaScript eficiente
- Imágenes SVG escalables
- Diseño mobile-first

## 📱 Responsividad

El diseño se adapta perfectamente a:
- 📱 Móviles (480px y menores)
- 📱 Tablets (481px - 768px)
- 💻 Desktops (769px y mayores)

## 🎓 Objetivos Educativos

✅ Aprender la estructura de datos Grafos
✅ Entender dos formas de representar grafos
✅ Dominar algoritmos de recorrido (BFS y DFS)
✅ Aplicar HTML5, CSS3 y JavaScript moderno
✅ Practicar control de versiones con Git/GitHub
✅ Crear contenido técnico de calidad

## 👨‍💻 Autor

Proyecto desarrollado como actividad académica de **Estructuras de Datos 2**.

## 📄 Licencia

Este proyecto es de código abierto y está disponible bajo los términos que establezca tu institución educativa.

## 🚀 Próximas Mejoras

- [ ] Implementar tema oscuro/claro
- [ ] Agregar más algoritmos (Dijkstra, Floyd-Warshall)
- [ ] Visualizador interactivo de grafos
- [ ] Quiz y ejercicios interactivos
- [ ] Versión en inglés
- [ ] Exportar contenido a PDF

---

**Última actualización**: 25 de Noviembre, 2025

¡Disfruta aprendiendo sobre Grafos! 🎉

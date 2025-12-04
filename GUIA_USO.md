# 📘 Guía de Uso del Blog Técnico de Grafos

## 1. Estructura del Proyecto

```
proyecto-copilot/
├── index.html              # Página web del blog
├── styles.css              # Estilos CSS
├── scripts.js              # JavaScript interactivo
├── grafos.py               # Implementación de grafos en Python
├── test_grafos.py          # Tests unitarios
├── cola.py                 # Archivo de datos
├── README.md               # Documentación principal
├── GUIA_USO.md            # Este archivo
└── .git/                   # Control de versiones
```

## 2. Cómo Abrir el Blog Web

### Opción 1: Abrir directamente en el navegador
1. Abre la carpeta del proyecto
2. Haz doble clic en `index.html`
3. Se abrirá automáticamente en tu navegador predeterminado

### Opción 2: Usar un servidor local (Recomendado)

#### Con Python 3:
```bash
cd "ruta/a/proyecto-copilot"
python -m http.server 8000
```
Luego abre: `http://localhost:8000`

#### Con Node.js:
```bash
cd "ruta/a/proyecto-copilot"
npx http-server
```

#### Con PHP (si está instalado):
```bash
cd "ruta/a/proyecto-copilot"
php -S localhost:8000
```

## 3. Navegar por el Blog

### Elementos Principales

**Barra de Navegación (arriba)**
- Logo del blog
- Enlaces a secciones
- Adhesiva (se queda arriba al scroll)

**Sección Hero**
- Título principal
- Descripción breve
- Botón para ir a artículos

**Grid de Artículos**
- 3 tarjetas clickeables
- Resumen de cada post
- Información de fecha

**Modal (ventana emergente)**
- Se abre al hacer clic en un artículo
- Contiene el artículo completo
- Cerrar con X, click fuera o ESC

**Pie de Página**
- Información del proyecto
- Créditos

### Interacciones

| Acción | Resultado |
|--------|-----------|
| Click en tarjeta de artículo | Abre el artículo completo |
| Click en botón "Leer Artículos" | Scroll suave a los artículos |
| Click en logo | Va a inicio |
| Press ESC | Cierra artículo abierto |
| Click fuera del modal | Cierra artículo abierto |

## 4. Artículos Disponibles

### Post 1: Introducción a los Grafos
- **Duración de lectura:** ~8 minutos
- **Temas cubiertos:**
  - Definición de grafos
  - Vértices y aristas
  - Tipos de grafos (dirigidos, no dirigidos, ponderados)
  - Concepto de grado
  - Caminos y ciclos
- **Visual:** Diagrama de grafo con 5 nodos

### Post 2: Representación de Grafos
- **Duración de lectura:** ~10 minutos
- **Temas cubiertos:**
  - Lista de adyacencia (con código)
  - Matriz de adyacencia (con código)
  - Ventajas y desventajas de cada una
  - Cuándo usar cada representación
- **Visuals:** Comparación lado a lado de ambas representaciones

### Post 3: Algoritmos Fundamentales
- **Duración de lectura:** ~12 minutos
- **Temas cubiertos:**
  - BFS (Breadth-First Search) con código
  - DFS (Depth-First Search) - recursivo e iterativo
  - Comparación de ambos algoritmos
  - Aplicaciones prácticas
- **Visuals:** Diagramas de proceso para cada algoritmo

## 5. Usar los Archivos Python

### Ejecutar Ejemplos
```bash
cd "ruta/a/proyecto-copilot"
python grafos.py
```

Esto mostrará:
- Ejemplo 1: Lista de Adyacencia
- Ejemplo 2: Matriz de Adyacencia
- Ejemplo 3: Detección de Ciclos

### Ejecutar Tests
```bash
cd "ruta/a/proyecto-copilot"
python test_grafos.py
```

Resultado esperado: 20 tests ejecutados con éxito

### Importar las Clases en tu Código
```python
from grafos import (
    GrafoListaAdyacencia,
    GrafoMatrizAdyacencia,
    AlgoritmosGrafos
)

# Crear un grafo
g = GrafoListaAdyacencia()
g.agregar_vertice('A')
g.agregar_vertice('B')
g.agregar_arista('A', 'B')

# Usar algoritmos
resultado_bfs = AlgoritmosGrafos.bfs(g, 'A')
print(resultado_bfs)  # ['A', 'B']
```

## 6. Personalizar el Blog

### Cambiar Colores
Edita `styles.css` y modifica las variables en `:root`:
```css
:root {
    --primary-color: #2563eb;      /* Azul */
    --secondary-color: #1e40af;    /* Azul oscuro */
    --accent-color: #f59e0b;       /* Naranja */
    --text-color: #1f2937;         /* Texto gris oscuro */
}
```

### Agregar Nuevo Artículo
1. Abre `scripts.js`
2. Agrega un nuevo objeto a la variable `posts`:
```javascript
post4: {
    title: "Título del nuevo artículo",
    content: `<div class="post-full">
        <h2>Mi Nuevo Artículo</h2>
        <!-- Contenido aquí -->
    </div>`
}
```
3. Agrega la tarjeta en `index.html`:
```html
<article class="post-card" onclick="showPost('post4')">
    <h3>Título del nuevo artículo</h3>
    <p>Descripción breve...</p>
</article>
```

### Cambiar Fuentes
En `styles.css`, busca `font-family` y reemplaza:
```css
font-family: 'Tu Fuente', fallback;
```

## 7. Requisitos del Sistema

### Para el Blog Web
- Navegador moderno (Chrome, Firefox, Edge, Safari)
- Conexión a internet (opcional si usas servidor local)

### Para Python
- Python 3.7 o superior
- Módulos estándar (unittest, collections, deque)

## 8. Solución de Problemas

### El blog no se ve correctamente
**Solución:** Asegúrate de abrir con `http://localhost:...` en lugar de `file://`

### Los ejemplos Python no ejecutan
**Solución:** 
- Verifica que Python esté instalado: `python --version`
- Asegúrate de estar en la carpeta correcta
- En Windows, usa `python grafos.py`

### Los tests fallan
**Solución:** Verifica que `grafos.py` está en la misma carpeta que `test_grafos.py`

## 9. Características de Responsive Design

El blog se adapta automáticamente a:
- **Móviles (< 480px):** Layout de una columna
- **Tablets (480-768px):** Grid de 2 columnas
- **Desktops (> 768px):** Grid de 3 columnas

Prueba redimensionando tu navegador o abriendo con un dispositivo móvil.

## 10. Recursos Educativos Incluidos

### En el Blog
- ✅ 3 artículos técnicos completos
- ✅ 4 diagramas SVG interactivos
- ✅ 15+ fragmentos de código
- ✅ 3 cajas de información/éxito

### En Python
- ✅ 2 clases principales (Lista y Matriz)
- ✅ 5 algoritmos implementados
- ✅ 20 tests unitarios
- ✅ 3 ejemplos de uso

## 11. Control de Versiones con Git

### Ver historial
```bash
cd "ruta/a/proyecto-copilot"
git log --oneline
```

### Ver cambios
```bash
git status
git diff
```

### Hacer commit
```bash
git add .
git commit -m "Descripción de cambios"
```

### Push a GitHub
```bash
git push origin main
```

## 12. Consejos para Aprender

1. **Comienza con el Post 1** para entender conceptos básicos
2. **Visualiza los diagramas** mientras lees para mejor comprensión
3. **Ejecuta los ejemplos Python** para ver cómo funcionan realmente
4. **Modifica el código** y experimenta con cambios
5. **Lee los tests** para entender casos edge
6. **Intenta crear tus propios grafos** con el código

## 13. FAQ (Preguntas Frecuentes)

**P: ¿Puedo usar este blog para otra clase?**
R: Sí, el contenido es reutilizable bajo los términos de tu institución.

**P: ¿Cómo agrego más algoritmos?**
R: Agrega métodos a la clase `AlgoritmosGrafos` en `grafos.py` y crea tests correspondientes.

**P: ¿El blog funciona sin internet?**
R: Sí, es completamente local. Solo necesitas Python para los ejemplos.

**P: ¿Puedo desplegarlo en un servidor web?**
R: Sí, copia todos los archivos `.html`, `.css`, `.js` a tu servidor.

---

**Última actualización:** 25 de Noviembre, 2025

¡Disfruta aprendiendo Grafos! Si tienes preguntas, revisa el README.md para más detalles.

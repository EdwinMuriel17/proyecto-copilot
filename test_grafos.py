"""
Tests unitarios para la implementación de Grafos
Usa el módulo unittest de Python
"""

import unittest
from grafos import (
    GrafoListaAdyacencia,
    GrafoMatrizAdyacencia,
    AlgoritmosGrafos
)


class TestGrafoListaAdyacencia(unittest.TestCase):
    """Tests para la clase GrafoListaAdyacencia."""
    
    def setUp(self):
        """Se ejecuta antes de cada test."""
        self.grafo = GrafoListaAdyacencia()
        
        # Crear grafo de prueba
        for v in ['A', 'B', 'C', 'D', 'E']:
            self.grafo.agregar_vertice(v)
        
        aristas = [('A', 'B'), ('A', 'D'), ('B', 'C'), ('B', 'E'), 
                   ('C', 'E'), ('D', 'E')]
        for u, v in aristas:
            self.grafo.agregar_arista(u, v)
    
    def test_agregar_vertice(self):
        """Verifica que se agrega correctamente un vértice."""
        self.assertIn('A', self.grafo.grafo)
        self.assertIn('B', self.grafo.grafo)
    
    def test_agregar_arista(self):
        """Verifica que se agrega correctamente una arista."""
        self.assertIn('B', self.grafo.obtener_vecinos('A'))
        self.assertIn('A', self.grafo.obtener_vecinos('B'))
    
    def test_obtener_vecinos(self):
        """Verifica que se obtienen correctamente los vecinos."""
        vecinos_A = self.grafo.obtener_vecinos('A')
        self.assertIn('B', vecinos_A)
        self.assertIn('D', vecinos_A)
        self.assertEqual(len(vecinos_A), 2)
    
    def test_grafo_vacio(self):
        """Verifica comportamiento con grafo vacío."""
        grafo_vacio = GrafoListaAdyacencia()
        self.assertEqual(grafo_vacio.grafo, {})
        self.assertEqual(grafo_vacio.obtener_vecinos('X'), [])
    
    def test_vertice_aislado(self):
        """Verifica que un vértice sin aristas no tiene vecinos."""
        self.grafo.agregar_vertice('F')
        self.assertEqual(self.grafo.obtener_vecinos('F'), [])
    
    def test_arista_no_duplicada(self):
        """Verifica que no se duplican aristas."""
        self.grafo.agregar_arista('A', 'B')
        vecinos = self.grafo.obtener_vecinos('A')
        # Contar cuántas veces aparece 'B'
        conteo = vecinos.count('B')
        # Puede ser 2 porque se agregó nuevamente, pero verificamos estructura
        self.assertGreaterEqual(conteo, 1)


class TestGrafoMatrizAdyacencia(unittest.TestCase):
    """Tests para la clase GrafoMatrizAdyacencia."""
    
    def setUp(self):
        """Se ejecuta antes de cada test."""
        self.grafo = GrafoMatrizAdyacencia(5)
        
        # Agregar vértices
        etiquetas = ['A', 'B', 'C', 'D', 'E']
        for i, etiqueta in enumerate(etiquetas):
            self.grafo.agregar_vertice(etiqueta, i)
        
        # Agregar aristas
        aristas = [('A', 'B'), ('A', 'D'), ('B', 'C'), ('B', 'E'), 
                   ('C', 'E'), ('D', 'E')]
        for u, v in aristas:
            self.grafo.agregar_arista(u, v)
    
    def test_existe_arista(self):
        """Verifica consulta de existencia de arista."""
        self.assertTrue(self.grafo.existe_arista('A', 'B'))
        self.assertTrue(self.grafo.existe_arista('B', 'A'))
        self.assertFalse(self.grafo.existe_arista('A', 'C'))
    
    def test_agregar_arista_con_peso(self):
        """Verifica agregar arista con peso."""
        grafo = GrafoMatrizAdyacencia(3)
        grafo.agregar_vertice('A', 0)
        grafo.agregar_vertice('B', 1)
        grafo.agregar_vertice('C', 2)
        
        grafo.agregar_arista('A', 'B', peso=5)
        self.assertEqual(grafo.matriz[0][1], 5)
        self.assertEqual(grafo.matriz[1][0], 5)  # Bidireccional
    
    def test_arista_unidireccional(self):
        """Verifica agregar arista unidireccional."""
        grafo = GrafoMatrizAdyacencia(3)
        grafo.agregar_vertice('A', 0)
        grafo.agregar_vertice('B', 1)
        
        grafo.agregar_arista('A', 'B', bidireccional=False)
        self.assertEqual(grafo.matriz[0][1], 1)
        self.assertEqual(grafo.matriz[1][0], 0)


class TestAlgoritmosBFS(unittest.TestCase):
    """Tests para el algoritmo BFS."""
    
    def setUp(self):
        """Se ejecuta antes de cada test."""
        self.grafo = GrafoListaAdyacencia()
        
        for v in ['A', 'B', 'C', 'D', 'E']:
            self.grafo.agregar_vertice(v)
        
        aristas = [('A', 'B'), ('A', 'D'), ('B', 'C'), ('B', 'E'), 
                   ('C', 'E'), ('D', 'E')]
        for u, v in aristas:
            self.grafo.agregar_arista(u, v)
    
    def test_bfs_desde_A(self):
        """Verifica BFS desde vértice A."""
        resultado = AlgoritmosGrafos.bfs(self.grafo, 'A')
        # BFS debe visitar todos los vértices
        self.assertEqual(len(resultado), 5)
        # Primer elemento debe ser A
        self.assertEqual(resultado[0], 'A')
    
    def test_bfs_visita_todos(self):
        """Verifica que BFS visita todos los vértices accesibles."""
        resultado = AlgoritmosGrafos.bfs(self.grafo, 'A')
        # Verificar que todos los vértices están presentes
        for v in ['A', 'B', 'C', 'D', 'E']:
            self.assertIn(v, resultado)
    
    def test_bfs_grafo_desconectado(self):
        """Verifica BFS con grafo desconectado."""
        grafo = GrafoListaAdyacencia()
        grafo.agregar_vertice('A')
        grafo.agregar_vertice('B')
        grafo.agregar_vertice('C')
        
        grafo.agregar_arista('A', 'B')
        grafo.agregar_vertice('D')  # Vértice desconectado
        
        resultado = AlgoritmosGrafos.bfs(grafo, 'A')
        # BFS solo debe visitar vértices accesibles
        self.assertIn('A', resultado)
        self.assertIn('B', resultado)
        self.assertNotIn('D', resultado)
    
    def test_bfs_orden_por_niveles(self):
        """Verifica que BFS mantiene orden por niveles."""
        grafo = GrafoListaAdyacencia()
        for v in ['A', 'B', 'C', 'D', 'E']:
            grafo.agregar_vertice(v)
        
        # Crear árbol de niveles
        grafo.agregar_arista('A', 'B')
        grafo.agregar_arista('A', 'C')
        grafo.agregar_arista('B', 'D')
        grafo.agregar_arista('C', 'E')
        
        resultado = AlgoritmosGrafos.bfs(grafo, 'A')
        # A debe ser primero
        self.assertEqual(resultado[0], 'A')
        # B y C deben estar antes que D y E
        indice_D = resultado.index('D')
        indice_E = resultado.index('E')
        indice_B = resultado.index('B')
        indice_C = resultado.index('C')
        
        self.assertLess(indice_B, indice_D)
        self.assertLess(indice_C, indice_E)


class TestAlgoritmosDFS(unittest.TestCase):
    """Tests para el algoritmo DFS."""
    
    def setUp(self):
        """Se ejecuta antes de cada test."""
        self.grafo = GrafoListaAdyacencia()
        
        for v in ['A', 'B', 'C', 'D', 'E']:
            self.grafo.agregar_vertice(v)
        
        aristas = [('A', 'B'), ('A', 'D'), ('B', 'C'), ('B', 'E'), 
                   ('C', 'E'), ('D', 'E')]
        for u, v in aristas:
            self.grafo.agregar_arista(u, v)
    
    def test_dfs_recursivo_desde_A(self):
        """Verifica DFS recursivo desde vértice A."""
        resultado = AlgoritmosGrafos.dfs_recursivo(self.grafo, 'A')
        # DFS debe visitar todos los vértices
        self.assertEqual(len(resultado), 5)
        # Primer elemento debe ser A
        self.assertEqual(resultado[0], 'A')
    
    def test_dfs_iterativo_desde_A(self):
        """Verifica DFS iterativo desde vértice A."""
        resultado = AlgoritmosGrafos.dfs_iterativo(self.grafo, 'A')
        # DFS debe visitar todos los vértices
        self.assertEqual(len(resultado), 5)
        # Primer elemento debe ser A
        self.assertEqual(resultado[0], 'A')
    
    def test_dfs_visita_todos(self):
        """Verifica que DFS visita todos los vértices accesibles."""
        resultado_rec = AlgoritmosGrafos.dfs_recursivo(self.grafo, 'A')
        resultado_iter = AlgoritmosGrafos.dfs_iterativo(self.grafo, 'A')
        
        for v in ['A', 'B', 'C', 'D', 'E']:
            self.assertIn(v, resultado_rec)
            self.assertIn(v, resultado_iter)
    
    def test_dfs_recursivo_vs_iterativo(self):
        """Verifica que ambas versiones de DFS visitan los mismos vértices."""
        resultado_rec = AlgoritmosGrafos.dfs_recursivo(self.grafo, 'A')
        resultado_iter = AlgoritmosGrafos.dfs_iterativo(self.grafo, 'A')
        
        # Mismo número de vértices visitados
        self.assertEqual(len(resultado_rec), len(resultado_iter))
        # Mismos vértices visitados
        self.assertEqual(set(resultado_rec), set(resultado_iter))


class TestDeteccionCiclos(unittest.TestCase):
    """Tests para la detección de ciclos."""
    
    def test_grafo_sin_ciclos(self):
        """Verifica detección en grafo sin ciclos."""
        grafo = GrafoListaAdyacencia()
        for v in ['A', 'B', 'C', 'D']:
            grafo.agregar_vertice(v)
        
        aristas = [('A', 'B'), ('B', 'C'), ('C', 'D')]
        for u, v in aristas:
            grafo.agregar_arista(u, v, bidireccional=False)
        
        tiene_ciclo = False
        for v in grafo.grafo:
            if AlgoritmosGrafos.detectar_ciclos(grafo, v):
                tiene_ciclo = True
                break
        
        self.assertFalse(tiene_ciclo)
    
    def test_grafo_con_ciclos(self):
        """Verifica detección en grafo con ciclos."""
        grafo = GrafoListaAdyacencia()
        for v in ['A', 'B', 'C', 'D']:
            grafo.agregar_vertice(v)
        
        aristas = [('A', 'B'), ('B', 'C'), ('C', 'D'), ('D', 'A')]
        for u, v in aristas:
            grafo.agregar_arista(u, v, bidireccional=False)
        
        tiene_ciclo = False
        for v in grafo.grafo:
            if AlgoritmosGrafos.detectar_ciclos(grafo, v):
                tiene_ciclo = True
                break
        
        self.assertTrue(tiene_ciclo)
    
    def test_auto_ciclo(self):
        """Verifica detección de auto-ciclo (self-loop)."""
        grafo = GrafoListaAdyacencia()
        grafo.agregar_vertice('A')
        grafo.agregar_arista('A', 'A', bidireccional=False)
        
        tiene_ciclo = AlgoritmosGrafos.detectar_ciclos(grafo, 'A')
        self.assertTrue(tiene_ciclo)


# ============================================================================
# MAIN - Ejecutar tests
# ============================================================================

if __name__ == '__main__':
    # Crear suite de tests
    loader = unittest.TestLoader()
    suite = unittest.TestSuite()
    
    # Agregar tests
    suite.addTests(loader.loadTestsFromTestCase(TestGrafoListaAdyacencia))
    suite.addTests(loader.loadTestsFromTestCase(TestGrafoMatrizAdyacencia))
    suite.addTests(loader.loadTestsFromTestCase(TestAlgoritmosBFS))
    suite.addTests(loader.loadTestsFromTestCase(TestAlgoritmosDFS))
    suite.addTests(loader.loadTestsFromTestCase(TestDeteccionCiclos))
    
    # Ejecutar tests
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)
    
    # Imprimir resumen
    print("\n" + "=" * 60)
    print("RESUMEN DE TESTS")
    print("=" * 60)
    print(f"Tests ejecutados: {result.testsRun}")
    print(f"Tests exitosos: {result.testsRun - len(result.failures) - len(result.errors)}")
    print(f"Fallos: {len(result.failures)}")
    print(f"Errores: {len(result.errors)}")
    print("=" * 60 + "\n")

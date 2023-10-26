#Este código utiliza una matriz de adyacencia para representar el grafo y genera el Árbol Parcial Mínimo paso a paso:

import sys

class PrimMST:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[0 for _ in range(vertices)] for _ in range(vertices)]

    def min_key(self, key, mst_set):
        min_value = sys.maxsize
        min_index = -1
        for v in range(self.V):
            if key[v] < min_value and not mst_set[v]:
                min_value = key[v]
                min_index = v
        return min_index

    def print_mst(self, parent):
        print("Aristas del Árbol Parcial Mínimo (MST):")
        for i in range(1, self.V):
            print(f"Arista: {parent[i]} - {i}, Peso: {self.graph[i][parent[i]]}")

    def prim_mst(self):
        key = [sys.maxsize] * self.V
        parent = [-1] * self.V
        key[0] = 0
        mst_set = [False] * self.V

        for _ in range(self.V):
            u = self.min_key(key, mst_set)
            mst_set[u] = True

            for v in range(self.V):
                if self.graph[u][v] and not mst_set[v] and key[v] > self.graph[u][v]:
                    key[v] = self.graph[u][v]
                    parent[v] = u

        self.print_mst(parent)

# Ejemplo de uso
g = PrimMST(5)
g.graph = [[0, 2, 0, 6, 0],
           [2, 0, 3, 8, 5],
           [0, 3, 0, 0, 7],
           [6, 8, 0, 0, 9],
           [0, 5, 7, 9, 0]]

g.prim_mst()

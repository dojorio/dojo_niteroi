def minimo_cores(grafo):
    if all(bool(not vertice) for vertice in grafo.values()):
        return 1
    if grafo[0] or grafo[1] or grafo[2]:
        return 2



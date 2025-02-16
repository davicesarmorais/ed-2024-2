from collections import deque


def dfs(inicio, grafo):
    def _dfs(no, grafo, visitados):
        visitados.add(no)
        
        print(no, end=" ")
        for i in grafo[no]:
            if i not in visitados:
                _dfs(i, grafo, visitados)
    _dfs(inicio, grafo, set())


def bfs(inicio, grafo):
    visitados = set()
    fila = deque([inicio])

    while fila:
        no = fila.popleft()
        if no not in visitados:
            print(no, end=" ")
            visitados.add(no)
            for vizinho in grafo[no]:
                if vizinho not in visitados:
                    fila.append(vizinho)

def main():
    grafo = {
        'A': ['B', 'C'],
        'B': ['D', 'E'],
        'C': ['F'],
        'D': [],
        'E': [],
        'F': []
    }
    dfs("A", grafo)
    print()
    bfs("A", grafo)


if __name__ == "__main__":
    main()

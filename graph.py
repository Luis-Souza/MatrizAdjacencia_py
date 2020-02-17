#Author: Marcos Filho, Francisco Jose, Jorge Luis
import networkx as nx
import scipy

graph = nx.Graph()
arestas = [(1,5),(1,2),(2,3),(3,4),(4,5)]
node = 5
#return matriz adjacenci
def matrizAdj(qtdVertices, listArestas): 
    for i in range(qtdVertices):
        vertice = int(input('Informe o nome de cada Vertice do Grafo: '))       
        graph.add_node(vertice)                 #add vertices ao grafo

    for i in range(qtdVertices):
        graph.add_edges_from([listArestas[i]])  #add lista de aresta
    
    # aux = nx.adjacency_matrix(graph)    #gera a matriz de adjacencia

    return graph

def listAdj(graph):
    g = nx.to_dict_of_lists(graph)
    return g

visitados = []
def dfs(grafo, vertice):
    visitados = set()

    def dfs_recursiva(grafo, vertice):
        visitados.add(vertice)
        for vizinho in grafo[vertice]:
            if vizinho not in visitados:
                dfs_recursiva(grafo, vizinho)

    dfs_recursiva(grafo, vertice)

print(dfs(matrizAdj(node,arestas), 1))

print('Matriz de Adjacencia\n', matrizAdj(node,arestas).toarray())
print('Lista de Adjacencia\n', listAdj(graph))
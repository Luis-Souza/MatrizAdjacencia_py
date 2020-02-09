#Author: Marcos Filho, Francisco Jose, Jorge Luis
import networkx as nx
import scipy

arestas = [(1,5),(1,2),(2,3),(3,4),(4,5)]
node = 5
#return matriz adjacenci
def matrizAdj(qtdVertices, listArestas): 
    graph = nx.Graph()
    for i in range(qtdVertices):
        vertice = int(input('Informe o nome de cada Vertice do Grafo: '))       
        graph.add_node(vertice)                 #add vertices ao grafo

    for i in range(qtdVertices):
        graph.add_edges_from([listArestas[i]])  #add lista de aresta
    
    aux = nx.adjacency_matrix(graph)    #gera a matriz de adjacencia

    return aux

print('Matriz de Adjacencia\n', matrizAdj(node,arestas).toarray())

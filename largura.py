# #encoding: utf8

QtdVertices = int(input("Total de vertices: "))
maiorGrau = int(input("Qual valor do maior grau de um vertice no grafo que voce informa: "))

vertices           = []
verticesAssociados = []
qtdDeAssociadoporV = []

for i in range(0, QtdVertices):
    print(i+1, "° Vertice: ")
    vertice = input()
    vertices.append(vertice)

for j in range(0, QtdVertices):
    print("Qual(is) vertices(s) associados ao ", vertices[j], "?")
    qtdAssociado = int(input("Qtd Associada: "))
    qtdDeAssociadoporV.append(qtdAssociado)
    for k in range(0,qtdAssociado):
        verticeAss = input("VerticeAssociado: ")
        verticesAssociados.append(verticeAss)
        

def amplitude():
    pontoAtual = 0
    aux = 0

    for v in range(QtdVertices):
        print(" O Vertice ",vertices[v])
        ValorPraPercorrer = qtdDeAssociadoporV[pontoAtual]
        pontoAtual = pontoAtual + 1
               
        for i in range(0, ValorPraPercorrer):
            VerticeAss = verticesAssociados[aux]
            aux+=1
            print("tem os associados: ", VerticeAss)
        


#Leitura de arquivo dfs
arquivo = open('bsf.txt', 'r')
caracteres = []
for linha in arquivo:
    linha = linha.split()
    caracteres.append(linha)
for caract in range(len(caracteres)):
    print(caracteres[caract])
arquivo.close()
print(caracteres)



print("\nVertices: ", vertices)
print("Vertices Ass: ", verticesAssociados)        
print("Qtd Associado: ", qtdDeAssociadoporV)
amplitude()
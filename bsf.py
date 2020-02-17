#encoding: utf8
#Leitura de arquivo

arquivo = open('bsf.txt', 'r')
LeituraDoArquivo = []
Vertices = []
Arestas  = []
QtdAssoc = []


for linha in arquivo:
    linha = linha.split()
    LeituraDoArquivo.append(linha)
    
for i in LeituraDoArquivo[1]:
    Vertices.append(i)
for j in LeituraDoArquivo[2]:
    Arestas.append(j)
for k in LeituraDoArquivo[0]:
    QtdAssoc.append(k)
    
    
def associacoes():
    pontoAtual = 0
    aux = 0

    for v in range(len(Vertices)):
        print(" O Vertice ",Vertices[v])
        ValorPraPercorrer = QtdAssoc[pontoAtual]
        pontoAtual = pontoAtual + 1
               
        for i in range(int(ValorPraPercorrer)):
            VerticeAss = Arestas[aux]
            aux+=1
            print("tem os associados: ", VerticeAss)
        print("aux: ", aux)    

for caract in range(len(Vertices)):
    #print(caracteres[caract])
    print(Vertices[caract])
arquivo.close()


print("Leitura do Arquivo: ", LeituraDoArquivo)
print("vertices: ", Vertices)
print("Arestas: ", Arestas)
print("Qtd Assoc: ", QtdAssoc)
associacoes()
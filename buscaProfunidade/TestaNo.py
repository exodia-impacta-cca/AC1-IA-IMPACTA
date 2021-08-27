from Estado import Estado
from No import No

estadoInicial = Estado('/home/ec2-user/environment/DiretorioInicial')
raiz = No(estadoInicial)

print ("<< Atributos do Nó Raiz >>")
print("Path do Estado: ",raiz.estado.caminho)
print("Profundidade: ",raiz.profundidade)
print("Nós Filhos: ",raiz.filhos)
print("Nó Pai: ",raiz.pai)


estadosFilhos = raiz.estado.funcaoSucessora()
print("Estados filhos: ",estadosFilhos)


for umEstadoFilho in estadosFilhos:
    noFilho = No(Estado(umEstadoFilho))
    raiz.addFilho(noFilho)

print ("<< Atributos do Nó Raiz >>")    
print("Caminho do Estado: ",raiz.estado.caminho)
print("Profundidade: ",raiz.profundidade)
print("Nós Filhos: ",raiz.filhos)
print("Nó Pai: ",raiz.pai)  

for noFilho in raiz.filhos:
    print(noFilho.estado.caminho)
    
raiz.printArvore()

from No import No
from Estado import Estado
from DesenhaArvore import DesenhaArvore


estadoInicial = Estado()
raiz = No(estadoInicial,None)


estadosFilhos = estadoInicial.funcaoSucessora()
for filho in estadosFilhos:
    filho = No(Estado(filho),raiz) 


plotaArvore = DesenhaArvore()

plotaArvore.criaDiagrama(raiz,raiz)
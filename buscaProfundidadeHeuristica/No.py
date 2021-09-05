# nó da busca em Profundidade

from math import sqrt
from GrafoDados import *
'''
Esta classe representa um nó na árvore de busca
'''
class No():
    def __init__(self, estado, noPai):
        """
        Construtor
        """
        self.estado = estado
        self.profundidade = 0
        self.filhos = []
        self.pai= self.colocaPai(noPai)
        self.heuristica = None
        self.fringe = True
    
    def colocaPai(self,noPai):
        """
        Esse metodo adiciona um nó a outro nó
        """
        if noPai != None:
            noPai.filhos.append(self)
            self.pai = noPai
            self.profundidade = noPai.profundidade + 1
        else:
            self.pai = None
        
        
    def addFilho(self, noFilho):
        """
        Este método adiciona um nó em outro nó
        """
        self.filhos.append(noFilho)
        noFilho.pai = self   # o noFilho aponta para o nó atual
        noFilho.profundidade = self.profundidade + 1
        

    def printArvore(self):
        """
        Este método imprime a sub-árvore a partir desse nó
        """
        print (self.profundidade , " - " , self.estado.nome)
        for umFilho in self.filhos:
            umFilho.printArvore()
            
    def printCaminho(self):
                """
                Este método imprime o caminho do estado inicial ao estado objetivo
                """
                if self.pai != None:
                    self.pai.printCaminho()  
                print ("-> ", self.estado.nome)
    
    def calculaheuristica(self):
        '''
        Essa função calcula o valor da heuristica para esse nó
        '''
        #Calcula a distancia do estado atual para o estado meta

        #localização destino
        localizacaoMeta = conexoes["Faculdade Impacta"]
        #localização atual
        localizacaoAtual = conexoes[self.estado.nome]
        #delta na coordenada x
        dx = localizacaoMeta[0] - localizacaoAtual[0]
        #delta na coordenada y
        dy = localizacaoMeta[1] - localizacaoAtual[1]
        #distancia
        distancia = sqrt(dx ** 2 + dy ** 2)
        self.heuristica = distancia

        
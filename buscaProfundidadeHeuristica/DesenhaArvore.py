import pydot
import matplotlib.image as mpimg
import matplotlib.pyplot as plt

class DesenhaArvore:
    '''
    Essa classe desenha a arvore de busca
    '''
    def __init__(self):
        """
        Construtor
        """
        #Cria o objeto grafo

        self.grafo = pydot.Dot(graph_type = 'graph', dpi = 500)
        #indice do no
        self.indice = 0
    
    def criaDiagrama(self, noRaiz,noAtual):
        """
        Esse metodo desenha o diagrama
        """

        #adiciona nós e arcos ao diagrama
        self.criaGrafo(noRaiz, noAtual)

        #mostra o dagrama
        self.grafo.write_png('grafo.png')
        img=mpimg.imread('grafo.png')
        plt.imshow(img)
        plt.axis('off')
        mng = plt.get_current_fig_manager()
        #mng.window.state('normal')
        plt.show()

    
    def criaGrafo(self, no, noatual):
        """
        Este metodo adiciona nos e arcos ao objeto grafo
        semelhante ao printArvore() da classe No
        """

        #associa cor
        if (no.estado.posicao  == noatual.estado.posicao):
            cor = "#ee0011"
        elif no.fringe:
            cor = "#0011ee"
        else:
            cor = "#00ee11"
        
        #cria no
        grafoDoNoPai = pydot.Node(str(self.indice) + " " + no.estado.posicao, style='filled', \
                                      fillcolor = cor, xlabel = no.heuristica)
        self.indice += 1
        
        #add no
        self.grafo.add_node(grafoDoNoPai)
        
        #chama esse metodo para os nos filhos
        for noFilho in no.filhos:
            grafoComNosFilhos = self.criaGrafo(noFilho, noatual)
            
            #cria arco
            arco= pydot.Edge(grafoDoNoPai, grafoComNosFilhos)
            
            #adiciona arco ao objeto grafo
            self.grafo.add_edge(arco)
            
        return grafoDoNoPai
        
    
    
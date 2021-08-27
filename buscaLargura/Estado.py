from GrafoDados import *

class Estado():
    '''
    Esta classe recupera informações de estado de um aplicatico de conexão social
    '''
    
    def __init__(self, nome = None):
        if nome == None:
             #cria o estado inicial
            self.nome = self.getEstadoInicial()
        else:
            self.nome = nome
            
    def getEstadoInicial(self, ):
        """
        Este método retorna o nome  Ana
        """
        estadoInicial= "Casa"
        return estadoInicial

    def funcaoSucessora(self):
        """
        Esta é a função sucessora. Ela encontra todas as pessoas conectads com
        a pessoa atual
        """
        return conexoes[self.nome]
        
        
    def funcaoObjetivo(self):
        """
        Esse método verifica se a pessoa é Gil
        """ 
        #verifique se o nome da pessoa é Gil
        return self.nome == "Faculdade Impacta"
        
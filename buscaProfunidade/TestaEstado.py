from Estado import Estado
import os

estadoInicial = Estado('/home/ec2-user/environment/DiretorioInicial')



novoCaminho= os.path.join(estadoInicial.caminho, "d1", "d11","f111.txt")
print(novoCaminho)
estadoIntermediario = Estado(novoCaminho)

print ("estadoIntermediario", estadoIntermediario.caminho)

if estadoIntermediario.funcaoObjetivo():
    print("achou!!!")
else:
    print("não achou.")



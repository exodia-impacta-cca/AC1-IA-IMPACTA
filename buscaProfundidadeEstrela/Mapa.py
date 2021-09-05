#conexoes entre pontos
conexoes = {}

conexoes["Carregamento"] = {"Estoque Pronto"}
conexoes["Home e Energia"] = {"Estacao 1", "Estacao 4", "Estoque Intermediario"}
conexoes["Estoque Intermediario"] = {"Deposito Insumos 2", "Home e Energia", 
									"Estoque Pronto", "Estacao 3"}

conexoes["Deposito Insumos 1"] = {"Estacao 1"}
conexoes["Deposito Insumos 2"] = {"Estacao 1", "Estoque Intermediario" , "Estacao 2"}

conexoes["Estoque Pronto"] = {"Estacao 4", "Estoque Intermediario", "Carregamento"}

conexoes["Estacao 1"] = {"Deposito Insumos 1", "Deposito Insumos 2","Home e Energia"}
conexoes["Estacao 2"] = {"Deposito Insumos 2", "Estacao 3"}
conexoes["Estacao 3"] = {"Estacao 2", "Estoque Intermediario"}
conexoes["Estacao 4"] = {"Home e Energia", "Estoque Pronto"}

#localização de todos os lugares 

localizacao = {}
localizacao["Carregamento"] = [6, 0]
localizacao["Home e Energia"] = [1, 4]
localizacao["Estoque Intermediario"] = [6, 4]

localizacao["Deposito Insumos 1"] = [2, 8]
localizacao["Deposito Insumos 2"] = [6, 8]

localizacao["Estoque Pronto"] = [6, 1]

localizacao["Estacao 1"] = [4, 8]
localizacao["Estacao 2"] = [7, 7]
localizacao["Estacao 3"] = [7, 5]
localizacao["Estacao 4"] = [4, 1]
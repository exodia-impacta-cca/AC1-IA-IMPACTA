# Criar um dicionário com todos os mapeamentos
conexoes = {}
conexoes ["Casa"] = ["Amador Bueno"]
conexoes ["Amador Bueno"] = ["Osasco"]
conexoes ["Osasco"] = ["Júlio Prestes", "Pinheiros", "Amador Bueno"]
conexoes ["Júlio Prestes"] = ["Barra Funda" ]
conexoes ["Barra Funda"] = ["Faculdade Impacta"]
conexoes ["Pinheiros"] = ["Morumbi", "Consolação", "Santo Amaro"]
conexoes ["Santo Amaro"] = [ "Santa Cruz"]
conexoes ["Consolação"] = ["Anhangabaú"]
conexoes ["Anhangabaú"] = ["Barra Funda"] 
conexoes ["Morumbi"] = ["Santo Amaro"]
conexoes ["Sé"] = ["Barra Funda"]
conexoes ["Faculdade Impacta"] = ["Barra Funda"]
conexoes ["Santa Cruz"] = ["Sé"]


# localização de todos os lugares
localizacao ={}
localizacao ["Casa"] = [3,8]
localizacao ["Amador Bueno"] = [3,7]
localizacao ["Osasco"] = [3,6]
localizacao["Pinheiros"]= [3,5]
localizacao["Morumbi"] = [2,4]
localizacao["Santo Amaro"] = [3,4]
localizacao ["Consolação"] = [4,4]
localizacao ["Santa Cruz"] = [3,3]
localizacao ["Sé"] = [3,2]
localizacao["Anhangabaú"] = [4,3]
localizacao["Júlio Prestes"] = [4,6]
localizacao["Barra Funda"] = [6,6]
localizacao["Faculdade Impacta"] = [8,6]



"""
# localização de todos os lugares
localizacao ={}
localizacao ["Casa"] = [3,8]
localizacao ["Amador Bueno"] = [3,7]
localizacao ["Osasco"] = [3,6]
localizacao["Pinheiros"]= [3,5]
localizacao["Morumbi"] = [2,4]
localizacao["Santo Amaro"] = [3,4]
localizacao ["Consolação"] = [4,4]
localizacao ["Santa Cruz"] = [3,3]
localizacao ["Sé"] = [3,2]
localizacao["Anhangabaú"] = [4,3]
localizacao["Júlio Prestes"] = [4,2]
localizacao["Barra Funda"] = [4,1]
localizacao["Faculdade Impacta"] = [2,0]
"""


# Criar um dicionário com todos os mapeamentos
conexoes = {}
conexoes ["Casa"] = {"Amador Bueno"}
conexoes ["Amador Bueno"] = {"Osasco", "Casa"}
conexoes ["Osasco"] = {"Júlio Prestes", "Pinheiros", "Amador Bueno"}
conexoes ["Júlio Prestes"] = {"Osasco", "Barra Funda"}
conexoes ["Barra Funda"] = {"Anhangabaú", "Sé", "Júlio Prestes", "Faculdade Impacta"}
conexoes ["Pinheiros"] = {"Morumbi", "Consolação", "Osasco", "Santo Amaro"}
conexoes ["Júlio Prestes"] = {"Osasco", "Barra Funda"}
conexoes ["Santo Amaro"] = {"Morumbi", "Santa Cruz", "Pinheiros"}
conexoes ["Consolação"] = {"Anhangabaú", "Pinheiros"}
conexoes ["Anhangabaú"] = {"Consolação", "Barra Funda"} 
conexoes ["Morumbi"] = {"Pinheiros", "Santo Amaro"}
conexoes ["Sé"] = {"Barra Funda", "Santa Cruz"}
conexoes ["Faculdade Impacta"] = {"Barra Funda"}
conexoes ["Santa Cruz"] = {"Sé", "Santo Amaro"}

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
localizacao ["Sé"] = [2,3]
localizacao["Anhangabaú"] = [4,3]
localizacao["Júlio Prestes"] = [5,6]
localizacao["Barra Funda"] = [1,6]
localizacao["Faculdade Impacta"] = [6,0]





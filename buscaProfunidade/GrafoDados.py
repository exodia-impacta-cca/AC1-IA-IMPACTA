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

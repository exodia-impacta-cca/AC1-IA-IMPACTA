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

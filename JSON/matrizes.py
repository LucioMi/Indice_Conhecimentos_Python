#Matrizes são listas de listas que funcionão como linhas e colunas para identificação

carros = [
    ["Modelo","Corola"], 
    ["Fabricante","Toyota"], 
    ["Ano",2020]
    ]

#print (carros[0][1] + carros[1][1])
carros [0] [1] = "Corola Cross" 

carros.append(["Cor","Azul Metálico"])

for l,c in carros:
    print(l + "|" + str(c))
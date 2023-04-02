#chave/key - Valor/Value
#Pode existir um dicionario dentro de um dicionario
carro = {"Fabricante":"Volks Waguen",
         "Modelo":"Jetta",
         "Ano": "2023",
         "Cor":"Azul Metálico"
}

carro["Diferenciais"] = "Suspensão a ar"  #Adicionando valor ao dicionario

carro.pop("Diferenciais") #Removendo valor do dicionario = del carro("Diferenciais")

print("Tamanho do Dicionario: " + str(len(carro)))

#carro.clear limpa todo o dicionario

""" 
if "Modelo" in carro:
    print("SIM, Modelo é uma chave")

carro ["Modelo"] = "Jetta Turbo" 

print(carro["Modelo"]) #Apontando para a chave ele retorna o modelo 

for x in carro:     #percorre as chaves
    #print(x)     #chave
    print(carro[x])

for c,v in carro.items(): #imprime linha e coluna
    print(c + ": " + v)
"""
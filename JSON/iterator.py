#Iteradores são objetos que representão o fluxo de dados este objeto retorna os dados um elemento por vez

""" carros = ["Corola","Jetta","Golf GTI","Range Rover Evoke"]

itCarros = iter(carros) #Cria o objeto tipo iter que percorre os elementos da lista um de cada vez

print(next(itCarros))   #a cada vez que chamar o 'next' ele percorre um item da lista
print(next(itCarros)) 
print(next(itCarros))
print(next(itCarros)) """



carros = ["Corola","Jetta","Golf GTI","X1","Mercedez GLA","Range Rover Evoke", "X6"]

itCarros = iter(carros) #Cria o objeto tipo iter que percorre os elementos da lista um de cada vez

while itCarros:
    try:
        print(next(itCarros))    #a cada vez que chamar o 'next' ele percorre um item da lista
    except StopIteration:
        print("Fim da lista!")
        break           #para parar a execução do while
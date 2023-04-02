class carro:                                                                         #cria a classe carro e define suas caracteristicas
    velMax = 0
    ligado = False
    cor = ""

c1 = carro()                                                                        #cria um objeto da classe carro
c2 = carro()
c3 = carro()

c1.velMax = 260                                                                   #atribui valores ao objeto da classe carro
c1.cor = "Azul Metálico"
c1.ligado = False

print(f'Velocidade Maxima: {c1.velMax}')
print(f'Cor: {c1.cor}')
print(f'Estado: {"Carro Ligado" if False else "Carro Desligado"}') 
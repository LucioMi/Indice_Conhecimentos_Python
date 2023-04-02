class carro:  #cria a classe carro e define suas caracteristicas
    modelo = ""
    velMax = ""
    cor = ""
    def __init__(self, m,v, c):  #este é o 'metodo' função que é chamada quando se cria um objeto
        self.modelo = m
        self.velMax = v
        self.cor = c
    def imprimir(self):
        print(f'Modelo.............: {self.modelo}') 
        print(f'Velocidade Máxima..: {self.velMax}')
        print(f'Cor................: {self.cor}\n')

c1 = carro("Jetta", "280 Km/h ", "Azul Metálico")            #cria um objeto da classe carro
c2 = carro("Golf GTI", "310 Km/h ", "Azul Metálico")
c3 = carro("Range Rover Evoke", "260 Km/h ", "Preto Fosco")

c1.imprimir()
c2.imprimir()
c3.imprimir()

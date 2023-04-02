class humano:  #classe base, classe pai, superclasse
    def __init__(self, nome, altura, peso):
        self.nome = nome
        self.altura = altura
        self.peso = peso
    def imprimir(self):
        print(f'Nome..: {self.nome}\nAltura: {self.altura}\nPeso..: {self.peso}')

class classe(humano):  #classe filho
    def __init__(self, nome, altura, peso):
        self.tipo = "Sardinha"             #Nova caracteristica atribuida a essa nova classe
        super().__init__(nome, altura, peso)    # 'super' CHAMA PROPRIEDADES DA CLASSE PAI (EX: super().altura)
    def tipoDeHumano(self):
        print(f'Nome..: {self.nome}\nAltura: {self.altura}\nPeso..: {self.peso}\nTipo..: {self.tipo}')

class nivel(classe):         #Uma classe que herda outra classe
    def __init__(self, nome, altura, peso):
        super().__init__(nome, altura, peso)
        self.nivel = "Classe Media"      #Nova caracteristica atribuida a essa nova sub-classe
    def nivelDeHumano(self):
        print(f'Nome..: {self.nome}\nAltura: {self.altura}\nPeso..: {self.peso}\nTipo..: {self.tipo}\nNivel.: {self.nivel}')


""" h1 = nivel("lucio","1,73","57 Kg")     #atribuindo valor a classe pai
h1.tipo ="Tubarão"                     #atribuindo valor a classe filho
h1.nivel = "Multimilionário"           #atribuindo valor a subclasse
h1.nivelDeHumano()                     #imprimindo metodo da subclasse """
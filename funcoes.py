r = lambda x,funcao : x + funcao(x)
res = r (2, lambda x : x*x)
print(res)
""" 

print((lambda a,b : a*b) (5,1000))   #cria uma função lambda em uma linha sem associar a um 'nome' e ja passando os parametros


soma = lambda a,b : a+b   #cria uma função anonima lambda que soma a +b

print(soma(12,18))


valores = [10,20,30,40]

def somar(num):          #Tambem é possivel passar uma lista para uma função
    r = 0
    for n in num:
        r+=n
    print("Soma = " + str(r))

somar (valores)


def carros(c="Golf GTI"):    #Se chamar a função sem falar o valor ela imprime o valor prestabelecido se falar ela imprime oque falar
    print("Modelo: " + c)

#carros("Evoke")
carros()


def textos (*txt):   #Representa valores arbritarios (pode passar quantos valores voçe quiser   )
    for t in txt:
        print(t)

textos("Ailton", "Vanderly", "Ana", "Lucio") """
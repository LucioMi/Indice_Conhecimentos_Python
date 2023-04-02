#Funçãode uma linha só
r = lambda x,funcao : x + funcao(x)
res = r (2, lambda x : x*x)
print(res)


#cria uma função lambda em uma linha sem associar a um 'nome' e ja passando os parametros
print((lambda a,b : a*b) (5,1000))   


#cria uma função anonima lambda que soma a +b
soma = lambda a,b : a+b   

print(soma(12,18))


#Tambem é possivel passar uma lista para uma função
valores = [10,20,30,40]

def somar(num):          
    r = 0
    for n in num:
        r+=n
    print("Soma = " + str(r))

somar (valores)


#Se chamar a função sem falar o valor ela imprime o valor prestabelecido se falar ela imprime oque falar
def carros(c="Golf GTI"):    
    print("Modelo: " + c)

#carros("Evoke")
carros()


#Representa valores arbritarios (pode passar quantos valores voçe quiser)
def textos (*txt):   
    for t in txt:
        print(t)

textos("Ailton", "Vanderly", "Ana", "Lucio")
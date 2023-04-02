""" try:
    print(x)
except NameError:      #um except especificando um tipo de erro
    print("'x' nao esta definido")
except:                #um except geral
    print("Erro desconhecido") """



""" x = "Lúcio"

try:           #Rotina completa de tratamento de erros
    print(x)
except:                #um except geral
    print("ERRO")
else:                  #um try except tambem pode ter um else que vai ser executado se tudo der certo
    print("Tudo certo")
finally:              #Imprime independente se deu certo ou se caiu em alguma excessão
    print("Fim do tratamento") """



num = -10

if type(num) is not int:    #se 'num' não for inteiro
    raise Exception("Valor não permitido")     #outro jeito de gerar uma exceção com o comando "raise Exception"
else:
    print(num)




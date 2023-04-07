import os #para poder apagar os arquivos

nome = "teste.txt"
""" 
'r' - read - Abrir para leitura  ===  'a' - append - Anexar no final do arquivo  ===  w - write - Escrever no arquivo  ===  x - create - Cria um arquivo  ===  
t - text - Abre o arquivo em modo texto(ja vem de padrão abrindo txt)  ===  b - binari - Abre o arquivo em modo binário 
"""
"""=============================================================================================================================================================
                                                          ESCREVENDO E ADICIONANDO NO ARQUIVO
============================================================================================================================================================="""

""" file = open("ARQUIVOS/"+nome,"w") #Abre oarquivo ('open')

#write apaga tudo e reescreve ele não subscreve, pra subescrever isso deve usar append
file.write("Percistência!\nNada no mundo pode superar a persistência.\nO talento não supera! Não há nada mais comum do que talêntoso fracassados.\n")

#fecha o arquivo
file.close()

file = open("ARQUIVOS/"+nome,"a") #Abre oarquivo ('open')

file.write("A educação não supera o mundo esta cheio de tolos educados.")

file.close()
 """
"""=============================================================================================================================================================
                                                                 LENDO O ARQUIVO  
============================================================================================================================================================="""

""" f = open ("ARQUIVOS/" + nome,"rt")

#faz a leitura do arquivo (pode limitar os caracteres ex: f.read(10))
print(f.read())

#Lê apenas uma linha do arquivo por vez, se chamar de novo ele le outra e retorna uma string
print(f.readline())
print(f.readline())

#Opção para substituir o readline
for l in f:
    print(l)

f.close() """

"""=============================================================================================================================================================
                                                                   DELETANDO O ARQUIVO  
============================================================================================================================================================="""

""" f = open("ARQUIVOS/teste2.txt","x")


f.close()  """

#para apagar um arquivo é necessario usar o modulo 'os'
if os.path.exists("ARQUIVOS/teste2.txt"):     #so uma possibilidade de if que eu achei interessante
    os.remove("ARQUIVOS/teste2.txt")
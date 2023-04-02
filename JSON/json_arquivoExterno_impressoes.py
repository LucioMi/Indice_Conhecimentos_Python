import json


#Abrindo um arquivo json externo e atribuindo a uma variavel (repare que como é um arquivo externo foi usado 'load' em vez de 'loads')
with open("JSON/json_arquivo_externo.json") as f:
    jogador = json.load(f)

#Criando um arquivojson no proprio python
""" jogador_json = '{"nome":"lucio","time":"galo","gosta":["python","back-end","c++","database"],"metas":[{"tipo":"trabalho","recurso":0},{"tipo":"realização","recurso":0},{"tipo":"felicidade","recurso":0}]}' 

jogador_dict = json.loads(jogador_json)"""

""" 
jogador_json = {  #mostrando em estrutura de dicionario para facilitar a manipulação
                "nome":"lucio",
                "time":"galo",
                "gosta":["python","back-end","c++","database"],
                "metas":[{"tipo":"trabalho","recurso":0},
                         {"tipo":"realização","recurso":0},
                         {"tipo":"felicidade","recurso":0}]}
 """

""" #imprime todo o conteudo do dicionario
print(jogador_dict)  """

""" #imprime somente as keys do dicionario
for c in jogador_dict:   
    print(c)
 """
""" #imprime chave e valor do dicionario
for i in jogador_dict.items():
    print(i) """
""" 
#imprime os valores do dicionario
for v in jogador_dict.values():
    print(v) """

""" #imprime campo expecifico com uma posição no caso 'time'
print(jogador_dict["time"]) """ 

""" #imprime campo expecifico com duas posições no caso 'gosta' na posição que esta o 'c++'
print(jogador_dict["gosta"][2])  """

""" #imprime todos os items do campo "gosta"
for im in jogador_dict["gosta"]:
    print(im) """

""" #imprime todos os items de 'meta' que são dicionarios
for a in jogador_dict["metas"]:
    print(a) """

#imprime todos os items de 'meta' que são dicionarios, mas seleciona apenas os do campo tipo
for a in jogador_dict["metas"]:
    print(a["tipo"] + "___" + str(a["recurso"]))   #imprime 'tipo' e 'recurso'
    #print(a ["tipo"])   #imprime so o tipo



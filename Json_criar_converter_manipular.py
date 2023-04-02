import json

#cria um arquivo do mesmo modelo de um arquivo json 
carros_json = '{"marca":"porshe", "modelo":"Cayenne","cor":"vermelha"}'  


""" 
'transforma' o arquivo json em um dicionario dai permitindo se manipular este arquivo igual se manipula um dicionario pode ser manipulado do 
 mesmo tipo que se manipula um dicionario 
 """
""" carros = json.loads(carros_json) 

print (carros ["modelo"])    #manipulando igual em um dicionario

for x in carros.items():    #manipulando igual em um dicionario (imprime tudo)
    print(x)

for x in carros:    #manipulando igual em um dicionario (imprime tas chaves)
    print(x)

for x in carros.values():    #manipulando igual em um dicionario (imprime o conteudo das chaves)
    print(x)

for k,v in carros.items():    #manipulando igual em um dicionario (imprime chave e valor)
    print(k,v) """



#CONVERTENDO DICIONARIO EM JSON
carros_dicionario = {"marca":"porshe", 
               "modelo":"Cayenne",
               "cor":"vermelha"
} 

carros_json2 = json.dumps(carros_dicionario) #função que 'transforma' o dicionario em json

print(carros_json2) #imprime o arquivo json
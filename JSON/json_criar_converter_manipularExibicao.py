import json

#dicionario ===> objeto json
carros_dicionario = {"marca":"porshe", 
               "modelo":"Cayenne",
               "cor":"vermelha"
}

#list ===> array json
carros_list = ["Toyota", "Volkswagem","Range Rover","Porshe"]

#tupla ===> array json
carros_tuple = ("Toyota", "Volkswagem","Range Rover","Porshe","Ferari")


""" carros_json = json.dumps(carros_tuple)   #"transforma" lista tupla ou dicionario em json """


""" indent=5 = É O NUMERO DA IDENTAÇÃO QUE O ARQUIVO JSON IRA ADIQUIRIR
    separators=(":","==>") = É O SEPARADOR QUE SERA SUBSTITUIDO NO AQUIVO JSON
    sort_keys=True = ORGANIZA AS KEYS DO ARQUIVO JSON EM ORDEM ALFABETICA """
carros_json = json.dumps(carros_dicionario, indent=5, separators=(":","==>"), sort_keys=True)  


print (carros_json)

 
import datetime

data = datetime.datetime.now()    #retorna ano\mes\dia\hora\minuto\segundo\milissegundo

nascimento = datetime.date(1997,5,6)  #cria um objeto do tipo data apenas

print(data.day)       #seleciona para imprimir somente o dia

print(nascimento)     #imprime o objeto tipo date que eu criei

print(nascimento.month)  #imprime somente o mes do elemento date que eu criei


"""  FUNCÕES DO 'strtime': %a (dia da semana resumido em txt), %A(dia da semana completo em txt), %w (retorna o numero do dia da semana em 
numerico), %d ( retoena o dia do mês em numerico), %b(texto mes abreviado), %B (testo mes completo), %m (num do mes), %y(ano com 2 digitos), 
%Y (ano com 4 numeros), %H (hora com 2 digitos, 00-23), %I (hora com dois digitos, 00-12), %p (AM / PM), %M (minutos), %S(segundos), %f (microssegundos), %j (dia do ano, 365), %W 
(numero da semana do ano) """
print(nascimento.strftime("%A"))  #imprime o dia da semana que deu esse elemento do tipo date que eu criei

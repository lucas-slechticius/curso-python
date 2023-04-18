# Aqui vamos listar a variavel s
'''
s = "pernambuco"
'''
"""
Diferente de outras linguagens, como C ou JavaScript
o For tem um uso bem unico em python, nesse exemplo abaixo
seria o seguinte

for 
se o x estiver na variavel s
printar, ou seja
o IN é usado para VERIFICAR

como toda String, é para o computador uma
lista de "char" (caractere)

Ele vai listar até achar.
"""

'''
for x in s:
    print(x)
'''

"""
Agora, para fazer um for parecido com o "tradicional" de outras
linguagens orientadas a objeto, como
for (x = 0; x < 5; x = x++)

você executa dessa maneira:
"""
'''
for n in range(6): 
    print(n)

# Dessa maneira, é executado uma lista numerica, do 0 ao 5.
'''
'''
Você ainda consegue efetuar + 2 execuções para o range, como
por exemplo, um limite entre listas:

'''
'''
for y in range(2,10):
    print(y)

#Ou mais absurdo ainda, colocando de quanto em quanto deve acrescentar.
# se entendermos que o primeiro (->'n',<- 'x', 'y') significa o
# inicio da lista, e o segundo ('n', -> 'x'<-, 'y') significa o 
# final da lista, o ultimo ('n','x',->'y'<-) representa de quanto
# em quantos numeros deve avançar até o final, como uma soma, é incrivel.
# veja o exemplo a baixo

for x in range(2, 50, 5):
    print(x)
'''
'''
Saída:
2
7
12
17
22
27
32
37
42
47
Isso significa que você pode basicamente imprimir listas como
tabuadas!! sensacional isso.

'''
'''
#exemplo da tabuada do 2
print(" ")
for x in range(2, 21, 2):
    print(x)
'''
"""
saída:
2
4
6
8
10
12
14
16
18
20

"""

for x in range(6):
    print(x)
else:
    print("Chegamos ao fim")
    

lista = ["chicago", "Queens", "Salvador", "Porto Alegre"]
print(lista)

lista2 = [1, 2, 7, 8, 10]
print(lista2)

lista3 = [2.0, 2.5, 6.3]
print(lista3)

lista4 = [True, False]
print(lista4)

lista5 = ["Lucas", 20, 1.90, True, 3, "Slechticius"]
print(lista5)
'''
print(type(lista5))

print(lista5[1])

print(lista5[-5])

print(lista5[::])
'''

##Slicing

print(lista5[1:]) #usar o slice, permite que eu escolha a ordem da lista
print(lista5[2:])
print(lista5[:3]) #Ele retorna do começo da lista até o index -1
print(lista5[1:4])
print(lista5[1:5:2]) # O ultimo numero se assemelha a função Range, pulando de valor a valor

#Funciona também com strings

nome = "Lucas"

print(nome[2:5])

#Funções, concatenar listas


list1 = [2.0, 3.5, 4.7]
list2 = [1, 5, 9, 11, 15]
list3 = ["nome", "Lucas", "nome", "teste"]

#Função Len é equivalente a 'lenght', para ver a largura da lista

print(len(list1))
print(len(list2))
print(len(list3))

#Funções que só podem ser utilizadas com tipos de dados númericos;

'''
int
float
complex
'''
#sum() serve para SOMAR os dados valores dentro da lista.
print(sum(list1))
#max() Retorna o valor numerico mais alto desse array
print(max(list1))
#min() faz o contrario do max(). Ele retorna o menor valor do array
print(min(list1))

#Functions

nome = "Curso Python"
valor = range(10)

print(nome)
print(valor)

value = list(range(10))
print(value)
"""
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
"""

list4 = list("Curso de Python")
print(list4)
'''
['C', 'u', 'r', 's', 'o', ' ', 'd', 'e', ' ', 'P', 'y', 't', 'h', 'o', 'n']
'''
elemento = 8
if elemento in value:
    print("Este elemento esta dentro da lista")


# Alterar itens dentro de arrays 

lista_animais = ["Gato", "Cachorro", 'Peixe', "Girafa", "Tubarão", "Falcão", "Capivara"]
print(lista_animais)

lista_animais[1] = "Cavalo"
print(lista_animais)

lista_animais[1:3] = ["Peixinho Dourado", "Macaco Prego", "Sagui"]
print(lista_animais)

lista_animais[1:3] = ["Leão Marinho"]
print(lista_animais)

# Adicionar elementos em Lista

print(30 * '-')
print('\n')

# Index     0       1         2
honda = ["Civic", "Accord", "Fit"]
print(honda)

for x in range(len(honda)):
    print(x, honda[x])

"""
Nesse caso, como o 'x' dentro do for, vai passar por cada unidade numerica do tamanho da lista
(nesse caso 3 unidades) você pode pedir para printar o valor do index q a lista está percorrendo
print(x ,) <--- e logo a pós, chamar a lista de novo, só de dessa vez, em vez de chamar a lista
como por exemplo "honda[0,1,2]", você pode chamar pelo 'X', já q ele vai passar por esses index!

Output:

0 Civic
1 Accord
2 Fit
"""

## Como transformar var string em lista
print("\n")
print(30 * "-")

varstring = "toyota, supra"
toyota = list(varstring)
print(toyota)
'''

varstring = varstring.split()
print(varstring)

Output: 

['toyota,', 'supra']

Atenção!!
Percebemos q nesse exemplo, a virgula no "toyota," permaneceu,
para resolver esse simples problema, basta colocar dentro da
função, entre aspas, o que deve ser usado como parametro no
split: 
'''

varstring = varstring.split(',')#<--- DESSE JEITO!
print(varstring)


## Como ADICIONAR E REMOVER itens dessa lista:
print("\n")
print(30 * "-")

honda.append("NSX")#append() só consegue adicionar um item por vez.
print(honda)    # Sendo possível q o mesmo seja um array. na linha 167 tem a explicação.

""" Tendo mais um detalhe, o .append() você não escolhe em qual indice ele vai ficar
Ou seja, ele sempre vai criar um novo indice, ficando no ultimo lugar da lista.
"""

for x in range(len(honda)):
    print(x, honda[x])


#Para adicionar varios valores no append(), basta inserir como uma lista
"""
honda.append(["VTEC", "CVCC"])
print(honda)
print(len(honda))

No python, vai gerar o seguinte output:

['Civic', 'Accord', 'Fit', 'NSX', ['VTEC', 'CVCC']]
5

Ou seja, o tamanho da lista consta como 5 objetos,
porem o quinto, é uma lista, ou seja, uma lista 
dentro de outra lista, diferente não?

"""

'''
.insert() tem a mesma função que o .append(), com
a única diferença é que nele você pode atribuir
em qual indice você quer colocar, mas ainda tem a
limitação de colocar apenas um objeto por vez.
'''

#o .inset() vai pedir 2 elementos, sendo o primeiro o lugar do indice, e depois o objeto.
honda.insert(1, "Honda Civic 1995 Vtec EX")
print(honda)

print("\n")
print(30 * "-")

#Como adicionar multiplos objetos. --> .extend()

honda.extend(["S200","Prelude"])
print(honda)

# Como remover e ordenar Listas

honda.pop()
print(honda)

"""
.pop()
Ele remove um conteúdo na lista, utilizando dessa maneira
sem atribuir ou escolher qual indice, ele sempre vai
remover o ultimo item da lista
before:
['Civic', 'Honda Civic 1995 Vtec EX', 'Accord', 'Fit', 'NSX', 'S200', 'Prelude']
after:
['Civic', 'Honda Civic 1995 Vtec EX', 'Accord', 'Fit', 'NSX', 'S200']
"""
honda.pop(1)
print(honda)

honda.remove("Civic") #Pelo .remove, você escolhe por string qual deseja remover
print(honda)

#Função del => de Deletar, ele deleta a lista completamente, ou por indice

'''
del honda

'''

del honda[2]
print(honda)

"""
Ok, mas usando o "del lista" eu literalmente deleto a memoria da lista,
e se eu quero mante-la? 
"""

civic = ["Motor Vtec", "Rodas", "Volante", "Portas", "Transmissão", "Embreagem"]
print(civic)

civic.clear()
print(civic)

""" .clear literalmente Limpa a sua lista, porém mantendo ela na memória.
Output:
['Motor Vtec', 'Rodas', 'Volante', 'Portas', 'Transmissão', 'Embreagem']
[] <--- Depois do .clear
"""

"""
Com isso temos
.clear() <- Limpa
del <- Deleta completamente
.pop() <- Remove por indice
.remove() <- Remove por variavel.
"""
print("\n")
print(30 * "-")

# COMO ORDENAR LISTA
'''
.sort()
'''

engine = ["freios","pistoes","freio de mao","acelerador","embreagem","cabeçote","bomba de gasolina"]
print(engine)
engine.sort() #Sem argumentos, ele ordena em alfabetico / crescente (para int e float)
print(engine)
""" além de ordenar strings em ordem alfabetica, também ordena int's"""

vel = [1,10,120,5,50,70]
print(vel)
vel.sort(reverse = True)#<-- Decrescente
print(vel)
'''
Métrica de curiosidade.

Se você executar o código

vel.reverse() <- Usamos a função reverse, sem o .sort()

Ele vai inverter a lista, porém sem ordenar.
'''
print("\n")
print(30 * "-")


nomes = ["Ana", "Lucas", "Roberto", "Rafael", "Joao", "notch", "bernardo"]
print(nomes)
nomes.sort()
print(nomes)

"""O que acontece nesse exemplo é que o .sort() ordena em ordem alfabetica
seguindo a ordem de letras upper e down case.
saindo assim no output:

['Ana', 'Joao', 'Lucas', 'Rafael', 'Roberto', 'bernardo', 'notch']

Sabmos que depois de Ana, em teoria, deveria ser o 'bernardo', pois é a letra
b, mas o sort separa upper de downcase.
"""

#Aqui tem a solução

nomes.sort(key = str.lower)#<- Aqui eu peço que a key, seja "str(ing).lower" assim podemos solucionar essa lista.
print(nomes)
"""output:
['Ana', 'bernardo', 'Joao', 'Lucas', 'notch', 'Rafael', 'Roberto']"""
print("\n")
print(30 * "-")


#Como copiar listas:
"""
Sabemos que isso vai gerar uma concatenação.

l1 = ["a", "b", "c"]
l2 = [1, 4, 6]
print(l1, l2)
l1 += l2
print(l1)
"""
l1 = ["a", "b", "c"]
l2 = [1, 4, 6]

l1.extend(l2) #Usando extend obtemos o mesmo resultado
print(l1)

"""
A terceira forma de concatenar (não muito usado mas tem a opção)

for x in l2:
    l1.append(x)

print(l1)
"""

# Como Copiar uma Lista
print("\n")
print(30 * "-")

ctrlc = [1,2,3]
ctrlv = ctrlc
print(ctrlv, ctrlc)

"""
ATENÇÃO!
Interessante que TODA ALTERAÇÃO FEITA em qualquer uma das listas
afetara automaticamente a outra. Exemplo:
"""

ctrlc.append(4)
print(ctrlv, ctrlc)

"""
Output before:
[1, 2, 3] [1, 2, 3]
Output after:
[1, 2, 3, 4] [1, 2, 3, 4]

"""
######
"""
Segunda forma de fazer uma copia de lista:
"""

ctrlv = ctrlc.copy()
print(ctrlv)

ctrlv.append(5)

print(ctrlv, ctrlc)

"""
Output:
 (ctrlv)          (ctrlc)
[1, 2, 3, 4, 5] [1, 2, 3, 4]

utilizando .copy()
ele vai gerar uma cópia do momento em que a lista estava no código
sem gerar uma alteração naquela variavel, isso sendo então
possível adicionar novas informações nessa lista.
"""

ctrlc.append(4.5)

print(ctrlv, ctrlc)

"""
output:
 ctrlv            ctrlc
[1, 2, 3, 4, 5] [1, 2, 3, 4, 4.5]
Sem se alterar.
"""
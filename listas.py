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
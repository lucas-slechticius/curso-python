'''
Listas = coleção ordenada, mutável e que permite valores duplicados
tuplas = coleção ordenada, imutável e que permite valores duplicados
dicionarios = coleção não ordenada, mutável e que não permite valores duplicados
sets = não ordenada, imutável e que não permite valores duplicados (BASICAMENTE NÃO PODE NADA)
'''

#Os sets também são conhecidos como conjuntos

"""conjunto = {"item1", "item2", "item3"}
print(type(conjunto))
#<class 'set'>

print(conjunto)
print(len(conjunto))
"""

tupla = (1,2,3,14)

conjunt = set(tupla)
print(conjunt)

conjunt = set ((2, 3, 5 , 9))
print(conjunt)
"""

Como adicionar elementos


set1 = {1, 2, 3, 4, 5}
set2 = {"True", "False"}
set1.update(set2)
print(set1)
set1.update({"teste", 1})
print(set1)


"""

#Removendo Elementos

set1 = {1, 2, 3, 4, 5, 6, 7, True, False, "True", "False", "Lucas"}

#usando .pop e .remove
"""
set1.remove("Lucas")
set1.discard(1)
set1.pop()
print(set1)
"""

#Funções principais

set1 = {1,2,3,4,5,6,7,8,9}
set2 = {9, 8, 7, "Nagatani", "True", "Teste"}

"""
set3 = set1.union(set2)

print(set3)

set1.update(set2)


print(set1)"""

#Isso resulta apenas em números repitidos.
set3 = set1.intersection(set2)

print(set3)


#.intersection_update()Permite que você atualize o primeiro set.
set1.intersection_update(set2)

print(set1)


#Mostra os itens que não estão repetidos
set3 = set1.symmetric_difference(set2)

print(set3)

#Atualizar o proprio array
set1.symmetric_difference_update(set2)
print(set1)
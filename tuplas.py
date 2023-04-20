lista = ["item1", "item2", "item3"]



print(lista)
print(len(lista))
print(type(lista))

print(30 * "-",end = "\n")

#index    0         1         2        3        4
tupla = ("item1", "item2", "item3", "item1", "item1")
print(tupla)
print(len(tupla))
print(type(tupla))
print(tupla[2])
print(tupla.count("item1"))

# A grande diferença entre os dois, é q a tupla não é alteravel.

"""
ela só tem duas funções possíveis na verdade, que é o .index() e .count()

Ela nn pode nem inserir, nem apagar dentro de uma tupla.

Seria útil como uma váriavel que nunca vai ser alterada.
"""

print(tupla)

for variavel in tupla:
    print(variavel)

for x in range(len(tupla)):
    print(x)
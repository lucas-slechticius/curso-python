'''
Listas = coleção ordenada, mutável e que permite valores duplicados
tuplas = coleção ordenada, imutável e que permite valores duplicados
dicionarios = coleção não ordenada, mutável e que não permite valores duplicados
'''
# index   0         1
lista = ["item2","item1"]
tuplas = ("item2","item1")
# Pode se repetir itens pois essas listas tem um INDEX


#Já os dicio, é chave:valor
dicio = {"chave1" : "Nagatani", "Chave2" : 1999, "chave3" : True}

print(dicio)
print(type(dicio))
# <class 'dict'>

dicionario = {
    "nome" : "Lucas",
    "idade" : 20,
    "nacionalidade" : "Brasileiro"
}
"""Bem parecido com js
você pode quebrar linha e adicionar
como se fosse um array, bem útil"""

print(dicionario)

# {'nome': 'Lucas', 'idade': 20, 'nacionalidade': 'Brasileiro'}

print(dicionario["nome"])
# Chamar ou manipular, nn se usa o index, já q não existe, deve se usar a chave.

print(dicionario.get("idade"))

print(dicionario.keys())

print(len(dicionario))

print(dicionario.values())

if "idade" in dicionario:
    print("A chave idade existe.")

print(dicionario.items())

dic = {"nome" : "Rafael", "ano" : 1993, "valor_logico" : True} 

dic["nome"] = "Pedro"

print(dic)

dic.update({"nome":"Anna"})

print(dic)

#adicionar no dicionario

dic["idade"] = 23

print(dic)

#ou usar o update

dic.update({"Estado":"SP"})

print(dic)

#A Função popitem elimina o último item apenas da versão 3.7 e acima.
dic.popitem() #Nas outras versões (abaixo da 3.7) essa função elimina um item aleatório
print(dic)

dic.pop("valor_logico")
print(dic)

del dic["ano"]
print(dic)

dic.clear()
print(dic)

dic = {"nome" : "Rafael", "ano" : 1993, "valor_logico" : True} 

print("\n")


for x in dic:
    print(dic[x])
    print(x)
print("\n")

for x in dic.values():
    print(x)
print("\n")

for x in dic.keys():
    print(x)
print("\n")

for x in dic.items():
    print(x)
print("\n")

for x, y in dic.items():
    print(x, y)
print("\n")


dic = dicio.copy()

print(dic)

dic2 = dict(dic)

print(dic2)

#Metodo Fromkeys

#index    0       1        2
tupla = ("item1","item2","item3")
tupl = ("teste1","teste2","teste3")
dicin = dict.fromkeys(tupla,tupl)
print(dicin)

dicty = {
    "dicio": {
    "nome": "Lucas",
    "idade": 23
    },
    "dic":{
    "nome":"Rafael",
    "idade":35,
    "dependentes":{
    "nome" : "Ana Julia",
    "idade":5
    }
    }
}
print(dicty)
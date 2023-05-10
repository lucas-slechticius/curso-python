#Paradigma Iperativo
#Imperare

#variáveis, atribuições e sequência
#C, Fortran, Cobol, Basic, Pascal, Ada, Modula-2

#Bloco externo

""" 
nome = "Nagatani"
def minha_fun():
    #Vloco interno * bloco interno é conhecido como corpo da função
    tupla = 2, 4, 5
    nome = "Ana" #Variável local
    print(nome)
    print(tupla)
    if nome == "Ana":
        print("Impressão do bloco interno da condição if")
    for x in tupla:
        print(x)

print(nome)
minha_fun()

### Retorno de Funções \/

lista = [1,2,3,4,5]
print(lista)

retorno = lista.pop()
print(lista)
print("Retorno da função pop: ", retorno)

Saida =

[1, 2, 3, 4, 5]
[1, 2, 3, 4]
Retorno da função pop:  5



def ola_mundo():
    return "ola mundo"
 
print(ola_mundo())
"""

def par_impar():
    numero = 4
    if (numero % 2) == 0:
        return "numero par"
    return "numero impar" # Return Sai da função.

print(par_impar())
"""
No python, se a gente reescrevesse o código dessa maneira:
def par_impar():
    numero = 4
    if (numero % 2) == 0:
        print("numero par")
    print("numero impar") 
print(par_impar())
SAÍDA:
numero par
numero impar

Porque quando usamos o return isso não acontece?

Pois assim que o código lê o primeiro RETURN, o python já entende que o if já terminou, 
e não continua a leitura.
"""
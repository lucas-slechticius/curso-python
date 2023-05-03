#Paradigma Iperativo
#Imperare

#variáveis, atribuições e sequência
#C, Fortran, Cobol, Basic, Pascal, Ada, Modula-2

#Bloco externo
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
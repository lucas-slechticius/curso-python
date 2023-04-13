'''Escopo de variaveis'''

'''
as variaveis globais (ficam fora de funções)

as variaveis locais (são declaradas dentro de funções e não podem ser alteradas)
'''

x = 5
print("Valor da variavel local: ", x)

def funcao():
    x = 3
    print("Valor da variavel local: ", x)

funcao()
print("Valor da variavel global: ", x)

nome = 'Gabriel' #nome 
altura = 1.74 #altura
cpf = "000.000.000-00" #cpf
idade = 23 #idade
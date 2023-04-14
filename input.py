'''
Função input() - função para receber dados do usuário

'''

nome = input("Qual eh o seu nome? ")
print("Ola, ",nome)

idade = int(input("Qual a sua idade? "))

ano_nascimento = 2023 - idade

print("seu nome eh: {0} e voce nasceu em {1}".format(nome,ano_nascimento))

'''Maneira mais eficiente 

print(f"seu nome eh: {nome} e voce nasceu em {idade}")


'''
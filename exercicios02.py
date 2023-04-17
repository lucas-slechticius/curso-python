'''
1 - Implemente um programa que receba a idade de uma pessoa e imprima mensagem de
acordo com os critérios:
● Menor de 16 anos: MENOR
● Entre 16 e 18 anos: EMANCIPADO
● Maior de 18 anos: MAIOR


'''
idade = int(input("Informe a sua idade: "))

if idade >= 18:
    print(f"Voce tem {idade} logo, eh de maior")
elif idade >= 16 and idade < 18:
    print(f'Voce tem {idade}, logo eh emancipado')
else:
    print("voce eh de menor")

# Exercicio 02
'''
 Implemente um programa que receba a idade de um nadador e imprima a sua
categoria seguindo as regras:

Infantil A 5-7 anos 
Infantil B 8-10 anos
Juvenil A  11-13 anos
Juvenil B  14-17 anos
'''




idade_nadador = int(input("Informe a sua idade para saber a sua categoria: "))

if idade_nadador >= 14 and idade_nadador <= 17:
    print("Voce esta na categoria Juvenil B")
elif idade_nadador >= 11 and idade_nadador <= 13:
    print("voce esta na categoria Juvenil A")
elif idade_nadador >= 8 and idade_nadador <= 10:
    print("Voce esta na categoria Infantil B")
else:
    print("voce esta na categoria Infantil A")

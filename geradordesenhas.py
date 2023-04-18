# maiúsculas e minúsculas
# símbolos e espaços

'''
Security = chave
5ecurt1ty = senha

hex

1=1
2=2
até 9=9
10 = a
11 = b
12 = c
13 = d
14 = e
15 = f
16 = g

'''

chave = input("Digite a base da sua senha: ")

senha = ""

for letra in chave:
    if letra in "Aa": senha = senha + "10"
    elif letra in "Bb": senha = senha + "11"
    elif letra in "Cc": senha = senha + "12"
    elif letra in "Dd": senha = senha + "13"
    elif letra in "Ee": senha = senha + "14"
    elif letra in "Ff": senha = senha + "15"
    elif letra in "Gg": senha = senha + "16"
    elif letra in "Rr": senha = senha + "#"
    elif letra in "Ss": senha = senha + "%"
    elif letra in "Mm": senha = senha + "$"
    elif letra in "Nn": senha = senha + "@"
    else: senha = senha + letra

print(senha)
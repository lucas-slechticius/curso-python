'''
Descobrir se um numero eh primo
'''

print(30 * "-")

numero = int(input("insira um numero para descobrir se o mesmo eh primo: "))

if numero > 1:
    for x in range(2, numero):
        if(numero % x) == 0:
            print("Esse nao eh primo")
            break
    else:
        print(f"Esse numero eh primo")
else:
    print("esse numero nao eh primo: numero menor ou igual a 1")

print(30 * "-")

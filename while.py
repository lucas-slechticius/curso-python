'''

Estrutura de repetição

while
for
do while*

'''

'''
a = 0

while a <= 5:
    print(a)
    a = a ++ 1
print("resultado final de a eh: ", a)
'''
# isso e para voce conseguir ver que mesmo apos o while, o a ainda repete uma ultima vez

'''
Caso voce queira impedir que o 'a' termine com um valor +1, voce ainda pode
usar dentro do while, if e if else, o exemplo do codigo ficaria assim
'''
a = 0
while a <= 5:
    print(a <= 5)
    print(a)
    if a == 5:
        break
    a = a + 1

print("resultado final de a eh: ", a)
print(a <= 5)

# Exemplo usando Else

a = 0
while a <= 5:
    print(a <= 5)
    print(a)
    a = a + 1
else:
    print(f"a nao eh menor ou igual a 5. Valor de a: {a}")
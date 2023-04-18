'''

do while

Nesse caso, python não tem um do while
como as outras linguagens, mas tem como
fazer no proprio código.

Código para adivinhar um número

'''

palpite = 0
numero = 9

while True: # 0 sempre é false, isso bugando o código, mas tem uma solução
    print("Qual o numero correto?: ")
    palpite = int(input())
    if palpite == numero:
        print("Parabens voce acertou")
        break
    else:
        print("Voce errou")
else:
    print("Erro na aplicação")
    print(bool(palpite))

#O While, quando vem com a condição true, torna o numero zero por exemplo (que naturalmente é false)
#Sempre na condição true, sem bugar o código mesmo que o palpite seja zero
#Por conta disso o While natural, vira como se fosse um do while, fazendo primeiro o código e depois 
#verificando.


print(bool(palpite))
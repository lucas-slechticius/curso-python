'''
IF, ELSE e ELIF -> (else if)
'''

x = float(input("Informe um numero que vai ser comparado: "))
y = float(input("informe o segundo numero: "))

if y > x: #SEMPRE USAR OS " : " PARA AVISAR FIM DA CONDIÇÃO
    print("o segundo numero eh maior que o primeiro")
elif y < x:
    print("o primeiro numero e maior q o segundo")
else:
    print("os numeros sao iguais")


"""
poderia ser

elif y == x:
 
Ou seja, não precisa necessariamente terminar com else

(se tiver 10 condições (elif) anteriores
apenas quando os 10 estiverem false que vai
ser levado em conta o else)
"""








print("codigo fora da condicional")

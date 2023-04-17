largura = float(input("Vamos calcular a area de um retangulo, insira a largura em centimetros: "))

altura = float(input("Agora, insira a altura em centimetros: "))

area = largura * altura

print(f"a sua area eh de {area} cm")

## Exercicio 2

quadrado = float(input("Coloque a altura do seu quadrado: "))

area_quadrado = quadrado ** 2

print(f"A area do seu quadrado eh {area_quadrado}")


## Exercicio 3

valor_original = float(input("Coloque o valor do seu produto: "))
desconto_produto = float(input("Informe o desconto: "))

desconto_produto = desconto_produto / 100

print("o valor do seu produto, era: R$", valor_original)
print("o valor do seu produto, com o desconto ficaria: R$", valor_original * (1-desconto_produto))
print("o valor do desconto foi : R$ ", valor_original * desconto_produto) 

## Exercicio 4

raio = float(input("Informe o raio do seu circulo: "))

pi = 3.14
area_circulo = pi * (raio ** 2)

print(f"a area do seu circulo, eh: {area_circulo}")

## Exercicio 5

brl = float(input("Informe o valor de reais: "))

converbrl = brl / 4.93

print(f"A conversao de reais para dolar, sendo dolar=4,93 reais, ficaria: U${converbrl} ")

us = float(input("Informe a quantidade de dolar que você quer converter para brl: "))

converus = us * 4.93

print(f"O valor de dolar para Real, estando ele em 4,93 eh: {converus}")
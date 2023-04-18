for x in range(10):
    if x == 3:
        continue
    print(x)

"""
Continue nesse contexto, ele faz o if ser true nesse caso,
e continua o código, porém o resultado da lista
sai dessa maneira:

0
1
2
4
5
6
7
8
9

faltando o 3 nesse caso, já que ele passa pela condicional, da true
e logo após o continue faz com q ele continue o processo

"""


if x == 5:
    pass

"""
esse comando, ignora o resultado, deixando a lista inalterada,
ele é utilizado pois, não pode deixar esse código sem uma resolução para o if

não pode ficar um if sem um else, porém, o pass abre essa excecão

Porém o pass deve ser usado com muita cautela, pois ela abre espaço
para o interpretador ignorar erros, já que com o pass da a entender que
assim foi requisitado.
"""

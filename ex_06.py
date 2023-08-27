"6- Substitua todos os números ímpares em arr com -1 sem alterar arr"

import numpy as np

arr = np.arange(0,11)
# A função np.where() retorna elementos escolhidos de dois arrays, dependendo de uma condição fornecida.
# Neste caso, a condição é arr % 2 == 1, ou seja, verifica se os elementos de 'arr' são ímpares.
# Se a condição for verdadeira, o valor correspondente em 'out' será -1, caso contrário, será o próprio valor de 'arr'.
out = np.where(arr % 2 != 0, -1, arr)
print(arr)
print(out)
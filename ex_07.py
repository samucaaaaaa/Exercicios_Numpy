"7- Converta uma matriz 1D para uma matriz 2D com 2 linhas:"

import numpy as np

matriz_1D = np.arange(0,10)
# OBS: Posso usar o reshape para alterar as dimensões de um array
# Devemos colocar no primeiro argumento o número de linhas e no segundo argumento o némero de colunas (devem ser proporcionais ao tamanho da array)
# Também posso simplesmente passar o número de linhas e como segundo argumento o '-1' que irá colocar o número de colunas automaticamente.
matriz_2D = matriz_1D.reshape(2, 5)
print(matriz_2D)

"4- Extraia todos os números ímpares de ‘arr’"

import numpy as np

arr = np.arange(100)
numeros_impares = arr[arr % 2 != 0]
# OBS: "numeros_impares" que é criado a partir de uma operação com a array, se torna uma array.
print(numeros_impares)
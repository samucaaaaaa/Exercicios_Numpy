"5- Substitua todos os números ímpares arr por -1"

import numpy as np

arr = np.array([0,1,2,3,4,5,6,7,8,9])
# Dessa forma fazemos com que todos os numeros impares da array receba -1
arr[arr % 2 != 0] = -1 
print(arr)



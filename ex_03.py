"3- Crie uma matriz booleana numpy 3×3 com ‘True’"

import numpy as np
# Podemos criar um array com "np.full". OBS: É muito útil para criar matrizes com valores repetidos.
# Ele é muito bom, pois podemos especificar a quantidade de linhas e de colunas como primeiro parâmetro,
# o dado que queremos que a matriz tenha como segundo parâmetro e o seu tipo como terceiro parãmetro.
array_bool = np.full((3, 3), True, dtype=bool)
print(array_bool)

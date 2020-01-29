import numpy as np
import pandas as pd
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print(matrix[0][2])
matrix = pd.DataFrame(matrix)
print(matrix.iloc[0, 2])
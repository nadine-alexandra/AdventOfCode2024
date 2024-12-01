import numpy as np

text_input = np.loadtxt("./input.txt")

col_left, col_right = text_input[:, 0], text_input[:, 1]

result = 0

while len(col_left > 0):
    id_left, id_right = np.argmin(col_left), np.argmin(col_right)

    result = result + np.absolute(col_left[id_left] - col_right[id_right])

    col_left = np.delete(col_left, id_left)
    col_right = np.delete(col_right, id_right)

print(result)


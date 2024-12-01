import numpy as np

text_input = np.loadtxt("./input.txt")

col_left, col_right = text_input[:, 0], text_input[:, 1]

result = 0

for item in col_left:
    result = result + item * np.count_nonzero(col_right == item)

print(result)

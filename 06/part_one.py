import numpy as np

position = ()
field = []
direction = "N"
result = 0

for line_nr, line in enumerate(open("input.txt")):
    line = np.array(list(line.strip()))
    field.append(line)

    if "^" in line:
        position = (line_nr, np.argwhere(line == "^").flatten()[0])

rows, cols = len(field), len(field[0])

while True:
    field[position[0]][position[1]] = "X"

    if direction == "N":
        if position[0] == 0:
            break
        elif field[position[0] - 1][position[1]] == "#":
            direction = "O"
            position = (position[0], position[1] + 1)
        else:
            position = (position[0] - 1, position[1])

        continue
    if direction == "O":
        if position[1] == cols - 1:
            break
        elif field[position[0]][position[1] + 1] == "#":
            direction = "S"
            position = (position[0] + 1, position[1])
        else:
            position = (position[0], position[1] + 1)

        continue
    if direction == "S":
        if position[0] == rows - 1:
            break
        elif field[position[0] + 1][position[1]] == "#":
            direction = "W"
            position = (position[0], position[1] - 1)
        else:
            position = (position[0] + 1, position[1])

        continue
    if direction == "W":
        if position[1] == 0:
            break
        elif field[position[0]][position[1] - 1] == "#":
            direction = "N"
            position = (position[0] - 1, position[1])
        else:
            position = (position[0], position[1] - 1)

        continue

for line in field:
    result += len(np.argwhere(line == "X").flatten())

print(result)

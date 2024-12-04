word_len = len("MAS")
result = 0

with open('input.txt') as f:
    grid = f.readlines()
    rows, cols = len(grid), len(grid[0])

for row in range(rows):
    for col in range(cols):
        count = 0

        if row - 1 >= 0 and col - 1 >= 0 and row + 1 < rows and col + 1 < cols:
            diagonal_l_r = grid[row - 1][col - 1] + grid[row][col] + grid[row + 1][col + 1]
            diagonal_r_l = grid[row - 1][col + 1] + grid[row][col] + grid[row + 1][col - 1]

            count += (diagonal_l_r == "MAS") + (diagonal_l_r[::-1] == "MAS")
            count += (diagonal_r_l == "MAS") + (diagonal_r_l[::-1] == "MAS")

        if count == 2:
            result += 1

print(result)

word_len = len("XMAS")
result = 0

with open('input.txt') as f:
    grid = f.readlines()
    rows, cols = len(grid), len(grid[0])

# Horizontal
for row in grid:
    result += row.count("XMAS")
    result += row[::-1].count("XMAS")

# Vertical
for col in range(cols):
    column = ''.join([grid[row][col] for row in range(rows)])
    result += column.count("XMAS")
    result += column[::-1].count("XMAS")

# Diagonal
for row in range(rows):
    for col in range(cols):
        # Top left to bottom right
        if row + word_len <= rows and col + word_len <= cols:
            diagonal = ''.join([grid[row + i][col + i] for i in range(word_len)])
            result += (diagonal == "XMAS") + (diagonal[::-1] == "XMAS")

        # Top right to bottom left
        if row + word_len <= rows and col - word_len >= -1:
            diagonal = ''.join([grid[row + i][col - i] for i in range(word_len)])
            result += (diagonal == "XMAS") + (diagonal[::-1] == "XMAS")

print(result)

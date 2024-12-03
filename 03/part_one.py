import re

pattern = "mul\(\d+,\d+\)"
result = 0

for line in open("input.txt"):
    for match in re.finditer(pattern, line):
        numbers = match.group()[4:-1].split(",")
        result += int(numbers[0]) * int(numbers[1])

print(result)

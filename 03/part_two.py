import re

pattern = "mul\(\d+,\d+\)|do\(\)|don't\(\)"
result = 0
do = True

for line in open("input.txt"):
    for match in re.finditer(pattern, line):
        if match.group() == "do()":
            do = True
        elif match.group() == "don't()":
            do = False
        else:
            if do:
                numbers = match.group()[4:-1].split(",")
                result += int(numbers[0]) * int(numbers[1])

print(result)

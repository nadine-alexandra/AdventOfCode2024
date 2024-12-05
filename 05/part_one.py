result = 0
rules = {}


def add_to_rules(rule):
    first, second = rule.split("|")

    if first in rules:
        rules[first].append(second)
    else:
        rules[first] = [second]


def check_update(p):
    for i in range(1, len(p)):
        if p[i - 1] in rules[p[i]]:
            return False

    return True


for line in open("input.txt"):
    if "|" in line:
        add_to_rules(line.strip())
    else:
        pages = line.strip().split(",")

        if check_update(pages):
            result += int(pages[len(pages) // 2])

print(result)

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


def sort_update(p):
    swap = True

    while swap:
        swap = False

        for i in range(len(p)-1):
            if p[i] in rules[p[i + 1]]:
                tmp = p[i]
                p[i] = p[i + 1]
                p[i + 1] = tmp
                swap = True

    return int(p[len(p) // 2])


for line in open("input.txt"):
    if "|" in line:
        add_to_rules(line.strip())
    else:
        pages = line.strip().split(",")

        if not check_update(pages):
            result += sort_update(pages)

print(result)

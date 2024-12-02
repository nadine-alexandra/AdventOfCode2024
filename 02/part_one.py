import numpy as np

result = 0

with open('input.txt') as f:
    lines = f.readlines()

    for line in lines:
        report = np.fromstring(line, dtype=int, sep=' ')
        diff = np.diff(report)

        # check if levels are all increasing or decreasing
        if (diff > 0).all() or (diff < 0).all():
            if (np.absolute(diff) > 3).sum() == 0:
                result += 1

print(result)

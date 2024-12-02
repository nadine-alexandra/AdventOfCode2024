import numpy as np

result = 0


def check_report(d):
    # check if levels are all increasing or decreasing
    if (d > 0).all() or (d < 0).all():
        if (np.absolute(diff) > 3).sum() == 0:
            return True

    return False


with open('input.txt') as f:
    lines = f.readlines()

    for line in lines:
        report = np.fromstring(line, dtype=int, sep=' ')
        diff = np.diff(report)

        if check_report(diff):  # Save
            result += 1
        else:  # Problem Dampener
            for i, r in enumerate(report):
                report2 = np.delete(report, i)

                if check_report(np.diff(report2)):
                    result += 1
                    break

print(result)

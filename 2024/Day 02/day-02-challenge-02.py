import enum

from typing import List

def analyse_report(report: List[str], skip: bool=True) -> bool:
    dir = 0
    err = False

    for i in range(len(report) - 1):
        diff = int(report[i + 1]) - int(report[i])
        if dir == 0 and i == 0:
            dir = -1 if diff < 0 else 1
            continue

        new_dir = -1 if diff < 0 else 1

        if diff == 0:
            print("No change")
            err = True
        elif diff > 3 or diff < -3:
            print("Delta to big")
            err = True
        elif dir != new_dir:
            print("Direction changed")
            err = True

        if err and skip:
            return analyse_report(report[:i + 1] + report[i +2:], skip=False)

    return not err


with open("real.txt", "r") as f:
    input = f.readlines()

safe = 0
unsafe = 0

for report in (line.strip().split() for line in input):
    state = analyse_report(report)

    if state:
        print(f"{report}: Safe")
        safe += 1
    else:
        print(f"{report}: Unsafe")
        unsafe += 1


print()
print(f"Safe: {safe}, Unsafe: {unsafe}")

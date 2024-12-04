from typing import List

def analyse_report(report: List[str]) -> bool:
    dir = 0

    for i in range(len(report) - 1):
        diff = int(report[i + 1]) - int(report[i])

        if diff == 0:
            print("No change")
            return False
        elif diff > 3 or diff < -3:
            print("Delta to big")
            return False

        if dir == 0 and i == 0:
            dir = -1 if diff < 0 else 1
            continue

        new_dir = -1 if diff < 0 else 1
        if dir != new_dir:
            print("Direction changed")
            return False

    return True


with open("input.txt", "r") as f:
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

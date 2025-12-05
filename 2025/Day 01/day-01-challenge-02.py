

with open("input.txt", 'r') as f:
    input = f.readlines()

instructions = ((line[0], int(line[1:-1])) for line in input)

pos = 50
count = 0

for d, v in instructions:
    old = pos

    count += v // 100

    if d == "L":
        new = old - (v % 100)
    else:
        new = old + (v % 100)

    pos = new % 100

    if old != 0 and (new <= 0 or new >= 100):
        count += 1

    print(f"{old} {d} {v}({v%100}) {new} {pos}: {count}")

print(f"Solution: {count}")

from typing import List


class Galaxy:
    def __init__(self, y: int, x: int):
        self.y = y
        self.x = x

    def __lt__(self, other) -> bool:
        if self.y <= other.y and self.x <= other.x:
            return True
        elif self.y <= other.y and self.x > other.x:
            return True
        elif self.y > other.y and self.x <= other.x:
            return False
        else:
            return False

    def __eq__(self, other) -> bool:
        if self.y == other.y and self.x == other.x:
            return True
        return False

    def __repr__(self) -> str:
        return f"({self.y}, {self.x})"


def expand_space(space: List[str]) -> List[str]:
    rows = []
    cols = []

    for y in range(len(space)):
        if not "#" in space[y]:
            rows.append(y)

    for x in range(len(space[0])):
        empty = True

        for y in range(len(space)):
            if space[y][x] == "#":
                empty = False

        if empty:
            cols.append(x)

    new_width = len(space[0]) + len(cols)
    new_hight = len(space) + len(rows)

    for y in rows:
        space.insert(y, "." * new_width)

    for x in cols:
        for y in range(new_hight):
            space[y] = space[y][:x] + "." + space[y][x:]

    return space


def find_galaxies(space: List[str]) -> List[Galaxy]:
    galaxies = []

    for y in range(len(space)):
        for x in range(len(space[0])):
            if space[y][x] == "#":
                galaxy = Galaxy(y, x)
                galaxies.append(galaxy)

    return galaxies


def distance(a: Galaxy, b: Galaxy) -> int:
    dy = max(a.y, b.y) - min(a.y, b.y)
    dx = max(a.x, b.x) - min(a.x, b.x)

    return dy + dx


with open("day-11-input.txt", "r") as infile:
    space = [line.strip() for line in infile.readlines()]

space = expand_space(space)
galaxies = find_galaxies(space)
print(galaxies)

total = 0
pairs = []

for a in galaxies:
    for b in galaxies:
        if a == b:
            continue

        pair = (a, b) if a < b else (b, a)
        if pair in pairs:
            # print(f"{pair}: Skipped")
            continue

        print(f"{pair}: Added")
        pairs.append(pair)
        total += distance(pair[0], pair[1])

    print(len(pairs))

print(len(galaxies))
print(len(pairs))
print(f"Challenge 01: {total}")

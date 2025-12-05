from typing import List, Optional, Tuple


def next_tile(
    start_poss: Tuple[int, int], start_tile: str, invert: bool = False
) -> Optional[Tuple[int, int]]:
    poss = start_poss
    tile = start_tile
    size = -1 if invert else 1

    y, x = poss

    if tile == "|":
        y += 1 * size
    elif tile == "-":
        x += 1 * size
    elif tile == "F":
        if invert:
            y += 1
        else:
            x += 1
    elif tile == "7":
        if invert:
            x -= 1
        else:
            y += 1
    elif tile == "J":
        if invert:
            x -= 1
        else:
            y -= 1
    elif tile == "L":
        if invert:
            x += 1
        else:
            y -= 1
    elif tile == "S":
        pass
    else:
        return None

    if x < 0 or y < 0:
        return None

    return (y, x)


def trace_path(field: List[str], start: Tuple[int, int], start_tile: str) -> int:
    tile = start_tile
    path = []
    poss = start

    while tile != "S":
        path.append(poss)

        poss = next_tile(poss, tile)

        if poss in path and poss != start:
            poss = path[-1]
            poss = next_tile(path[-1], field[poss[0]][poss[1]], True)

            if poss in path and poss != start:
                return 0

        if not poss:
            return 0

        tile = field[poss[0]][poss[1]]

    prev = next_tile(start, start_tile, False)
    next = next_tile(start, start_tile, True)

    if prev in path and next in path:
        return len(path)

    return 0


with open("day-10-input.txt", "r") as infile:
    input = [line.strip() for line in infile.readlines()]

start = (-1, -1)
poss = ()
steps = 0

for y in range(len(input[0])):
    for x in range(len(input)):
        if input[y][x] == "S":
            start = (y, x)
            break

for direction in "|-J7L":
    steps = trace_path(input, start, direction)

    if steps != 0:
        break

print(f"Challenge 01: {int((steps / 2) + steps % 2)}")

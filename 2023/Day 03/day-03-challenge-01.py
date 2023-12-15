from typing import List, Tuple


class Part:
    def __init__(self, start: Tuple[int, int], end: Tuple[int, int], value: int):
        self.start_x = start[1]
        self.start_y = start[0]

        self.end_x = end[1]
        self.end_y = end[0]

        self.value = value

    def __repr__(self) -> str:
        return f"{self.start_y}, {self.start_x} - {self.end_y}, {self.end_x} = {self.value}"


def is_part_adjacent(diagram: List[List[str]], part: Part) -> bool:
    width_y = len(diagram)
    width_x = len(diagram[0])

    sy = part.start_y - 1 if part.start_y != 0 else 0
    ey = part.end_y + 1 if part.end_y + 1 < width_y else part.end_y

    sx = part.start_x - 1 if part.start_x != 0 else 0
    ex = part.end_x + 1 if part.end_x + 1 < width_x else part.end_x

    for y in range(sy, ey + 1):
        for x in range(sx, ex + 1):
            if not diagram[y][x].isdigit() and diagram[y][x] != ".":
                return True

    return False


with open("day-03-challenge-01-input.txt", "r") as infile:
    input = [line.strip() for line in infile.readlines()]

sum = 0

parts = []

start = None
end = None

for y in range(len(input)):
    for x in range(len(input[y])):
        value = input[y][x]

        if value.isdigit() and not start:
            start = (y, x)
            end = (y, x)
        elif value.isdigit() and start:
            end = (y, x)
        elif not value.isdigit() and start:
            part = Part(start, end, int(input[start[0]][start[1] : end[1] + 1]))
            parts.append(part)

            start = None
            end = None


for part in parts:
    if is_part_adjacent(input, part):
        sum += part.value

print(sum)

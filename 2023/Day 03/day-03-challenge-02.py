from typing import List, Tuple


class Part:
    def __init__(self, start: Tuple[int, int], end: Tuple[int, int], value: int):
        self.start_x = start[1]
        self.start_y = start[0]

        self.end_x = end[1]
        self.end_y = end[0]

        self.value = value

        self.sympol = ''
        self.symbol_x = 0
        self.symbol_y = 0

    def __eq__(self, other) -> bool:
        if self.start_x == other.start_x and self.start_y == other.start_y and self.end_x == other.end_x and self.end_y == other.end_y:
            return True

        return False

    def __repr__(self) -> str:
        return f"{self.start_y}, {self.start_x} - {self.end_y}, {self.end_x} = {self.value}"


class Gear():
    def __init__(self, location: Tuple[int, int], first: Part, second: Part):
        self.x = location[1]
        self.y = location[0]

        self.part1 = first
        self.part2 = second

    def __eq__(self, other) -> bool:
        return True if self.x == other.x and self.y == other.y else False


    def __repr__(self) -> str:
        return f'{self.y}, {self.x} - {self.part1.value} * {self.part2.value} = {self.part1.value *
        self.part2.value}'

def is_part_adjacent(diagram: List[List[str]], part: Part) -> bool:
    width_y = len(diagram)
    width_x = len(diagram[0])

    sy = part.start_y - 1 if part.start_y != 0 else 0
    ey = part.end_y + 1 if part.end_y + 1 < width_y else part.end_y

    sx = part.start_x - 1 if part.start_x != 0 else 0
    ex = part.end_x + 1 if part.end_x + 1 < width_x else part.end_x

    for y in range(sy, ey + 1):
        for x in range(sx, ex + 1):
            part.symbol = diagram[y][x]

            if not diagram[y][x].isdigit() and diagram[y][x] != ".":
                part.symbol_y = y
                part.symbol_x = x

                return True

    return False


def is_gear(one: Part, two: Part) -> bool:
    if one.symbol == two.symbol and one.symbol_x == two.symbol_x and one.symbol_y == two.symbol_y:
        return True

    return False


with open("day-03-challenge-01-input.txt", "r") as infile:
    input = [line.strip() for line in infile.readlines()]

sum1 = 0

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
        sum1 += part.value

print(f'Challenge 1: {sum1}')
if sum1 != 557705:
    print("You broke it")

sum2 = 0

gears = []
maybe = [part for part in parts if part.symbol == '*']

for part in maybe:
    for other_part in [other for other in maybe if other != part]:
        if is_gear(part, other_part):
            gear = Gear((part.symbol_y, part.symbol_x), part, other_part)

            if not gear in gears:
                gears.append(gear)
                sum2 += gear.part1.value * gear.part2.value

print(f'Challenge 2: {sum2}')

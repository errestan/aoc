import enum

from typing import Tuple

class Direction(enum.IntEnum):
    R = 1
    L = 0

def parse(line: str) -> Tuple[str, str, str]:
    a = line.split('=')[0].strip()
    b, c = line.split('=')[1].lstrip('( ').rstrip(')\n').split(', ')

    return (a, b, c)

with open('day-08-input.txt', 'r') as infile:
    input = infile.readlines()

instructions = [*input[0].strip()]

labels = {}

for line in input[2:]:
    current, left, right = parse(line)
    labels[current] = (left, right)

current = 'AAA'
target = 'ZZZ'
steps = 0

for i in range(100000):
    steps += 1
    instruction = instructions[i % len(instructions)]
    current = labels[current][Direction.__members__[instruction]]

    if target == current:
        break;

print(f'Challenge 01: {steps}')

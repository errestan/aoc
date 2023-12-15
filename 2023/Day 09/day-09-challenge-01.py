from typing import List

def next_value(sequence: List[int]) -> List[int]:
    differences = []
    none_zero = False

    for i in range(len(sequence) - 1):
        difference = sequence[i + 1] - sequence[i]
        differences.append(difference)

        if difference != 0:
            none_zero = True

    if none_zero:
        differences = next_value(differences)

    sequence.append(sequence[-1] + differences[-1])

    return sequence

with open('day-09-input.txt', 'r') as infile:
    input = [line.strip() for line in infile.readlines()]

answer = 0

for line in input:
    values = [int(value) for value in line.split()]
    values = next_value(values)

    answer += values[-1]

print(f'Challenge 01: {answer}')

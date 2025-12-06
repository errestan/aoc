from functools import reduce
from textwrap import wrap

INPUT_FILE = "input.txt"

def is_match(id_str, factors):
    for factor in factors:
        if factor == len(id_str):
            continue

        parts = wrap(id_str, factor)

        if all(x == parts[0] for x in parts):
            return True

    return False

def get_factors(n):
    return set(reduce(
        list.__add__,
        ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))

def is_invalid(start, end):
    invalid = []

    for id in range(int(start), int(end) + 1):
        id_str = f"{id}"
        id_len = len(id_str)

        factors = get_factors(id_len)

        if is_match(id_str, factors):
            invalid.append(id)

    return invalid

with open(INPUT_FILE, 'r') as file:
    input = file.readline().strip()


ranges = (line.split('-') for line in input.split(","))
result = 0

for start, end in ranges:
    invalid_ids = is_invalid(start, end)

    print(f"{start} - {end}: {len(invalid_ids)}")
    if len(invalid_ids):
        result += sum(invalid_ids)

print(f"The solution is: {result}")

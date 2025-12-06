INPUT_FILE = "input.txt"

def is_invalid(start, end):
    invalid = []

    for id in range(int(start), int(end) + 1):
        id_str = f"{id}"
        id_len = len(id_str)

        if id_len % 2 != 0:
            continue

        half = int(id_len / 2)

        id_one = id_str[:half]
        id_two = id_str[half:]

        if id_one != id_two:
            continue

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

INPUT_FILE = "input.txt"

def get_max_joltage(bank):
    batteries = [0] * 12
    start_pos = 0

    for i in range(0, len(batteries)):
        highest = 0
        highest_idx = 0

        stop_pos = len(bank) + 1 - (len(batteries) - i)

        for j in range(start_pos, stop_pos):
            battery = int(bank[j])

            if battery > highest:
                highest = battery
                highest_idx = j

        batteries[i] = highest
        start_pos = highest_idx + 1

    return int(''.join(str(battery) for battery in batteries))

with open(INPUT_FILE, 'r') as file:
    input = (line.strip() for line in file.readlines())

banks = (list(bank) for bank in input)
total = 0

for bank in banks:
    joltage = get_max_joltage(bank)
    print(f"{bank}: {joltage}")

    total += joltage

print(f"The solution is: {total}")

with open('day-06-input.txt', 'r') as infile:
    input = infile.readlines()

answer = 0

time = int(input[0].lstrip('Time:').replace(' ', ''))
distance = int(input[1].lstrip('Distance:').replace(' ', ''))

def compute_distance(speed: int, time: int) -> int:
    return speed * time

for i in range(int(time / 2)):
    result = compute_distance(i, time - i)
    if result > distance:
        answer += 1

print(f'Challenge 02: {(answer * 2) + 1}')

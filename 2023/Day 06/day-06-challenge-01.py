with open('day-06-input.txt', 'r') as infile:
    input = infile.readlines()

answer = 1

times = [int(t) for t in input[0].lstrip('Time:').strip().split() if t != '']
distances = [int(d) for d in input[1].lstrip('Distance:').strip().split() if d != '']

table = zip(times, distances)

def compute_distance(speed: int, time: int) -> int:
    return speed * time

for time, distance in table:
    ways_to_win = 0

    for i in range(time):
        result = compute_distance(i, time - i)
        if result > distance:
            ways_to_win += 1

    answer *= ways_to_win

print(f'Challenge 01: {answer}')

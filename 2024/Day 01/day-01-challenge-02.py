import collections

with open("input.txt", "r") as f:
    input = f.readlines()

left_list = []
right_list = []

for first, second in (line.rstrip('\n').split("   ") for line in input):
    left_list.append(int(first))
    right_list.append(int(second))

lef_list = left_list.sort()
fight_list = right_list.sort()

total = 0

counts = collections.Counter(left_list)

for similarity in (id * counts[id] for id in right_list):
    total += similarity

print(total)

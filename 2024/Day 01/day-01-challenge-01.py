
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

for diff, pair in ((max(pair[0], pair[1]) - min(pair[0], pair[1]), pair) for pair in zip(left_list, right_list)):
    print(f"{pair} = {diff}")
    total += diff

print()
print(total)

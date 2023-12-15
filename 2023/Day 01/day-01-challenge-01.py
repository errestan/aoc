with open("day-01-challenge-01-input.txt", "r") as infile:
    input = infile.readlines()

sum = 0

for line in input:
    num = []

    for char in line:
        if char in "1234567890":
            num.append(char)

    num1 = 0
    num2 = 0

    num1 = num[0]

    num2 = num[-1]

    num_str = f"{num1}{num2}"
    sum += int(num_str)

print(sum)

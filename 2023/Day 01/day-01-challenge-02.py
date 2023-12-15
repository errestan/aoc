with open("day-01-challenge-01-input.txt", "r") as infile:
    input = infile.readlines()

sum = 0

words = {"oneight": 18, "twone": 21, "threeight": 38, "fiveight": 58, "sevenine": 79, "eightwo": 82, "eighthree": 83, "one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9}

for line in input:
    num = []

    for word in words.items():
        if word[0] in line:
            print(line)
            line = line.replace(word[0], str(word[1]))
            print(line)

    for char in line:
        if char in "1234567890":
            num.append(char)

    num1 = 0
    num2 = 0

    num1 = num[0]
    num2 = num[-1]

    num_str = f"{num1}{num2}"
    print(f"{num} = {num_str}")
    sum += int(num_str)

print(sum)

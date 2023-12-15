with open('day-04-challenge-01-input.txt', 'r') as infile:
    cards = [card.strip() for card in infile.readlines()]

points = 0

for card in cards:
    winning, matching = card.split(':')[1].split('|')

    matched = [int(num) for num in matching.strip().split(' ') if num != '' and num in winning.strip().split(' ')]
    points += 1 << (len(matched) - 1) if len(matched) > 0 else 0

print(f'Challenge 01: {points}')

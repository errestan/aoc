with open('day-04-challenge-01-input.txt', 'r') as infile:
    input = [card.strip() for card in infile.readlines()]

cards = {}

for card in input:
    id = int(card.split(':')[0].lstrip('Card '))
    winning, matching = card.split(':')[1].split('|')

    if not id in cards:
        cards[id] = 1

    matched = [int(num) for num in matching.strip().split(' ') if num != '' and num in winning.strip().split(' ')]

    for i in range(1, len(matched) + 1):
        if not id + i in cards:
            cards[id + i] = 1

        cards[id + i] += cards[id]

sum = sum([num[1] for num in cards.items()])
print(sum)

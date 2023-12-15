from typing import List

class Game():
    def __init__(self, id: int, blue: int, green: int, red: int):
        self.id = id
        self.blue = blue
        self.green = green
        self.red = red

    def is_posible(self, red: int, green: int, blue: int) -> bool:
        return self.red <= red and self.green <= green and self.blue <= blue

    def __repr__(self):
        return f'{self.id}: R({self.red}) G({self.green}) B({self.blue})'

def all_posible(iterations: List[Game], red: int, green: int, blue: int) -> bool:
    for iteration in iterations:
        if not iteration.is_posible(red, green, blue):
            return False

    return True

with open('day-01-challenge-01-input.txt', 'r') as infile:
    input = infile.readlines()

sum = 0

for line in input:
    game_id, iterations = line.strip('\n').split(':')

    games = []

    for iteration in iterations.split(';'):
        colours = iteration.split(',')

        blue = 0
        green = 0
        red = 0

        for colour in colours:
            if 'blue' in colour:
                blue = int(colour.rstrip('blue'))
            elif 'green' in colour:
                green = int(colour.rstrip('green'))
            elif 'red' in colour:
                red = int(colour.rstrip('red'))

        game = Game(int(game_id.lstrip('Game ')), blue, green, red)
        games.append(game)

    if all_posible(games, 12, 13, 14):
        sum += games[0].id
        print(games)

print(sum)

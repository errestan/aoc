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

def min_posible(iterations: List[Game]) -> bool:
    min_red = -1
    min_green = -1
    min_blue = -1

    for iteration in iterations:
        if min_red == -1 or (iteration.red > 0 and min_red < iteration.red):
            min_red = iteration.red
        if min_green == -1 or (iteration.green > 0 and min_green < iteration.green):
            min_green = iteration.green
        if min_blue == -1 or (iteration.blue > 0 and min_blue < iteration.blue):
            min_blue = iteration.blue

    return min_red * min_green * min_blue

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

    sum += min_posible(games)

print(sum)

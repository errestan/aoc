import enum

STEP_SCORE = 1
TURN_SCORE = 1000

class Direction(enum.Enum):
    NORTH = 1
    EAST = 2
    SOURTH = 3
    WEST = 4

class Position:
    def __init__(self, x: int, y: int, direction: Direction):
        self.x = x
        self.y = y
        self.direction = direction

    def __str__(self):
        return f"{self.x}, {self.y}: {self.direction}"

    def __repr__(self):
        return self.__str__

class Path:
    def __init__(self, start: Position):
        self.curent = start
        self.steps = []

        self.total_steps = 0
        self.total_turns = 0

        def take_step(self, x: int, y: int, direction: Direction):
            new = Position(x, y, direction)

            if (new.x != self.current.x or new.y != self.current.y) and (new.direction ==
                self.current.direction):
                self.total_steps += 1
            elif (new.x == self.current.x and new.y == self.current.y) and (new.direction != self.current.direction):
                self.total_turns += 1

            self.steps.append(self.current)
            self.current = new


    def calculate_score(self) -> int:
        return (self.total_steps * STEP_SCORE) + (self.total_turns * TURN_SCORE)

class Maze():
    def __init__(self, input):
        self.map = []

        for x in range(len(input[0])):
            self.map.append([])

            for y in range(len(input)):
                self.map[x].append(input[y][x])

                if self.map[x][y] == "S":
                    self.start = Position(x, y, Direction.EAST)
                elif self.map[x][y] == "E":
                    self.end = Position(x, y, Direction.NORTH)

    def __str__(self):
        output = ""

        for x in range(len(self.map)):
            for y in range(len(self.map[0])):
                output += self.map[x][y]

            output += "\n"

        return output

    def __repr__(self):
        return self__str__()

with open("input.txt", "r") as file:
    input = file.read()

maze = Maze(input)

print(maze)
print(maze.start)
print(maze.end)

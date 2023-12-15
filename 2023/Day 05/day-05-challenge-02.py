from typing import List

class Mapping():
    def __init__(self, source: int, destination: int, length: int):
        self.src = source
        self.dst = destination
        self.len = length

    def contains(self, value: int) -> bool:
        return True if value >= self.src and value < (self.src + self.len) else False

    def lookup(self, value: int) -> int:
        if self.contains(value):
            return self.dst + (value - self.src)

        return value

    def __lt__(self, other) -> bool:
        if self.src < other.src:
            return True

        return False

    def __repr__(self):
        return f'{self.src}-{self.src + self.len} = {self.dst}-{self.dst + self.len}'

def parse_mappings(input: List[str]) -> List[Mapping]:
    output = []

    for line in input:
        if not line.strip():
            break

        destination, source, length = line.split()
        output.append(Mapping(int(source), int(destination), int(length)))

    return output

def lookup(value: int, mappings: List[Mapping]) -> int:
    for map in mappings:
        if map.contains(value):
            return map.dst + (value - map.src)

    return value

with open('day-05-input.txt', 'r') as infile:
    input = infile.readlines()

seeds = []

ranges = [int(seed) for seed in input[0].split(':')[1].strip().split(' ')]

for i in range(0, len(ranges), 2):
    print(f'{ranges[i]}\t{ranges[i] + ranges[i +1]}')
quit()

seed_to_soil = parse_mappings(input[3:])
seed_to_soil.sort()

soil_to_fertilizer = parse_mappings(input[28:])
soil_to_fertilizer.sort()

fertilizer_to_water = parse_mappings(input[70:])
fertilizer_to_water.sort()

water_to_light = parse_mappings(input[86:])
water_to_light.sort()

light_to_temperature = parse_mappings(input[134:])
light_to_temperature.sort()

temperature_to_humidity = parse_mappings(input[171:])
temperature_to_humidity.sort()

humidity_to_location = parse_mappings(input[201:])
humidity_to_location.sort()

locations = []

for seed in seeds:
    soil = lookup(seed, seed_to_soil)
    fertilizer = lookup(soil, soil_to_fertilizer)
    water = lookup(fertilizer, fertilizer_to_water)
    light = lookup(water, water_to_light)
    temperature = lookup(light, light_to_temperature)
    humidity = lookup(temperature, temperature_to_humidity)
    location = lookup(humidity, humidity_to_location)

    locations.append(location)

locations.sort()
print(locations[0])

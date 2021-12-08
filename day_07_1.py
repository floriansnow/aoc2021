import math

with open('day_07_input_1') as f:
    crab_positions = [int(crab) for crab in f.readlines()[0].split(",")]

potential_positions1 = dict()
potential_positions2 = dict()
for potential_position in range(max(crab_positions) + 1):
    potential_positions1[potential_position] = 0
    potential_positions2[potential_position] = 0
    for crab_position in crab_positions:
        steps = abs(potential_position - crab_position)
        potential_positions1[potential_position] += steps
        potential_positions2[potential_position] += (steps * (steps + 1)) // 2

print(min(potential_positions1.values()), min(potential_positions2.values()))

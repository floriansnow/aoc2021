with open('day_02_input_1') as c:
    course = [(entry.strip().split()[0], int(entry.strip().split()[1])) for entry in c.readlines()]

position = 0
depth = 0
aim = 0
for entry in course:
    if entry[0] == 'forward':
        position += entry[1]
        depth += aim * entry[1]
    elif entry[0] == 'down':
        aim += entry[1]
    elif entry[0] == 'up':
        aim -= entry[1]
    else:
        print(entry)

print(position * depth)
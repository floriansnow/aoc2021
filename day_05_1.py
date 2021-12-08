from fractions import Fraction


class Map:
    def __init__(self):
        self._map = dict()

    def _add_point(self, point):
        if point in self._map:
            return
        # optimization: do not add empty points (break visualization)
        self._map[point] = 0
        return
        # add all empty points
        max_x = max([point[0]] + [k[0] for k in self._map.keys()])
        max_y = max([point[1]] + [k[1] for k in self._map.keys()])
        for x in range(max_x + 1):
            for y in range(max_y + 1):
                if (x, y) not in self._map:
                    self._map[(x, y)] = 0

    def add_line(self, line):
        (x1, y1), (x2, y2) = line
        try:
            slope = (y2 - y1) // (x2 - x1)
        except ZeroDivisionError:
            slope = None
        if slope is None:
            if y2 > y1:
                r = range(y1, y2 + 1)
            else:
                r = range(y2, y1 + 1)
            for y in r:
                self._add_point((x1, y))
                self._map[(x1, y)] += 1
        elif slope == 0:
            if x2 > x1:
                r = range(x1, x2 + 1)
            else:
                r = range(x2, x1 + 1)
            for x in r:
                self._add_point((x, y1))
                self._map[(x, y1)] += 1
        else:
            if x2 > x1:
                r = range(x1, x2 + 1)
                y = y1
            else:
                r = range(x2, x1 + 1)
                y = y2
            for x in r:
                self._add_point((x, y))
                self._map[(x, y)] += 1
                y += slope

    def get_dangerous_coordinates(self):
        danger = []
        for coordinates, rating in self._map.items():
            if rating >= 2:
                danger.append(coordinates)
        return danger

    def __repr__(self):
        out = []
        line = []
        last_y = 0
        for x, y in sorted(self._map.keys(), key=lambda k: [k[1], k[0]]):
            symbol = str(self._map[(x, y)])
            if symbol == '0':
                symbol = '.'
            if last_y < y:
                out.append(line)
                line = [symbol]
            else:
                line.append(symbol)
            last_y = y
        out.append(line)
        return '\n'.join([''.join(line) for line in out])




with open('day_05_input_1') as f:
    puzzle = f.readlines()

m1 = Map()
m2 = Map()
total_lines = len(puzzle)
for index, line in enumerate(puzzle):
    print('processing line', str(index) + '/' + str(total_lines) + ':', line)
    parts = line.split()
    x1, y1 = (int(n) for n in parts[0].split(','))
    x2, y2 = (int(n) for n in parts[2].split(','))
    if x1 == x2 or y1 == y2:
        m1.add_line([(x1, y1), (x2, y2)])
    m2.add_line([(x1, y1), (x2, y2)])

print(len(m1.get_dangerous_coordinates()), len(m2.get_dangerous_coordinates()))
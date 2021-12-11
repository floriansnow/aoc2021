# Solution for Advent of Code day 11
# Copyright (C) 2021 Florian Snow <florian@familysnow.net>
#
# This program is free software: you can redistribute it and/or modify it under
# the terms of the GNU Affero General Public License as published by the Free
# Software Foundation, either version 3 of the License, or (at your option) any
# later version.
#
# This program is distributed in the hope that it will be useful, but WITHOUT
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS
# FOR A PARTICULAR PURPOSE.  See the GNU Affero General Public License for more
# details.
#
# You should have received a copy of the GNU Affero General Public License along
# with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# SPDX-FileCopyrightText: 2021 Florian Snow <florian@familysnow.net>
# SPDX-License-Identifier: AGPL-3.0-or-later

def print_grid(data):
    out = []
    for line in data:
        out.append("".join([str(x) for x in line]))
    print("\n".join(out))

def adjacent(point, data):
    for x_offset in range (-1, 2):
        for y_offset in range(-1, 2):
            x = point[0] + x_offset
            y = point[1] - y_offset
            if point != (x, y) and 0 <= x < len(data[0]) and 0 <= y < len(data):
                yield x, y

def increase_adjacent(point, flashed):
    for x, y in adjacent(point, data):
        data[y][x] += 1
        if data[y][x] > 9 and (x, y) not in flashed:
            flashed.add((x, y))
            flashed = increase_adjacent((x, y), flashed)
    return flashed

with open("day_11_input_1") as f:
    data = [[int(x) for x in line.strip()] for line in f.readlines()]

flashes = 0
step = 1
while True:
    for y, line in enumerate(data):
        for x, dumbo in enumerate(line):
            data[y][x] += 1
    flashed = set()
    for y, line in enumerate(data):
        for x, dumbo in enumerate(line):
            if dumbo > 9 and (x, y) not in flashed:
                flashed.add((x, y))
                flashed = increase_adjacent((x, y), flashed)

    flashes += len(flashed)
    for x, y in flashed:
        data[y][x] = 0

    if step == 100:
        print(flashes)

    if len(flashed) == len(data) * len(data[0]):
        print(step)
        break

    step += 1

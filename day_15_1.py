# Solution for Advent of Code day 15
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

import heapq
from collections import defaultdict


def adjacent(point, data, diagonals=True):
    for x_offset in range(-1, 2):
        for y_offset in range(-1, 2):
            if not diagonals and x_offset != 0 and y_offset != 0:
                continue
            x = point[0] + x_offset
            y = point[1] - y_offset
            if point != (x, y) and 0 <= x < len(data[0]) and 0 <= y < len(data):
                yield x, y


def parse_data(raw_data):
    data = defaultdict()
    for y, line in enumerate(raw_data):
        for x, risk in enumerate(line):
            data[(x, y)] = risk
    return data


def get_least_risky_path(map, start, end):
    unvisited = {point: None for point in map.keys()}
    unvisited[start] = 0
    visited = dict()
    heap = [(0, start)]

    while True:
        risk, point = heapq.heappop(heap)
        if point == end:
            return risk
        if point in visited:
            continue
        for adjacent_point in adjacent(point, raw_data, diagonals=False):
            if adjacent_point in visited:
                continue
            new_risk = risk + map[adjacent_point]
            if unvisited[adjacent_point] is None or unvisited[adjacent_point] > new_risk:
                unvisited[adjacent_point] = new_risk
                heapq.heappush(heap, (new_risk, adjacent_point))
        visited[point] = risk


def get_next_value(value):
    value += 1
    if value > 9:
        return 1
    return value


def get_expanded_data(data, factor):
    width = len(data[0])
    height = len(data)
    for _ in range(factor - 1):
        for line in data:
            old_line = line[-width:]
            for value in old_line:
                line.append(get_next_value(value))
    for _ in range(factor - 1):
        old_lines = data[-height:]
        for line in old_lines:
            new_line = [get_next_value(value) for value in line]
            data.append(new_line)
    return data


with open("day_15_input_1") as f:
    raw_data = [list(map(int, line.strip())) for line in f]

map = parse_data(raw_data)
risk = get_least_risky_path(map, (0, 0), (len(raw_data[0]) - 1, len(raw_data) - 1))
print(risk)

data = get_expanded_data(raw_data, 5)
map = parse_data(data)
risk = get_least_risky_path(map, (0, 0), (len(data[0]) - 1, len(data) - 1))
print(risk)

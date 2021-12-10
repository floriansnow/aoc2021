# Solution for Advent of Code day 9
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

def get_adjacent_heights(data, point):
    x, y = point
    adjacent_heights = dict()
    if x > 0:
        adjacent_heights[(x - 1, y)] = data[y][x - 1]
    if x < len(data[y]) - 1:
        adjacent_heights[(x + 1, y)] = data[y][x + 1]
    if y > 0:
        adjacent_heights[(x, y - 1)] = data[y - 1][x]
    if y < len(data) - 1:
        adjacent_heights[(x, y + 1)] = data[y + 1][x]
    return adjacent_heights


def get_lows(data):
    lows = dict()
    for y, line in enumerate(data):
        for x, height in enumerate(line):
            if height < min(get_adjacent_heights(data, (x, y)).values()):
                lows[(x, y)] = height
    return lows


def get_basin_sizes(data):
    basin_sizes = dict()
    for y, line in enumerate(data):
        for x, height in enumerate(line):
            if height == 9:
                continue
            destination = get_destination(data, (x, y))
            if destination not in basin_sizes:
                basin_sizes[destination] = 0
            basin_sizes[destination] += 1
    return basin_sizes


def get_destination(data, point):
    x, y = point
    adjacent_heights = get_adjacent_heights(data, point)
    lowest_adjacent_point = min(adjacent_heights.keys(), key=adjacent_heights.get)
    lowest_adjacent_height = adjacent_heights[lowest_adjacent_point]
    if data[y][x] <= lowest_adjacent_height:
        return point
    return get_destination(data, lowest_adjacent_point)


with open('day_09_input_1') as f:
    raw_data = f.readlines()
    data = [list(map(int, list(line.strip()))) for line in raw_data]

lows = get_lows(data)
risk = sum(lows.values()) + len(lows)
print(risk)

basin_sizes = get_basin_sizes(data)
largest_basins = sorted(basin_sizes.items(), key=lambda item: item[1], reverse=True)[:3]
product = 1
for point, size in largest_basins:
    product *= size
print(product)
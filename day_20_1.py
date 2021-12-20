# Solution for Advent of Code day 20
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


class Image:
    def __init__(self, data, algorithm):
        self._data = dict()
        for y, line in enumerate(data):
            for x, pixel in enumerate(line):
                if pixel == "#":
                    self._data[(x, y)] = 1
                else:
                    self._data[(x, y)] = 0
        self._algorithm = [0 if char == "." else 1 for char in algorithm]

    def __repr__(self):
        repr = ["".join(["#" if i == 1 else "." for i in self._algorithm]), ""]
        for y in self._get_y_coordinates():
            line = []
            for x in self._get_x_coordinates():
                item = self._data[(x, y)]
                if item == 0:
                    char = "."
                else:
                    char = "#"
                line.append(char)
            repr.append("".join(line))
        return "\n".join(repr)

    def _get_x_coordinates(self, offset=0):
        x = [x for (x, y), value in self._data.items() if value == 1]
        max_x = max(x) + offset
        min_x = min(x) - offset
        return range(min_x, max_x + 1)

    def _get_y_coordinates(self, offset=0):
        y = [y for (x, y), value in self._data.items() if value == 1]
        max_y = max(y) + offset
        min_y = min(y) - offset
        return range(min_y, max_y + 1)

    @staticmethod
    def _get_rectangle(point):
        for y_offset in range(-1, 2):
            for x_offset in range(-1, 2):
                x = point[0] + x_offset
                y = point[1] + y_offset
                yield x, y

    def improve(self, it):
        data = dict()
        if self._algorithm[0]:
            default = it % 2
        else:
            default = 0
        for y in self._get_y_coordinates(offset=9):
            for x in self._get_x_coordinates(offset=9):
                value = int("".join([str(self._data.get(point, default)) for point in self._get_rectangle((x, y))]), 2)
                new_value = self._algorithm[value]
                data[(x, y)] = new_value
        self._data = data

    def get_number_lit_pixels(self):
        return len([pixel for pixel in self._data.values() if pixel])


with open("day_20_input_1") as f:
    data = [line.strip() for line in f]
image = Image(data[2:], data[0])

for it in range(2):
    image.improve(it)
print(image.get_number_lit_pixels())
for it in range(48):
    image.improve(it)
print(image.get_number_lit_pixels())

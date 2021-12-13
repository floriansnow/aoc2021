# Solution for Advent of Code day 13
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

class Paper:
    def __init__(self):
        self._paper = dict()

    def get_dimensions(self):
        size_x = max([k[0] for k in self._paper.keys()]) + 1
        size_y = max([k[1] for k in self._paper.keys()]) + 1
        return size_x , size_y

    def _add_point(self, point):
        if point in self._paper:
            return
        self._paper[point] = "."

    def mark_point(self, point):
        self._add_point(point)
        self._paper[(point)] = "#"

    def fold(self, axis, number):
        size_x, size_y = self.get_dimensions()
        max_x, max_y = size_x - 1, size_y - 1
        new_paper = Paper()
        if axis == "y":
            for x, y in self._paper.keys():
                if y > number:
                    new_paper.mark_point((x, max_y - y))
                else:
                    new_paper.mark_point((x, y))
        else:
            for x, y in self._paper.keys():
                if x > number:
                    new_paper.mark_point((max_x - x, y))
                else:
                    new_paper.mark_point((x, y))
        self._paper = new_paper._paper

    def __repr__(self):
        out = []
        size_x, size_y = self.get_dimensions()
        for y in range(size_y):
            line = []
            for x in range(size_x):
                if (x, y) in self._paper:
                    symbol = self._paper[(x, y)]
                else:
                    symbol = "."
                line.append(symbol)
            out.append(line)

        return '\n'.join([''.join(line) for line in out])


with open("day_13_input_1") as f:
    raw_data = [line.strip() for line in f]

paper1 = Paper()
paper2 = Paper()
folds = []
for line in raw_data:
    if line == "":
        continue
    elif line.startswith('fold'):
       axis, number = line.split()[2].split("=")
       folds.append((axis, int(number)))
    else:
        point = tuple(map(int, line.split(",")))
        paper1.mark_point(point)
        paper2.mark_point(point)

paper1.fold(folds[0][0], folds[0][1])
print(len(paper1._paper))
for axis, number in folds:
    paper2.fold(axis, number)
print(paper2)

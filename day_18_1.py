# Solution for Advent of Code day 18
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

import ast


class List:
    def __init__(self, data):
        self._data = ast.literal_eval(data)

    def __add__(self, other):
        data = List(str([self._data, other._data]))
        while data.reduce(()):
            pass
        return data

    def __repr__(self):
        return str(self._data)

    def _explode_element(self, indices):
        data = self._get_data_at_indices(indices[:-1])
        index = indices[-1]
        self._add_to_next(indices, data[index][0], "left")
        # if index > 0 and type(data[index - 1]) == int:
        #     data[index - 1] += data[index][0]
        data = self._get_data_at_indices(indices[:-1])
        self._add_to_next(indices, data[index][1], "right")
        # if index < len(data) - 1 and type(data[index + 1]) == int:
        #     data[index + 1] += data[index][1]
        data = self._get_data_at_indices(indices[:-1])
        data[index] = 0

    def _split_element(self, indices):
        d = self._get_data_at_indices(indices[:-1])
        index = indices[-1]
        left = d[index] // 2
        right = left + d[index] % 2
        d[index] = [left, right]

    def _add_to_next(self, indices, num, direction):
        data = self._get_data_at_indices(indices[:-1])
        index = indices[-1]
        exploding_element = str(data[index])
        data[index] = "X"
        data = str(self._data)
        exploding_element_start = data.index("'")
        front, back = data[:exploding_element_start], data[exploding_element_start + 3:]
        in_num = False
        closest_num = None
        if direction == "left":
            search = front
        else:
            search = back
        for index, char in enumerate(search):
            if char.isnumeric() and not in_num:
                start_num = index
                closest_num = char
                in_num = True
            elif char.isnumeric() and in_num:
                closest_num += char
            elif not char.isnumeric() and in_num:
                end_num = index
                in_num = False
                if direction == "right":
                    break
        if closest_num:
            if direction == "left":
                data = front[:start_num] + str(int(closest_num) + num) + front[end_num:] + exploding_element + back
            else:
                data = front + exploding_element + back[:start_num] + str(int(closest_num) + num) + back[end_num:]
        else:
            data = front + exploding_element + back
        self._data = ast.literal_eval(data)

    def _get_data_at_indices(self, indices):
        data = self._data
        for index in indices:
            data = data[index]
        return data

    def _explode(self, indices):
        depth = len(indices) + 1
        data = self._get_data_at_indices(indices)
        for index, element in enumerate(data):
            if depth == 4 and type(element) == list:
                self._explode_element(indices + (index,))
                return True
            if type(element) == list:
                if self._explode(indices + (index,)):
                    return True
        return False

    def _split(self, indices):
        data = self._get_data_at_indices(indices)
        for index, element in enumerate(data):
            if type(element) == int and element >= 10:
                self._split_element(indices + (index,))
                return True
            if type(element) == list:
                if self._split(indices + (index,)):
                    return True
        return False

    def reduce(self, indices):
        while self._explode(indices):
            pass
        return self._split(indices)

    def _get_magnitude(self, element):
        if type(element) == int:
            return element
        return 3 * self._get_magnitude(element[0]) + 2 * self._get_magnitude(element[1])

    def get_total_magnitude(self):
        while type(self._data) == list:
            self._data = self._get_magnitude(self._data)
        return self._data


with open("day_18_input_1") as f:
    data = list(map(List, [line.strip() for line in f.readlines()]))

result = data[0]
for line in data[1:]:
    result += line

print(result.get_total_magnitude())
magnitudes = []
with open("day_18_input_1") as f:
    data = list(map(List, [line.strip() for line in f.readlines()]))

for index_a, line_a in enumerate(data):
    for index_b, line_b in enumerate(data):
        if index_a == index_b:
            continue
        magnitude = (line_a + line_b).get_total_magnitude()
        magnitudes.append(magnitude)
print(max(magnitudes))

# Solution for Advent of Code day 12
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

from collections import defaultdict


def count_paths(data, point, current_path, allow_twice):
    count = 0
    if ((point.islower() and not allow_twice and point in current_path) or
            (point == 'start' and point in current_path) or
            (point != 'start' and allow_twice and point.islower() and current_path.count(point) >= 2)):
        return 0
    current_path += (point,)
    if point.islower() and current_path.count(point) >= 2:
        allow_twice = False
    if point == 'end':
        return 1
    for next_point in data[point]:
        count += count_paths(data, next_point, current_path, allow_twice)
    return count


with open("day_12_input_1") as f:
    raw_data = [line.strip() for line in f]
data = defaultdict(list)
for line in raw_data:
    f, t = line.split("-")
    data[f].append(t)
    data[t].append(f)

count1 = count_paths(data, 'start', (), False)
print(count1)
count2 = count_paths(data, 'start', (), True)
print(count2)

# Solution for Advent of Code day 8
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

import itertools

def get_decoded_patterns(line):
    for a, b, c, d, e, f, g in itertools.permutations(['a', 'b', 'c', 'd', 'e', 'f', 'g']):
        irregular_patterns = {
            frozenset({a, b, c, e, f, g}): 0,
            frozenset({c, f}): 1,
            frozenset({a, c, d, e, g}): 2,
            frozenset({a, c, d, f, g}): 3,
            frozenset({b, c, d, f}): 4,
            frozenset({a, b, d, f, g}): 5,
            frozenset({a, b, d, e, f, g}): 6,
            frozenset({a, c, f}): 7,
            frozenset({a, b, c, d, e, f, g}): 8,
            frozenset({a, b, c, d, f, g}): 9
        }
        for pattern in line['signal_patterns']:
            if pattern not in irregular_patterns:
                break
        else:
            return irregular_patterns


with open("day_08_input_1") as f:
    raw_data = f.readlines()
    data = []
    for line in raw_data:
        signal_patterns, output_value = line.split('|')
        signal_patterns = list(map(frozenset, signal_patterns.split()))
        output_value = list(map(frozenset, output_value.split()))
        data.append({'signal_patterns': signal_patterns, 'output_value': output_value})

regular_patterns = {
    frozenset({'a', 'b', 'c', 'e', 'f', 'g'}): 0,
    frozenset({'c', 'f'}): 1,
    frozenset({'a', 'c', 'd', 'e', 'g'}): 2,
    frozenset({'a', 'c', 'd', 'f', 'g'}): 3,
    frozenset({'b', 'c', 'd', 'f'}): 4,
    frozenset({'a', 'b', 'd', 'f', 'g'}): 5,
    frozenset({'a', 'b', 'd', 'e', 'f', 'g'}): 6,
    frozenset({'a', 'c', 'f'}): 7,
    frozenset({'a', 'b', 'c', 'd', 'e', 'f', 'g'}): 8,
    frozenset({'a', 'b', 'c', 'd', 'f', 'g'}): 9
}

output_values = []
count = 0
sum = 0
for line in data:
    irregular_patterns = get_decoded_patterns(line)
    count += len([irregular_patterns[pattern] for pattern in line ['output_value'] if irregular_patterns[pattern] in (1, 4, 7, 8)])
    sum += int(''.join([str(irregular_patterns[pattern]) for pattern in line['output_value']]))

print(count, sum)

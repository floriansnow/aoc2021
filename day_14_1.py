# Solution for Advent of Code day 14
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


def parse_data(raw_data):
    polymer = []
    transformations = dict()
    for line in raw_data:
        if not line:
            continue
        elif "->" in line:
            parts = line.split()
            transformations[tuple(parts[0])] = parts[-1]
        else:
            polymer = list(line)
    return polymer, transformations

def get_pairs(polymer):
    pairs = defaultdict(int)
    for index, left in enumerate(polymer):
        if index == len(polymer) - 1:
            break
        right = polymer[index + 1]
        pairs[(left, right)] += 1
    return pairs

def transform(pairs, transformations, steps):
    for step in range(steps):
        new_pairs = defaultdict(int)
        for pair, count in pairs.items():
            if pair in transformations:
                new_pairs[(pair[0], transformations[pair])] += count
                new_pairs[(transformations[pair], pair[1])] += count
        pairs = new_pairs
    return new_pairs

def count_elements(pairs, polymer):
    count = defaultdict(int)
    for (left, right), c in pairs.items():
        count[left] += c
        count[right] += c
    count[polymer[0]] += 1
    count[polymer[-1]] += 1
    count = {key: value // 2 for key, value in count.items()}
    return count


with open("day_14_input_1") as f:
    raw_data = [line.strip() for line in f]

polymer, transformations = parse_data(raw_data)
pairs = get_pairs(polymer)

pairs1 = transform(pairs, transformations, 10)
count = count_elements(pairs1, polymer)
most_common = max(count.items(), key=lambda k: k[1])
least_common = min(count.items(), key=lambda k: k[1])
print(most_common[1] - least_common[1])

pairs2 = transform(pairs, transformations, 40)
count = count_elements(pairs2, polymer)
most_common = max(count.items(), key=lambda k: k[1])
least_common = min(count.items(), key=lambda k: k[1])
print(most_common[1] - least_common[1])

# Solution for Advent of Code day 10
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

def check(line):
    filo = []
    for char in line:
        if char in opening:
            filo.append(char)
        elif char in closing and filo and char == closing[opening.index(filo[-1])]:
            filo.pop()
        else:
            return char
    if filo:
        return filo


opening = ['[', '(', '<', '{']
closing = [']', ')', '>', '}']
with open("day_10_input_1") as f:
    data = [line.strip() for line in f.readlines()]

illegal_points = {
    ')': 3,
    ']': 57,
    '}': 1197,
    '>': 25137
}
completion_points = {
    ')': 1,
    ']': 2,
    '}': 3,
    '>': 4
}

illegal_score = 0
completion_scores = []
for line in data:
    completion_score = 0
    illegal = check(line)
    if isinstance(illegal, str):
        illegal_score += illegal_points[illegal]
    else:
        for char in reversed(illegal):
            closing_char = closing[opening.index(char)]
            completion_score = completion_score * 5 + completion_points[closing_char]
        completion_scores.append(completion_score)

print(illegal_score, sorted(completion_scores)[len(completion_scores) // 2])

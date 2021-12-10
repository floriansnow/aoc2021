# Solution for Advent of Code day 2, part 2
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

with open('day_02_input_1') as c:
    course = [(entry.strip().split()[0], int(entry.strip().split()[1])) for entry in c.readlines()]

position = 0
depth = 0
aim = 0
for entry in course:
    if entry[0] == 'forward':
        position += entry[1]
        depth += aim * entry[1]
    elif entry[0] == 'down':
        aim += entry[1]
    elif entry[0] == 'up':
        aim -= entry[1]
    else:
        print(entry)

print(position * depth)
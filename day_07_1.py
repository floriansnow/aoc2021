# Solution for Advent of Code day 7
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

with open('day_07_input_1') as f:
    crab_positions = [int(crab) for crab in f.readlines()[0].split(",")]

potential_positions1 = dict()
potential_positions2 = dict()
for potential_position in range(max(crab_positions) + 1):
    potential_positions1[potential_position] = 0
    potential_positions2[potential_position] = 0
    for crab_position in crab_positions:
        steps = abs(potential_position - crab_position)
        potential_positions1[potential_position] += steps
        potential_positions2[potential_position] += (steps * (steps + 1)) // 2

print(min(potential_positions1.values()), min(potential_positions2.values()))

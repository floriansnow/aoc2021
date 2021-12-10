# Solution for Advent of Code day 3, part 1
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

import numpy

with open('day_03_input_1') as f:
    data = [list(line.strip()) for line in f]

data = numpy.array(data, int)
data = numpy.rot90(data)[::-1].tolist()
#data = [''.join(map(str, line)) for line in data]

majority = (len(data[0]) // 2) + 1

gamma_rate = int(''.join(map(str, [sum(entry) // majority for entry in data])), 2)
epsilon_rate = int(bin((gamma_rate ^ (2 ** (len(data)+1) - 1)))[3:], 2)
print(gamma_rate * epsilon_rate)

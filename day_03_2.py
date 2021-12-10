# Solution for Advent of Code day 3, part 2
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
    rows = [list(map(int, list(line.strip()))) for line in f]

def rotate_data(data):
    data = numpy.array(data, int)
    return numpy.rot90(data)[::-1].tolist()

def get_most_common_value(num):
    return int(sum(num) >= len(num) - sum(num))

def get_least_common_value(num):
    return int(not (sum(num) >= len(num) - sum(num)))

def bin_list_to_int(l):
    return int(''.join(map(str, l)), 2)

oxygen_rows = rows.copy()
co2_rows = rows.copy()
for column_index in range(len(rows[0])):
    if len(oxygen_rows) > 1:
        oxygen_columns = rotate_data(oxygen_rows)
        oxygen_mcv = get_most_common_value(oxygen_columns[column_index])
        oxygen_rows = [row for row in oxygen_rows if row[column_index] == oxygen_mcv]
    if len(co2_rows) > 1:
        co2_columns = rotate_data(co2_rows)
        co2_lcv = get_least_common_value(co2_columns[column_index])
        co2_rows = [row for row in co2_rows if row[column_index] == co2_lcv]

print(bin_list_to_int(oxygen_rows[0]) * bin_list_to_int(co2_rows[0]))
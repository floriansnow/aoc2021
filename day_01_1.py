# Solution for Advent of Code day 1, part 1
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

with open('day_01_input_1') as d:
    depths = [int(depth.strip()) for depth in d.readlines()]

depth_increases = 0
prev_depth = None
for depth in depths:
    if not prev_depth:
        print(depth, '(N/A)', depth_increases)
    if prev_depth and prev_depth < depth:
        depth_increases += 1
        print(depth, '(increased)', depth_increases)
    elif prev_depth:
        print(depth, '[decreased]', depth_increases)
    prev_depth = depth

print(depth_increases)
# Solution for Advent of Code day 17
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

def reaches_target(start, target, trajectory):
    x, y = start
    min_x, max_x, min_y, max_y = target
    vx, vy = trajectory
    positions = [start]
    while x <= max_x and y >= min_y:
        x += vx
        y += vy
        positions.append((x, y))
        if vx > 0:
            vx -= 1
        vy -= 1
        if min_x <= x <= max_x and min_y <= y <= max_y:
            return True, positions
    return False, positions


def get_peaks(target):
    peaks = dict()
    min_x, max_x, min_y, max_y = target
    for tx in range(0, max_x + 1):
        max_abs_y = max(-126, 127)
        for ty in range(-max_abs_y, max_abs_y + 1):
            reaches, positions = reaches_target((0,0), target, (tx, ty))
            if reaches:
                peaks[(tx, ty)] = max([y for x, y in positions])
    return peaks


with open("day_17_input_1") as f:
    raw_data = f.read().strip()
    parts = [part.split("..") for part in raw_data.split()]
    min_x, max_x = int(parts[2][0][2:]), int(parts[2][1][:-1])
    min_y, max_y = int(parts[3][0][2:]), int(parts[3][1])

target = min_x, max_x, min_y, max_y
peaks = get_peaks(target)

peak_trajectory, peak = max(peaks.items(), key=lambda item: item[1])
print(peak, peak_trajectory)
print(len(peaks.keys()))

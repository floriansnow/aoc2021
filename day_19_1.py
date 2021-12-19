# Solution for Advent of Code day 19
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

class Scanner:
    def __init__(self, beacons):
        self.beacons = beacons
        self.position = (0, 0)
        self.scanners = ()

    def __repr__(self):
        return "Scanner(" + str(self.beacons) + ")"

    def __add__(self, other):
        if not self._overlaps(other):
            raise ValueError("Scanners do not overlap.")
        scanner = Scanner(self.beacons + tuple((beacon for beacon in other.beacons if beacon not in self.beacons)))
        scanner.scanners = self.scanners + tuple(
            (scanner for scanner in other.scanners if scanner not in self.scanners))
        if other.position not in scanner.scanners:
            scanner.scanners += (other.position,)
        return scanner

    def _shift(self, x_offset, y_offset, z_offset):
        self.beacons = tuple(((x + x_offset, y + y_offset, z + z_offset) for x, y, z in self.beacons))

    def _rotate(self, orientation):
        orientations = [((-1, -1, -1), (0, 2, 1)), ((-1, -1, -1), (1, 0, 2)), ((-1, -1, -1), (2, 1, 0)),
                        ((-1, -1, 1), (0, 1, 2)), ((-1, -1, 1), (1, 2, 0)), ((-1, -1, 1), (2, 0, 1)),
                        ((-1, 1, -1), (0, 1, 2)), ((-1, 1, -1), (1, 2, 0)), ((-1, 1, -1), (2, 0, 1)),
                        ((-1, 1, 1), (0, 2, 1)), ((-1, 1, 1), (1, 0, 2)), ((-1, 1, 1), (2, 1, 0)),
                        ((1, -1, -1), (0, 1, 2)), ((1, -1, -1), (1, 2, 0)), ((1, -1, -1), (2, 0, 1)),
                        ((1, -1, 1), (0, 2, 1)), ((1, -1, 1), (1, 0, 2)), ((1, -1, 1), (2, 1, 0)),
                        ((1, 1, -1), (0, 2, 1)), ((1, 1, -1), (1, 0, 2)), ((1, 1, -1), (2, 1, 0)),
                        ((1, 1, 1), (0, 1, 2)), ((1, 1, 1), (1, 2, 0)), ((1, 1, 1), (2, 0, 1))]
        (xf, yf, zf), (xi, yi, zi) = orientations[orientation]
        self.beacons = tuple(((xf * point[xi], yf * point[yi], zf * point[zi]) for point in self.beacons))

    def _overlaps(self, other):
        for orientation in range(24):
            original_rotation = other.beacons
            other._rotate(orientation)
            for index1 in range(len(self.beacons)):
                for index2 in range(len(other.beacons)):
                    beacon1 = self.beacons[index1]
                    beacon2 = other.beacons[index2]
                    if (beacon1, beacon2, orientation) in impossible_beacon_combinations:
                        continue
                    x_offset = beacon1[0] - beacon2[0]
                    y_offset = beacon1[1] - beacon2[1]
                    z_offset = beacon1[2] - beacon2[2]
                    original_shift = other.beacons
                    other._shift(x_offset, y_offset, z_offset)
                    overlap = len([beacon for beacon in self.beacons if beacon in other.beacons]) >= 12
                    if overlap:
                        other.position = (x_offset, y_offset, z_offset)
                        return True
                    impossible_beacon_combinations.add((beacon1, beacon2, orientation))
                    impossible_beacon_combinations.add((beacon2, beacon1, orientation))
                    other.beacons = original_shift
            other.beacons = original_rotation
        return False


def manhattan_distance(a, b):
    return sum(abs(value1 - value2) for value1, value2 in zip(a, b))


scanners = []
beacons = ()
with open("day_19_input_1") as f:
    for line in f:
        if beacons and "scanner" in line:
            scanners.append(Scanner(beacons))
            beacons = ()
        if line.strip() and "scanner" not in line:
            beacons += (tuple(map(int, line.strip().split(","))),)
    scanners.append(Scanner(beacons))

main_scanner = scanners[0]
used_scanners = [main_scanner]
impossible_beacon_combinations = set()
while len(used_scanners) < len(scanners):
    for scanner in scanners:
        if scanner in used_scanners:
            continue
        try:
            main_scanner += scanner
            used_scanners.append(scanner)
        except ValueError:
            continue

print(len(main_scanner.beacons))
distances = []
for scanner1 in main_scanner.scanners:
    for scanner2 in main_scanner.scanners:
        if scanner1 == scanner2:
            continue
        distances.append(manhattan_distance(scanner1, scanner2))
print(max(distances))

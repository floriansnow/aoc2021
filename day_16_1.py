# Solution for Advent of Code day 16
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

import operator


class Packet:
    def __init__(self, data):
        self._version = int(data[:3], 2)
        self._type = int(data[3:6], 2)
        self.value = None
        self.length = 6
        self._payload = data[6:]
        self._subpackets = []
        self._decode_payload()
        self.value = self._get_value()

    def _decode_payload(self):
        self._set_operand()
        if self._type == 4:
            self._decode_literal_value()
        else:
            self._decode_subpackets()

    def _decode_literal_value(self):
        payload = self._payload
        number = ""
        while True:
            self.length += 5
            number += payload[1:5]
            if payload[0] == "0":
                break
            payload = payload[5:]
        self.value = int(number, 2)

    def _set_operand(self):
        if self._type == 0:
            self._operand = operator.add
        elif self._type == 1:
            self._operand = operator.mul
        elif self._type == 2:
            self._operand = min
        elif self._type == 3:
            self._operand = max
        elif self._type == 4:
            self._operand = None
        elif self._type == 5:
            self._operand = operator.gt
        elif self._type == 6:
            self._operand = operator.lt
        elif self._type == 7:
            self._operand = operator.eq

    def _decode_subpackets(self):
        if self._payload[0] == "0":
            size_subpackets = int(self._payload[1:16], 2)
            self.length += 16 + size_subpackets
            subpackets = self._payload[16:size_subpackets + 16]
            while subpackets:
                self._subpackets.append(Packet(subpackets))
                subpackets = subpackets[self._subpackets[-1].length:]
        else:
            num_subpackets = int(self._payload[1:12], 2)
            subpackets = self._payload[12:]
            self.length += 12
            while len(self._subpackets) < num_subpackets:
                self._subpackets.append(Packet(subpackets))
                self.length += self._subpackets[-1].length
                subpackets = subpackets[self._subpackets[-1].length:]

    def get_version_sum(self):
        total = self._version
        for subpacket in self._subpackets:
            total += subpacket.get_version_sum()
        return total

    def _get_value(self):
        if self.value:
            return self.value
        sub_values = [packet.value for packet in self._subpackets]
        if len(sub_values) < 2:
            return sub_values[0]
        total = sub_values[0]
        for value in sub_values[1:]:
            total = self._operand(total, value)
        return total


with open("day_16_input_1") as f:
    raw_data = "".join([format(int(c, 16), "04b") for c in f.read().strip()])

data = Packet(raw_data)
print(data.get_version_sum())
print(data.value)

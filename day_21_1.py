# Solution for Advent of Code day 21
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

import itertools
from functools import cache


class Board:
    _spaces = 10

    def __init__(self, *args):
        if len(args) == 1:
            other = args[0]
            self._positions = other._positions.copy()
            self._points_to_win = other._points_to_win
            self._scores = other._scores.copy()
            self.active_player = other.active_player
        else:
            player_0_start, player_1_start, points_to_win = args
            self._positions = dict()
            self._positions[0] = player_0_start
            self._positions[1] = player_1_start
            self._points_to_win = points_to_win
            self._scores = dict()
            self._scores[0] = 0
            self._scores[1] = 0
            self.active_player = 0

    def move_player(self, player, steps):
        new_space = self._positions[player] + steps
        new_space %= 10
        if not new_space:
            new_space = 10
        self._scores[player] += new_space
        self._positions[player] = new_space
        self.active_player = not self.active_player

    def has_winner(self):
        return max(self._scores.values()) >= self._points_to_win

    def get_winner(self):
        if self._scores[0] >= self._points_to_win:
            return 0
        return 1

    def get_scores(self):
        if self._scores[0] >= self._points_to_win:
            return self._scores[0], self._scores[1]
        return self._scores[1], self._scores[0]


class Die:
    def __init__(self):
        self._next_roll = itertools.cycle(range(1, 101))
        self.rolls = 0

    def roll(self):
        self.rolls += 1
        for roll in self._next_roll:
            return roll


def play(player_1_start, player_2_start):
    board = Board(player_1_start, player_2_start, 1000)
    die = Die()
    while not board.has_winner():
        player = board.active_player
        roll = 0
        for _ in range(3):
            roll += die.roll()
        board.move_player(player, roll)
    winner, loser = board.get_scores()
    return loser * die.rolls


@cache
def play_quantum(position_player_0, position_player_1, score_player_0, score_player_1, active_player):
    wins = [0, 0]
    for rolls in itertools.product(range(1, 4), repeat=3):
        positions = [position_player_0, position_player_1]
        scores = [score_player_0, score_player_1]
        steps = sum(rolls)
        positions[active_player] = (positions[active_player] + steps) % 10
        if positions[active_player] == 0:
            positions[active_player] = 10
        scores[active_player] += positions[active_player]
        if scores[active_player] >= 21:
            wins[active_player] += 1
        else:
            deeper_wins = play_quantum(positions[0], positions[1], scores[0], scores[1], not active_player)
            wins[0] += deeper_wins[0]
            wins[1] += deeper_wins[1]
    return wins


with open("day_21_input_1") as f:
    raw_data = f.readlines()
player_0_start = int(raw_data[0].split(":")[-1])
player_1_start = int(raw_data[1].split(":")[-1])

print(play(player_0_start, player_1_start))
print(max(play_quantum(player_0_start, player_1_start, 0, 0, 0)))

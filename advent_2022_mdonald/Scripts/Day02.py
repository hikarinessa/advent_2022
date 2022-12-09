import os
import sys


INPUT_TXT = "../Input/Day02.txt"
TEST_INPUT = """A Y
B X
C Z"""

# BEATS = A beats Z, B beats X, C beats Y
BEATS = {
    "A": "Z",
    "B": "X",
    "C": "Y"
}
DRAWS = {
    "A": "X",
    "B": "Y",
    "C": "Z"
}
WIN_SCORE = 6
DRAW_SCORE = 3
PLAY_SCORES = {
    "A": 1,
    "B": 2,
    "C": 3,
    "X": 1,
    "Y": 2,
    "Z": 3
}


class Player():
    def __init__(self):
        self.score = 0


class Round():
    def __init__(self, plays: str, use_latest_rules=True):
        self.play1, _space, self.play2 = plays.partition(" ")
        if use_latest_rules:
            print("*"*92)
            print("* Result should be {}".format(self.play2))
            self._update_play2()
            print("* Player1 chose {}, Player2 chose {}".format(self.play1, self.play2))
        self.score1, self.score2 = self._resolve()

    def _resolve(self):
        score1 = PLAY_SCORES[self.play1]
        score2 = PLAY_SCORES[self.play2]
        # if player1 wins
        if self.play2 == BEATS[self.play1]:
            score1 += WIN_SCORE
        # if draw
        elif self.play2 == DRAWS[self.play1]:
            score1 += DRAW_SCORE
            score2 += DRAW_SCORE
        # player 2 wins
        else:
            score2 += WIN_SCORE
        return score1, score2

    def _update_play2(self):
        # if player2 should lose
        if self.play2 == "X":
            self.play2 = BEATS[self.play1]
        # if player2 should draw
        elif self.play2 == "Y":
            self.play2 = DRAWS[self.play1]
        # player 2 should win
        else:
            self.play2 = "XYZ".replace(BEATS[self.play1], "").replace(DRAWS[self.play1], "")


def get_input():
    with open(os.path.join(sys.path[0], INPUT_TXT), "r") as my_input:
        return my_input.read()


def parse_input(txt: str) -> list:
    rounds = [Round(r) for r in txt.splitlines()]
    return rounds


def do_magic(test=False):
    if test:
        rounds = parse_input(TEST_INPUT)
    else:
        rounds = parse_input(get_input())
    player1 = Player()
    player2 = Player()
    for r in rounds:
        player1.score += r.score1
        player2.score += r.score2
    print("*"*96)
    print("* My score is: {}".format(player2.score))


do_magic()

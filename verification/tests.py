"""
TESTS is a dict with all you tests.
Keys for this will be categories' names.
Each test is dict with
    "input" -- input data for user function
    "answer" -- your right answer
    "explanation" -- not necessary key, it's using for additional info in animation.
"""

from string import ascii_uppercase as au
from random import sample, randint, choice
from landing_site import landing_site
from itertools import chain


all_hexes = {c+str(r) for c in au[:12] for r in range(1, 10)}


def landing_site_make_random_tests(num):

    def adjacent_hexes(tgt_hex):
        c, r = au.index(tgt_hex[0]), int(tgt_hex[1])
        h1 = [au[c+cd] + str(r+rd) for cd in (1, -1) for rd in [-(1-c % 2), c % 2]]
        h2 = [au[c] + str(r+rd) for rd in (1, -1)]
        return set(map(lambda h: h if h in all_hexes else None, h1+h2))

    def make_island(start_hex):
        next_hexes = {start_hex}
        done_hexes = {start_hex}
        while next_hexes:
            for nx in set(next_hexes):
                adj_hexes = (adjacent_hexes(nx)-{None}) & rest_hexes
                next_hexes |= set(sample(adj_hexes, randint(0, min(3, len(adj_hexes)))))
            next_hexes -= done_hexes
            done_hexes |= next_hexes
        return done_hexes, set(chain(*[list(adjacent_hexes(dx)-{None}-done_hexes) for dx in done_hexes]))

    random_tests = []

    for _ in range(num):
        while True:
            rest_hexes = set(all_hexes)
            all_obstacles = set()
            for _ in range(randint(1, 10)):
                obstacles, adjacent = make_island(choice(list(rest_hexes)))
                all_obstacles |= obstacles
                rest_hexes -= obstacles | adjacent
                if not rest_hexes:
                    break
            answer, explanation = landing_site(all_obstacles)
            if len(answer) <= 4:
                random_tests.append({'input': list(all_obstacles),
                                     'answer': answer,
                                     'explanation': explanation})
                break

    return random_tests


TESTS = {
    "Basics": [
        {
            'input': ['E5', 'E7', 'F4', 'F6', 'G4', 'G6', 'H3', 'H5'],
            'answer': ['C3', 'J7'],
            'explanation': ['J5', 'A2', 'E2', 'K6', 'E4', 'A3', 'A4', 'B1',
                            'L8', 'J8', 'B3', 'K8', 'D3', 'C2', 'C5', 'H8',
                            'B4', 'I8', 'L6', 'I7', 'D4', 'J7', 'B2', 'H6',
                            'H7', 'D2', 'E3', 'C3', 'C4', 'J6', 'K7', 'J9',
                            'L7', 'I9', 'C1', 'D1', 'I6', 'K9'],
        },
        {
            'input': ['A4', 'C2', 'C6', 'C9', 'D4', 'D7', 'F1', 'F5',
                      'F8', 'G4', 'H7', 'I2', 'I5', 'I9', 'K3', 'K8', 'L5'],
            'answer': ['B7', 'E3', 'J6'],
            'explanation': ['J5', 'C8', 'B6', 'E2', 'K6', 'E4', 'C7', 'F3',
                            'B8', 'D3', 'F2', 'I7', 'J7', 'A8', 'A7', 'E3',
                            'D2', 'B7', 'J6', 'K7', 'I6'],
        },
        {
            'input': ['D3', 'D4', 'D5', 'D6', 'E3', 'E7', 'F2', 'F7', 'G2',
                      'G8', 'H2', 'H7', 'I3', 'I7', 'J3', 'J4', 'J5', 'J6'],
            'answer': ['G5'],
            'explanation': ['F6', 'G4', 'H4', 'I6', 'G5', 'E4', 'G7', 'F3',
                            'F4', 'I5', 'E6', 'E5', 'F5', 'H3', 'I4', 'H6',
                            'G3', 'H5', 'G6'],
        },
        {
            'input': [],
            'answer': ['E5', 'F5', 'G5', 'H5'],
            'explanation': ['B6', 'G5', 'G9', 'L5', 'C7', 'K8', 'F4', 'D3',
                            'K5', 'F8', 'C5', 'B4', 'I5', 'I7', 'D4', 'E6',
                            'I2', 'G8', 'C6', 'C3', 'I4', 'G1', 'H6', 'E1',
                            'L7', 'G3', 'F6', 'H4', 'H1', 'E4', 'A3', 'I3',
                            'J3', 'H8', 'D5', 'L4', 'F1', 'E3', 'D2', 'B7',
                            'E5', 'B5', 'F5', 'H3', 'G2', 'A6', 'E7', 'I6',
                            'L6', 'J5', 'C8', 'K6', 'A4', 'H9', 'D7', 'D8',
                            'F9', 'F2', 'C2', 'H2', 'I8', 'J7', 'B2', 'A7',
                            'E8', 'K4', 'L3', 'K7', 'J4', 'A5', 'I9', 'D1',
                            'H5', 'G4', 'E2', 'G7', 'J8', 'B3', 'D6', 'F3',
                            'K3', 'F7', 'J2', 'H7', 'J6', 'C4', 'E9', 'G6'],
        },
        {
            'input': list(all_hexes),
            'answer': [],
            'explanation': [],
        },
    ],
    "Randoms": landing_site_make_random_tests(10),
}

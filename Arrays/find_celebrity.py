import unittest
"""
You are given a party of N people. There may be one person in the party who does not know anyone but is
known by everyone. Such a person is called celebrity. Your task is to find this person.
You will be given a square matrix M, where M[i][j] is 1 means ith person knows jth person. You need to write
a function getId which returns the id of celebrity if present, else -1.
"""


def get_celebrity_id(M):

    first = 0
    last = len(M)-1

    while first < last:
        if M[first][last] == 1:
            first += 1
        else:
            last -= 1

    for i in range(len(M)):
        if i != first and (M[first][i] == 1 or M[i][first] == 0):
            return -1

    return first


class TestCelebrity(unittest.TestCase):

    def test_celebrity(self):
        M = [[0, 0, 1, 0], [0, 0, 1, 0], [0, 0, 0, 0], [0, 0, 1, 0]]
        self.assertEqual(get_celebrity_id(M), 2)

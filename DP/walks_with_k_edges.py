import unittest
"""
Given a directed graph and two vertices 'u' and 'v' in it, count all possible walks
from 'u' to 'v' with exactly k edges.
Graph is given in adjacency matrix notation where G[i][j] is True if there is an edge from i to j
else False.
"""

"""
Approach:
Optimal substructure:
num_walks = 0
for w in G.V such that edge(w,v):
    num_walks += get_walks(G, u, w, k-1)
Base case:
if u == v and k == 0: return 1
elif k == 1 and edge(u,v): return 1
elif k <= 0: return 0
"""


def get_k_walks(G, u, v, k):
    V = len(G)
    # table[i][j][e] denotes number of walks from i to j of length e
    # table[u][v][k] stores the final result
    table = [[[0] * (k+1) for _ in range(V)] for _ in range(V)]

    for e in range(k+1):
        for i in range(V):
            for j in range(V):
                if i == j and e == 0:
                    table[i][j][e] = 1
                elif G[i][j] == 1 and e == 1:
                    table[i][j][e] = 1
                elif e > 1:
                    for a in range(V):
                        if G[i][a] == 1:
                            table[i][j][e] += table[a][j][e-1]

    return table[u][v][k]


class TestGetKWalks(unittest.TestCase):

    def test_get_k_walks(self):
        G = [[0, 1, 1, 1],
             [0, 0, 0, 1],
             [0, 0, 0, 1],
             [0, 0, 0, 0]]
        u = 0
        v = 3
        k = 2

        self.assertEqual(get_k_walks(G, u, v, k), 2)

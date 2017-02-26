import unittest
"""
Given a graph which represents a flow network where every edge has a capacity. Also, given two
vertices, source 's' and sink 't' in the graph, find the maximum possible flow from 's' to 't'
with following constraints:
1. Flow on edge does not exceed the maximum capacity on edge.
2. Incoming flow is equal to outgoing flow for every vertex except s and t.
"""

"""
Approach:
Ford-Fulkerson Algorithm implemented using Edmonds-Karp
"""


def path_exists(residual_graph, s, t, parent):
    V = len(residual_graph)
    visited = [False] * V
    queue = []

    visited[s] = True
    queue.insert(0, s)

    while len(queue) > 0:
        u = queue.pop(0)
        for v in range(V):
            if not visited[v] and residual_graph[u][v] > 0:
                visited[v] = True
                parent[v] = u
                queue.append(v)

    return visited[t]


def max_flow(G, s, t):
    V = len(G)
    parent = [-1] * V
    result = 0
    residual_graph = [[0] * V for _ in range(V)]

    # Create Residual graph
    for i in range(V):
        for j in range(V):
            residual_graph[i][j] = G[i][j]

    while path_exists(residual_graph, s, t, parent):
        path_flow = float('inf')
        v = t
        while v != s:
            u = parent[v]
            path_flow = min(path_flow, residual_graph[u][v])
            v = u
        v = t
        while v != s:
            u = parent[v]
            residual_graph[u][v] -= path_flow
            residual_graph[v][u] += path_flow
            v = u
        result += path_flow

    return result


class TestMaxFlow(unittest.TestCase):

    def test_max_flow(self):
        G = [[0, 16, 13, 0, 0, 0],
             [0, 0, 10, 12, 0, 0],
             [0, 4, 0, 0, 14, 0],
             [0, 0, 9, 0, 0, 20],
             [0, 0, 0, 7, 0, 4],
             [0, 0, 0, 0, 0, 0]
             ]
        self.assertEqual(max_flow(G, 0, 5), 23)

import unittest
"""
Given an undirected graph and a number m, determine if the graph can be colored with at most m colors
such that no two adjacent vertices of the graph are colored with same color. Here coloring of a graph
means assignment of colors to all vertices.
Input:
a) A 2D array graph[V][V] where V is number of vertices in the graph. If graph[i][j] is 1, there is direct
edge from vertex i to j, otherwise graph[i][j] is 0.
b) An integer m which is maximum number of colors that can be used.
Output:
An array color[V] that should have numbers from 1 to m. color[i] should represent the color assigned
to the ith vertex. The code should return false if the graph cannot be colored using m colors.
"""

"""
Approach:
The idea is to start with vertex 1 and assign it a color. Then assign colors to subsequent vertices which
results in a "safe" assignment, ie, the color is not already assigned to any of its adjacent vertices. Backtrack
and try a new color in case none of the assignments is safe.
"""


def is_safe(graph, vertex_to_check, color, assigned):
    V = len(graph)
    for vertex in range(V):
        if vertex != vertex_to_check and graph[vertex][vertex_to_check] == 1:
            if assigned == color[vertex]:
                return False

    return True


def graph_coloring_helper(graph, color, vertex, m):
    if vertex == len(graph):
        return True
    for c in range(1, m+1):
        if is_safe(graph, vertex, color, c):
            color[vertex] = c
            if graph_coloring_helper(graph, color, vertex+1, m):
                return True
            color[vertex] = 0

    return False


def graph_coloring(graph, m):
    V = len(graph)
    color = [0] * V
    if graph_coloring_helper(graph, color, 0, m):
        return color
    return False


class TestGraphColoring(unittest.TestCase):

    def test_graph_coloring(self):
        #     Create
        #     following
        #     graph and test
        #     whether
        #     it is 3
        #     colorable
        #     (3)---(2)
        #     |    / |
        #     |   /  |
        #     |  /   |
        #     (0) --(1)

        graph = [[0, 1, 1, 1], [1, 0, 1, 0], [1, 1, 0, 1], [1, 0, 1, 0]]
        m = 3
        self.assertEqual(graph_coloring(graph, m), [1, 2, 3, 2])

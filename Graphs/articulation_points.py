import unittest
"""
A vertex in an undirected connected graph is an articulation point iff removing it (and the edges through it)
disconnects the graph. Articulation points represent vulnerabilities in a connected network.
A naive approach to find articulation points would be to one by one remove each vertex, and see if the graph is still
connected. If graph becomes disconnected after removing v, then v is an articulation point. The time complexity of
this algorithm is O(V*(V+E)). There is a linear time algorithm to find articulation points in a graph.
It maintains following values:
1. entry_time[v] = The time at which vertex v is discovered during DFS. Indicates the age of a node in DFS tree.
2. reachable_ancestor_time[v] = The time at which the earliest reachable ancestor (oldest ancestor) of v is
   discovered during DFS.
Following two types of articulation points can exist in the DFS tree of a graph:
1. If node v is root of DFS tree and if it has more than 1 children, then v is an articulation point.
2. For each child of v, if there is no back edge from any node in the subtree rooted at the child, to an ancestor
   of v, the v is an articulation point.
Explanation:
For the first point, removing a root with 2 or more children, will make the children disconnected. Hence such a root
is articulation point.
For the second point, think of back edges like backup security wires, so that even if the main line is damaged,
we can always go back using back edges to earlier nodes. Hence, graph remains connected. The absence of such
back edges means that if we remove v, then there is no way of coming back to an ancestor of v, from v's descendants.
Hence, v is an articulation point.
"""


def articulation_points_helper(G, u, ap, parent, visited, entry_time, reachable_ancestor_time):

    children = 0
    articulation_points_helper.time += 1
    entry_time[u] = articulation_points_helper.time
    reachable_ancestor_time[u] = articulation_points_helper.time
    visited[u] = True
    V = len(G)

    for v in range(V):
        if G[u][v] == 1:
            if not visited[v]:
                # u-v is a tree edge in DFS tree, so increment children count by 1.
                children += 1
                parent[v] = u
                articulation_points_helper(G, v, ap, parent, visited, entry_time, reachable_ancestor_time)
                reachable_ancestor_time[u] = min(reachable_ancestor_time[u], reachable_ancestor_time[v])
                # check for condition 1
                if parent[u] == -1 and children > 1:
                    ap[u] = True

                # check for condition 2
                if parent[u] != -1 and reachable_ancestor_time[v] >= entry_time[u]:
                    ap[u] = True
            elif parent[u] != v:
                # u-v is a back edge in DFS tree, so update the earliest ancestor of u.
                reachable_ancestor_time[u] = min(reachable_ancestor_time[u], entry_time[v])


def articulation_points(G):
    V = len(G)
    visited = [False] * V
    parent = [-1] * V
    entry_time = [0] * V
    reachable_ancestor_time = [0] * V
    ap = [False] * V
    articulation_points_helper.time = 0

    for u in range(V):
        if not visited[u]:
            articulation_points_helper(G, u, ap, parent, visited, entry_time, reachable_ancestor_time)

    return ap


class TestArticulation(unittest.TestCase):

    def test_articulation(self):
        G = [[0, 1, 1, 1, 0], [1, 0, 1, 0, 0], [1, 1, 0, 0, 0], [1, 0, 0, 0, 1], [0, 0, 0, 1, 0]]
        result = articulation_points(G)
        result = [i for i in range(len(result)) if result[i] is True]
        self.assertItemsEqual(result, [0, 3])
        G = [[0, 1, 0, 0], [1, 0, 1, 0], [0, 1, 0, 1], [0, 0, 1, 0]]
        result = articulation_points(G)
        result = [i for i in range(len(result)) if result[i] is True]
        self.assertItemsEqual(result, [1, 2])
        G = [[0, 1], [1, 0]]
        self.assertEqual(articulation_points(G), [False, False])

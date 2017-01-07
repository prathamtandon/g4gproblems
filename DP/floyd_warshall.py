"""
Floyd Warshall is used to compute All Pairs Shortest Paths in a given edge weighted directed graph.
For given solution, input Graph is represented in adjacency matrix format. If i == j, then graph[i][j] = 0.
If vertex i is not reachable from vertex j, then graph[i][j] = float('inf').
"""

"""
Approach:
The idea is to consider every vertex in the graph as a potential intermediate vertex
in shortest path between a source and destination vertex. Let (i,j) be a source destination pair.
If vertex k is not part of shortest path between i and j, then we do not change dist[i][j].
However, if vertex k is part of shortest path between i and j, then we update dist[i][j] as
dist[i][k] + dist[k][j]. Also, when vertex k is considered as intermediate vertex, it means all vertices
0,1,...,k-1 have already been considered as intermediate vertex before.
"""


def floyd_warshall(graph):
    V = len(graph)
    dist = [[0] * V for _ in range(V)]

    for i in range(V):
        for j in range(V):
            dist[i][j] = graph[i][j]

    for k in range(V):
        for start in range(V):
            for end in range(V):
                if dist[start][end] > dist[start][k] + dist[k][end]:
                    dist[start][end] = dist[start][k] + dist[k][end]

    return dist

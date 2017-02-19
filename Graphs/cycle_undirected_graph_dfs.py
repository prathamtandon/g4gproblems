"""
Find whether a given undirected graph has a cycle. NOTE: Another way to do this is using Union-Find algorithm.
"""

"""
Approach:
1. The idea is to perform a DFS starting from every vertex.
2. Along with standard DFS stuff, we also pass the parent node which started the DFS.
    Example, If we are doing DFS at u, and we start exploring an unvisited neighbor of u say v, then we pass
    parent as u for DFS from v.
3. During DFS, if we find a visited node, then we compare it with parent. If the visited node and parent are same,
    it means we just came from parent (in above example, that would be the case when u is parent, and since
    graph is undirected, u will again appear as neighbour of v during DFS from v), so we just skip the node.
4. However, if we find visited node, not equal to current parent, it means we will be exploring an already
    visited node using the current edge. Hence, there is a cycle.
"""


def has_cycle_helper(G, v, parent, visited):
    visited[v] = True
    V = len(G)
    for u in range(V):
        if G[v][u] == 1:
            if not visited[u]:
                return has_cycle_helper(G, u, v, visited)
            elif parent != u:
                return True
    return False


def has_cycle(G):
    V = len(G)
    visited = [False] * V
    for v in range(V):
        if has_cycle_helper(G, v, v, visited):
            return True
    return False

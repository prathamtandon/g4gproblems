"""
Given a DAG, print all topological orderings of the DAG.
"""


"""
Approach:
1. Compute indegree of each vertex in the graph.
2. Go through all vertices.
3. Find a vertex with indegree == 0 and visited == False
4. Mark the vertex as visited == True and add it to result.
5. Decrease indegree of all its adjacent vertices by 1.
6. Call the function again and then backtrack ie reset indegrees of neighbours, mark visited = False
    and remove from result.
"""


def all_topological_order(graph, visited, order, indegree):
    done = True

    # NOTE: VISIT ALL VERTICES IN EVERY RECURSIVE CALL!
    for u in graph.V:
        if indegree[u] == 0 and not visited[u]:
            done = False

            for v in graph.adj_list[u]:
                indegree[v] -= 1

            visited[u] = True
            order.append(u)

            all_topological_order(graph, visited, order, indegree)

            # BACKTRACK
            for v in graph.adj_list[u]:
                indegree[v] += 1

            visited[u] = False
            order.pop()

    # If all visited and all indegree == 0, print result
    if done:
        print order

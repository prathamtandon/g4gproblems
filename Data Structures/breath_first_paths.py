class BreadthFirstPaths:

    def __init__(self, G, s):
        self.marked = [False] * G.V()
        self.s = s
        self.edge_to = [0] * G.V()
        self.bfs(G)

    def bfs(self, G):
        self.marked[self.s] = True
        queue = [self.s]
        self.edge_to[self.s] = self.s
        while len(queue) > 0:
            v = queue.pop(0)
            for w in G.adj(v):
                if not self.marked[w]:
                    self.marked[w] = True
                    self.edge_to[w] = v
                    queue.append(w)

    def marked(self, v):
        return self.marked[v]

    def path_to(self, v):
        x = self.edge_to[v]
        path = [v]
        while x != self.s:
            path.insert(0, x)
            x = self.edge_to[x]
        return path

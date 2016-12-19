class DepthFirstSearch:

    def __init__(self, G, s):
        self.marked = [False] * G.V()
        self.count = 0
        self.dfs(G, s)

    def dfs(self, G, v):
        self.marked[v] = True
        self.count += 1
        for w in G.adj(v):
            if not self.marked[w]:
                self.dfs(G, w)

    def marked(self, v):
        return self.marked[v]

    def count(self):
        return self.count

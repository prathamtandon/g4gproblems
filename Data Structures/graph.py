"""
This Graph implementation maintains a vertex-indexed array of lists of integers. Every edge appears
twice: if the edge connects v and w, then w appears in v's list and v appears in w's list. The second constructor
reads a graph from an input stream, in the format V followed by E followed by a list of pairs of int values between
0 and V-1.
"""


class Graph:

    def __init__(self):
        self.V = 0
        self.E = 0
        self.adj = None

    def read_from_file(self, filename):
        with open(filename) as f:
            self.V = int(f.readline())
            self.adj = [[] for x in xrange(self.V)]
            E = int(f.readline())
            for i in xrange(E):
                next_edge = f.readline().split()
                v = next_edge[0]
                w = next_edge[1]
                self.add_edge(int(v), int(w))

    def V(self):
        return self.V

    def E(self):
        return self.E

    def adj(self, v):
        return self.adj[v]

    def add_edge(self, v, w):
        self.adj[v].append(w)
        self.adj[w].append(v)
        self.E += 1

    def degree(self, v):
        return len(self.adj[v])

    def max_degree(self):
        return max([len(v) for v in xrange(self.V)])

    def avg_degree(self):
        return 2 * self.E / self.V

    def __repr__(self):
        s = str(self.V) + ' vertices, ' + str(self.E) + ' edges\n'
        for v in xrange(self.V):
            s += str(v) + ': '
            for w in self.adj[v]:
                s += str(w) + ' '
            s += '\n'
        return s


if __name__ == '__main__':
    graph = Graph()
    graph.read_from_file('tinyG.txt')
    print graph

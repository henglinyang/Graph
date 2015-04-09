class Graph(object):
    '''A node list graph implementation
    '''
    def __init__(self, name='anonymous', undirected=True):
        self._name = name
        self._undirected = undirected
        self._nodes = {}
        self._edges = {}
        self._adjacency = {}

    def __repr__(self):
        return '{d} graph: {n}({v} nodes, {e} edges)'.format(d='Undirected' if self.undirected else 'Directed', n=self.name, v=len(self.nodes), e=len(self.edges))

    @property
    def undirected(self):
        return self._undirected

    @property
    def name(self):
        return self._name

    @property
    def nodes(self):
        return self._nodes

    @property
    def edges(self):
        return self._edges

    def add_node(self, v):
        if v not in self.nodes:
            self.nodes[v] = set()

    def add_edge(self, v1, v2, cost=1):
        self.add_node(v1)
        self.add_node(v2)
        self.nodes[v1].add(v2)
        if self.undirected:
            self.nodes[v2].add(v1)
            if v1 > v2:
                v1, v2 = v2, v1
        self.edges[(v1, v2)] = cost

    def edge_cost(self, v1, v2):
        if self.undirected and v1 > v2:
            v1, v2 = v2, v1
        try:
            return self.edges[(v1, v2)]
        except KeyError:
            return None
        

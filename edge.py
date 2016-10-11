class Edge(object):
    """
    Generic class to represent edges of a graph
    """

    __edge_count = -1  # global counter shared across all Edge instances

    def __init__(self, __node_a='empty', __node_b='empty', edge_weight='empty'):
        self.__node_a = __node_a    #an instance of node.py
        self.__node_b = __node_b    #an instance of node.py
        self.__edge_weight = edge_weight
        Edge.__edge_count += 1
        self.__id = Edge.__edge_count

    def get_name(self):
        "@:return name of graph"
        return self.__name

    def get_id(self):
        "@:return id of the graph"
        return self.__id

    def get_node_a(self):
        "@:return node_a of the graph"
        return self.__node_a

    def get_node_b(self):
        "@:return node_b of the graph"
        return self.__node_b

    def get_edge_weight(self):
        "@:return weight/cost of the edge"
        return self.__edge_weight

    def __lt__(self, other):
        return self.__edge_weight < other.get_edge_weight()

    def __repr__(self):
        id = self.get_id()
        node_a = self.get_node_a()
        node_b = self.get_node_b()
        edge_weight = self.get_edge_weight()
        s = 'Edge %d [node_a: %d, node_b: %d, weight: %d]' % (id, node_a.get_id(), node_b.get_id(), edge_weight)
        return s

if __name__ == 'main':
    edges = []
    for k in range(5):
        edges.append(Edge())

    for edge in edges:
        print edge

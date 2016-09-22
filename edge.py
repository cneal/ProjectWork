class Edge(object):
    """
    Generic class to represent edges of a graph
    """

    __edge_count = -1  # global counter shared across all Edge instances

    def __init__(self, from_node='empty', to_node='empty', edge_weight='empty'):
        self.__from_node = from_node
        self.__to_node = to_node
        self.__edge_weight = edge_weight
        Edge.__edge_count += 1
        self.__id = Edge.__edge_count

    def get_name(self):
        "@:return name of graph"
        return self.__name

    def get_id(self):
        "@:return id of the graph"
        return self.__id

    def get_from_node(self):
        "@:return from node of the graph"
        return self.__from_node

    def get_to_node(self):
        "@:return to node of the graph"
        return self.__to_node

    def get_edge_weight(self):
        "@:return weight/cost of the edge"
        return self.__edge_weight

    def __repr__(self):
        id = self.get_id()
        from_node = self.get_from_node()
        to_node = self.get_to_node()
        edge_weight = self.get_edge_weight()
        s = 'Edge %d [from: %d, to: %d, weight: %d]' % (id, from_node, to_node, edge_weight)
        return s

if __name__ == 'main':
    edges = []
    for k in range(5):
        edges.append(Edge())

    for edge in edges:
        print edge

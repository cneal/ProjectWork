class Graph(object):
    """
    Une classe generique pour representer un graphe comme un ensemble de
    noeuds.
    """

    def __init__(self, name='Sans nom'):
        self.__name = name
        self.__nodes = []       #Private. Array of nodes
        self.__num_nodes = 0    #Private. Size of graph
        self.__edges = []
        self.__num_edges = 0
        self.__adjacency_matrix = [] #initialize an empty adjacency matrix

    def add_node(self, node):
        "Ajoute un noeud au graphe."
        self.__nodes.append(node)
        self.__num_nodes += 1

    def add_edge(self, edge):
        """
        Add an edge to the graph.
        -An Edge instance is appended to the list self.__edges[]
        -The edge weight is put into the adjacency matrix
        """

        if len(self.__adjacency_matrix) == 0:
            self.__initialize_adjacency_matrix() #create an empty adjacency matrix if it doesnt exist yet

        self.__adjacency_matrix[edge.get_from_node()][edge.get_to_node()] = edge.get_edge_weight()

        self.__edges.append(edge)
        self.__num_edges += 1

    def __initialize_adjacency_matrix(self):
        """
        Initializes an empty adjacency matrix. Note it does not return anything.
        It has the dimension (num_nodes) * (num_nodes) and all values are 0 (zero)
        A value of 0 implies that there is no link between nodes.
        """
        for dimension in range(1, self.__num_nodes+1):
            self.__adjacency_matrix.append([0] * self.__num_nodes)

    def get_adjacency_matrix(self):
        """
        :return:  self.__adjacency_matrix
        """
        return self.__adjacency_matrix

    def get_name(self):
        "Donne le nom du graphe."
        return self.__name

    def get_nodes(self):
        "Donne la liste des noeuds du graphe."
        return self.__nodes

    def get_nb_nodes(self):
        "Donne le nombre de noeuds du graphe."
        return len(self.__nodes)

    def get_num_nodes(self):
        "Return the number of nodes in the graph"
        return self.__num_nodes

    def __repr__(self):
        name = self.get_name()
        nb_nodes = self.get_num_nodes()
        s = 'Graph %s has %d nodes' % (name, nb_nodes)
        for node in self.get_nodes():
            s += '\n  ' + repr(node)
        return s


if __name__ == '__main__':

    from node import Node

    G = Graph(name='Graphe test')
    for k in range(5):
        G.add_node(Node(name='Noeud test %d' % k))

    print G

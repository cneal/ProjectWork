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
        self.__adjacency_matrix_dictionary = [] #initialize an empty adjacency matrix using a dictionary os distionary

    def __init__(self, readInstance={}):
        """
        It builds an Graph object from an given instance. The instance is encapsulated in a Dictionary data structure
        @:param readInstance: a dictionary containing information about the TSP problem
        """
        if not readInstance.keys():
            print "Instance's dictionary not provided. Please provide a dictionary that contains instance's information."
            return

        import node
        import edge

        self.__name = readInstance["header"]["NAME"] #name of the graph
        self.__nodes = []       #Array of nodes
        self.__num_nodes = 0    #Number of nodes
        self.__edges = []       #Array of edges
        self.__num_edges = 0    #Number of edges
        self.__adjacency_matrix = []            #initialize an empty adjacency matrix
        self.__adjacency_matrix_dictionary = {} #initialize an empty double dictionary adjacency object

        #add nodes to the graph
        for curNodeVal in xrange(0, readInstance["header"]["DIMENSION"]):
            newNode = node.Node(curNodeVal, readInstance["nodes"][curNodeVal])  # create a new node instance
            self.add_node(newNode)  # add node to the graph

        # add edges to graph
        for tupleEdge in readInstance["edges"]:
            fromNodeId = tupleEdge[0]
            toNodeId = tupleEdge[1]
            edgeWeight = tupleEdge[2]
            if edgeWeight > 0:
                newEdge1 = edge.Edge(fromNodeId, toNodeId, edgeWeight) #create edge in original direction
                self.add_edge(newEdge1)
                newEdge2 = edge.Edge(toNodeId, fromNodeId, edgeWeight)  #create edges in the other direction
                self.add_edge(newEdge2)

    def add_node(self, node):
        "Add node to the graph"
        self.__nodes.append(node)
        self.__num_nodes += 1

    def add_edge(self, edge):
        """
        Add an edge to the graph.
        """

        if len(self.__adjacency_matrix) == 0:
            self.__initialize_adjacency_matrices()  #create an empty_adjacency_matrix & adjacency_matrix_dictionary if they doesnt exist yet

        self.__adjacency_matrix[edge.get_from_node()][edge.get_to_node()] = edge.get_edge_weight()
        self.__adjacency_matrix_dictionary[self.__nodes[edge.get_from_node()]][self.__nodes[edge.get_to_node()]] = edge

        self.__edges.append(edge)
        self.__num_edges += 1

    def __initialize_adjacency_matrices(self):
        """
        Initializes the adjacency_matrix (a value of 0 implies no link between nodes) and the adjacency_matrix_dictionary
        """
        for dimension in range(1, self.__num_nodes+1):
            self.__adjacency_matrix.append([0] * self.__num_nodes) #size of matrix is (num_nodes) * (num_nodes)

        for i in range(0, self.__num_nodes):
            self.__adjacency_matrix_dictionary[self.__nodes[i]] = {} #add empty dictionary elements for each node

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

    def get_edges(self):
        """:return:  self.__edges"""
        return self.__edges

    def __repr__(self):
        name = self.get_name()
        nb_nodes = self.get_num_nodes()
        s = 'Graph %s has %d nodes' % (name, nb_nodes)
        for node in self.get_nodes():
            s += '\n  ' + repr(node)

        # Prints the all the nodes with related edges
        s += '\n\nGraph %s has %d edges' %(name, self.__num_edges)
        for i in xrange(0, self.__num_nodes):
            neighbors = self.__adjacency_matrix_dictionary[self.__nodes[i]]
            s += "\nNode %d:\n" % i
            for nodeTo, edge in neighbors.iteritems():
                s += "   %r\n" % edge

        # Prints out the adjacency matrix
        s += "\n\nAdjacency Matrix:\n"
        for i in xrange(0, self.__num_nodes):
            s += str(i) + ": "
            for j in xrange(0, self.__num_nodes):
                s += " " + str(self.__adjacency_matrix[i][j])
            s += "\n"

        return s


if __name__ == '__main__':

    from node import Node

    G = Graph(name='Graphe test')
    for k in range(5):
        G.add_node(Node(name='Noeud test %d' % k))

    print G

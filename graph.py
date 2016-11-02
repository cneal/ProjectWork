import numpy as np


class Graph(object):
    """
    Une classe generique pour representer un graphe comme un ensemble de
    noeuds.
    """

    def __init__(self, name='Sans nom'):
        self.__name = name
        self.__nodes = []  # Private. Array of nodes
        self.__num_nodes = 0  # Private. Size of graph
        self.__edges = []
        self.__num_edges = 0
        self.__adjacency_matrix = []  # initialize an empty adjacency matrix
        self.__adjacency_matrix_dictionary = {}  # initialize an empty adjacency matrix using a dictionary os distionary

    def build_from_instance(self, instanceDict={}):
        """
        It builds an Graph object from an given instance. The instance is encapsulated in a Dictionary data structure
        @:param instanceDict: a dictionary containing information about the TSP problem
        """
        if not instanceDict.keys():
            print "Instance's dictionary not provided. Please provide a dictionary that contains instance's information."
            return

        from node import Node
        from edge import Edge

        self.__instance_dictionary = instanceDict
        self.__name = instanceDict["header"]["NAME"]  # name of the graph
        self.__nodes = []  # Array of nodes
        self.__num_nodes = 0  # Number of nodes
        self.__edges = []  # Array of edges
        self.__num_edges = 0  # Number of edges
        self.__adjacency_matrix = []  # initialize an empty adjacency matrix
        self.__adjacency_matrix_dictionary = {}  # initialize an empty double dictionary adjacency object

        # add nodes to the graph
        for curNodeVal in xrange(0, instanceDict["header"]["DIMENSION"]):
            new_node = Node(curNodeVal, instanceDict["nodes"][curNodeVal])  # create a new node instance
            self.add_node(new_node)  # add node to the graph

        # add edges to graph
        for tupleEdge in instanceDict["edges"]:
            node_a_id = tupleEdge[0]
            node_b_id = tupleEdge[1]
            edge_weight = tupleEdge[2]

            #if edge_weight > 0:
            if node_a_id != node_b_id:
                new_edge = Edge(self.__nodes[node_a_id], self.__nodes[node_b_id], edge_weight)  # create edge
                self.add_edge(new_edge)

    def add_node(self, node):
        "Add node to the graph"
        self.__nodes.append(node)
        self.__num_nodes += 1

    def add_edge(self, edge):
        """
        Add an edge to the graph.
        """

        if len(self.__adjacency_matrix) == 0:  # create an empty_adjacency_matrix & adjacency_matrix_dictionary if they doesnt exist yet
            for dimension in range(1, self.__num_nodes + 1):
                self.__adjacency_matrix.append([0] * self.__num_nodes)  # size of matrix is (num_nodes) * (num_nodes)
            for i in range(0, self.__num_nodes):
                self.__adjacency_matrix_dictionary[self.__nodes[i]] = {}  # add empty dictionary elements for each node

        self.__adjacency_matrix_dictionary[self.__nodes[edge.get_node_a().get_id()]][
            self.__nodes[edge.get_node_b().get_id()]] = edge
        self.__adjacency_matrix_dictionary[self.__nodes[edge.get_node_b().get_id()]][
            self.__nodes[edge.get_node_a().get_id()]] = edge  # add edge to both directions

        self.__edges.append(edge)
        self.__num_edges += 1

    def get_adjacency_matrix(self):
        """
        :return:  self.__adjacency_matrix
        """
        return self.__adjacency_matrix

    def get_adjacency_matrix_dictionary(self):
        return self.__adjacency_matrix_dictionary

    def get_name(self):
        "Donne le nom du graphe."
        return self.__name

    def get_nodes(self):
        "Donne la liste des noeuds du graphe."
        return self.__nodes

    def get_num_nodes(self):
        "Return the number of nodes in the graph"
        return self.__num_nodes

    def get_edges(self):
        """:return:  self.__edges"""
        return self.__edges

    def get_graph_weight(self):
        """
        :return: int - the weight of the graph
        """
        weight = 0
        for e in self.__edges:
            weight += e.get_edge_weight()
        return weight

    def get_graph_dictionary(self):
        """"
        Returns a dictionary structure of the Graph. This dictionary structure is the same as what is returned
        by the function read_stsp.get_stsp_data() in order to reuse the logic from the plotting of the graph.
        This dictionary can be used as an input to Graph_Plotter.py
        """
        nodes = {}
        n = 0
        for node in self.__nodes:
            nodes[n] = tuple(node.get_data())
            n += 1

        edges = set()
        for edge in self.__edges:
            new_edge = (edge.get_node_a().get_id(), edge.get_node_b().get_id())
            edges.add(new_edge)

        graph_dict = {}
        graph_dict["nodes"] = nodes
        graph_dict["edges"] = edges

        return graph_dict

    def __repr__(self):
        name = self.get_name()
        nb_nodes = self.get_num_nodes()

        #print nodes
        s = 'Graph %s has %d nodes' % (name, nb_nodes)
        for node in self.get_nodes():
            s += '\n  ' + repr(node)

        #print edges
        s += '\n\nGraph %s has %d edges \n' % (name, self.__num_edges)
        n = 1
        for edge in self.__edges:
            s += str(n) + ': ' + repr(edge) + "\n"
            n += 1

        #print the weight of the graph
        s += '\nGraph has weight: %d \n' % (self.get_graph_weight())

        return s


if __name__ == '__main__':

    from node import Node

    G = Graph(name='Graphe test')
    for k in range(5):
        G.add_node(Node(name='Noeud test %d' % k))

    print G

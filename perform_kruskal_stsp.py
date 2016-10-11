def start_kruskal_algorithm(my_graph):
    """
     Perform the kruskal's algorithm
     entry: Graph object
     return: Graph object
    """
    from graph import Graph

    # Creates the min_spanning_tree graph and adds nodes to min_spanning_tree graph
    min_spanning_tree = Graph(my_graph.get_name())

    for node in my_graph.get_nodes():
        min_spanning_tree.add_node(node)

    # Gets the list of edges and sorts it
    sorted_edges = my_graph.get_edges()
    sorted_edges.sort()

    # Kruskal`s algorithm
    for e in sorted_edges:
        set_of_a_root = e.get_node_a().find_disjoint_set() #get the set nodes in the 1st node of the edge
        set_of_b_root = e.get_node_b().find_disjoint_set() #get the set nodes in the 2nd node of the edge
        if set_of_a_root != set_of_b_root:
            min_spanning_tree.add_edge(e)
            set_of_a_root.set_kruskal_parent(set_of_b_root)

    return min_spanning_tree #return the minimun-spanning-tree

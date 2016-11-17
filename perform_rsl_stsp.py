import copy

def start_rsl_stsp(min_span_tree, start_node):
    """
     Perform Primm's algorithm
     @:param: my_graph: Graph object - original complete graph
     @:param start_node: Node to start the tour from
     @:return: min_tour: Graph object - minimum spanning graph
    """
    from graph import Graph

    #1)Initialize new graph used for a tour
    min_tour = Graph(min_span_tree.get_name() + '_RSL_TOUR')
    counter = 0
    for node in min_span_tree.get_nodes():
        if counter == start_node:
            print "Starting RSL tour from node %d" % (start_node)
            #do-something
        new_node = copy.copy(node)
        min_tour.add_node(new_node)
        counter += 1

    #2)Perform the algorithm
    #todo

    return min_tour

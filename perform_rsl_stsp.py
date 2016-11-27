import copy

def start_rsl_stsp(graph, min_span_tree, start_node):
    """
     Perform Primm's algorithm
     @:param: graph: Graph object - original complete graph
     @:param min_span_tree: our minimum spanning tree
     @:param start_node: Node to start the tour from
     @:return: min_tour: Graph object - minimum spanning graph
    """
    from graph import Graph

    #1)Initialize new graph used for a tour
    min_tour = Graph(min_span_tree.get_name() + '_RSL_TOUR')

    #print "Starting RSL tour from node %d" % (start_node)

    for node in min_span_tree.get_nodes():
        node.is_visited_dfs = False
        new_node = copy.copy(node)
        min_tour.add_node(new_node)

    #2)Perform the RSL algorithm
    # list that acts like a queue
    queue = [min_span_tree.get_nodes()[start_node]]
    # Mark the start_node as visited
    min_span_tree.get_nodes()[start_node].is_visited_dfs = True
    tour_ordering = []

    #Perform an iterative dfs using preorder visit policy
    while len(queue) != 0:
        u = queue.pop()
        tour_ordering.append(u)
        neighbors = min_span_tree.get_adjacency_matrix_dictionary()[u]

        #We must visit the nodes in preorder, then we have to sort the child nodes
        # and reverse them in order to do it.
        for node in reversed(sorted(neighbors.keys())):
            if not node.is_visited_dfs:
                node.is_visited_dfs = True
                queue.append(node)

    # Builds the approximate minimum tour using graph object. We used the complete graph object
    # because we needed to access the original graph's edges
    for i in xrange(len(tour_ordering)-1):
        u = graph.get_nodes()[tour_ordering[i].get_id()]
        v = graph.get_nodes()[tour_ordering[i+1].get_id()]

        min_tour.add_edge(graph.get_adjacency_matrix_dictionary()[u][v])

    u = graph.get_nodes()[tour_ordering[-1].get_id()]
    v = graph.get_nodes()[tour_ordering[0].get_id()]
    min_tour.add_edge(graph.get_adjacency_matrix_dictionary()[u][v])

    #Return the approximate minimum tour
    return min_tour
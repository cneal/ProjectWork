"""Main TSP hook."""

from tsp_helper import get_distance
from tsp_helper import GeoPoint
from node import Node
from edge import Edge
from graph import Graph
import perform_kruskal_stsp
import perform_prim_stsp
import perform_rsl_stsp


def get_visit_order(geoPoints):
    """THIS IS THE ONLY FUNCTION THAT YOU NEED TO MODIFY FOR PHASE 5.

    The only argument, *geoPoints*, is a list of points that user has marked.
    Each element of geoPoints is an instance of the GeoPoint class. You need to
    create your graph using these points. You obtain the distance between two
    points by calling the *getDistance* function; for example:

    get_distance(geoPoints[0], geoPoints[1])

    Run your tsp solver and return the locations visit order. The return value,
    *order*, must be a list of indices of points, specifying the visit order.

    In the example implementation below, we visit each point by the order
    in which they were marked (clicked).
    """
    n_marks = len(geoPoints)

    graph = Graph("Googlemaps_Points")
    nodes = []
    Node.reset_node_count()

    # We received the geoPoints, then we build the corresponding graph.
    # Creating all the nodes:
    for point in geoPoints:
        node = Node("", point)
        graph.add_node(node)
        nodes.append(node)

    # Creating all the Edges:
    for i in xrange(0, n_marks-1):
        for j in xrange(i, n_marks):
            # We don't create edges from a node to itself
            if i != j:
                graph.add_edge(Edge(nodes[i], nodes[j], get_distance(nodes[i].get_data(), nodes[j].get_data())))

    cur_best_starting_node = -1
    cur_best_tour_length = -1
    cur_best_tour = Graph(graph.get_name() + '_RSL_TOUR')
    cur_best_tour_order = []

    # First, we find the best using the minimum spanning tree from the Kruskal's algorithm:
    minimum_spanning_tree = perform_kruskal_stsp.start_kruskal_algorithm(graph)

    print "======================================== NEW TOUR ========================================"
    for start_node in xrange(n_marks):
        min_tour, min_tour_order = perform_rsl_stsp.start_rsl_stsp(graph, minimum_spanning_tree, start_node)
        min_tour_length = min_tour.get_graph_weight()

        if cur_best_tour_length == -1 or min_tour_length < cur_best_tour_length:
            cur_best_tour_length = min_tour_length
            cur_best_starting_node = start_node
            cur_best_tour = min_tour
            cur_best_tour_order = min_tour_order

        print "start_node: %d, algorithm: Kruskal, min_span_tree: %d, min_tour_length: %d" % (
            start_node, minimum_spanning_tree.get_graph_weight(), min_tour_length)
    print 'Best length: %d, Best start_node: %d\n' % (cur_best_tour_length, cur_best_starting_node)

    # Secondly, we find the best using the minimum spanning tree from the Prim's algorithm:
    for start_node in xrange(n_marks):
        minimum_spanning_tree = perform_prim_stsp.start_prim_algorithm(graph, start_node)

        min_tour, tour_order = perform_rsl_stsp.start_rsl_stsp(graph, minimum_spanning_tree, start_node)
        min_tour_length = min_tour.get_graph_weight()

        if min_tour_length < cur_best_tour_length:
            cur_best_tour_length = min_tour_length
            cur_best_starting_node = start_node
            cur_best_tour = min_tour
            cur_best_tour_order = min_tour_order

        print "start_node: %d, algorithm: Prim, min_span_tree: %d, min_tour_length: %d" % (
            start_node, minimum_spanning_tree.get_graph_weight(), min_tour_length)
    print 'Best length: %d, Best start_node: %d' % (cur_best_tour_length, cur_best_starting_node)

    # Finally, we print the information of the best tour found and the best tour's order is returned:
    print "\n\nBest tour found: %r  Best tour's length: %d" % (cur_best_tour_order, cur_best_tour_length)
    print "==========================================================================================\n"
    return cur_best_tour_order

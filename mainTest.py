import perform_rsl_stsp
import read_stsp
import read_kruskal_test_stsp
import perform_kruskal_stsp
import perform_prim_stsp
import Graph_Plotter
from graph import Graph

print('TEST: Starting TSP Program...')

finstance = "instances/instances/stsp\\bayg29.tsp"
#finstance = "instances\instances\stsp\\bays29.tsp"
#finstance = "instances\instances\stsp\\brazil58.tsp"
#finstance = "instances\instances\stsp\\brg180.tsp"
#finstance = "instances\instances\stsp\\dantzig42.tsp"
#finstance = "instances\instances\stsp\\fri26.tsp"
#finstance = "instances\instances\stsp\\gr17.tsp"
#finstance = "instances\instances\stsp\\gr21.tsp"
#finstance = "instances\instances\stsp\\gr24.tsp"
#finstance = "instances\instances\stsp\\gr48.tsp"
#finstance = "instances\instances\stsp\\gr120.tsp"
#finstance = "instances\instances\stsp\\hk48.tsp"
#finstance = "instances\instances\stsp\\pa561.tsp"
#finstance = "instances\instances\stsp\\swiss42.tsp"

# Reads the instance file
instance_dict = read_stsp.get_stsp_data(finstance) #load .stsp file, store information as a dictionary
#instance_dict = read_kruskal_test_stsp.get_stsp_data()

# Creates the Graph object based on the read instance
my_graph = Graph()
my_graph.build_from_instance(instance_dict)

#print 'Initial graph: \n'
#print my_graph

algorithm = 'prim'
start_node = 5


if algorithm == 'kruskal':
    print 'About to perform Kruskal algorithm'

    # Build the minimum-spanning-tree from myGraph
    minimum_spanning_tree = perform_kruskal_stsp.start_kruskal_algorithm(my_graph)
    min_graph_dict = minimum_spanning_tree.get_graph_dictionary()

    print instance_dict
    print min_graph_dict

    # Print the minimum-spanning-tree
    print '\n'
    # print minimum_spanning_tree.get_graph_weight()

    print "graph weight: %d, min span tree weight: %d" % (my_graph.get_graph_weight(), minimum_spanning_tree.get_graph_weight())

    # Graph_Plotter.plot_graph(instance_dict)
    Graph_Plotter.plot_min_span_tree(instance_dict, min_graph_dict)

    print "...done execution!"

else:
    print 'About to perform Prim algorithm'
    minimum_spanning_tree = perform_prim_stsp.start_prim_algorithm(my_graph, start_node)
    print "graph weight: %d, min span tree weight: %d" % (my_graph.get_graph_weight(), minimum_spanning_tree.get_graph_weight())
    min_graph_dict = minimum_spanning_tree.get_graph_dictionary()
    Graph_Plotter.plot_min_span_tree(instance_dict, min_graph_dict)
    print "...done execution!"

print "original graph weight: %d, min span tree weight: %d" % (my_graph.get_graph_weight(), minimum_spanning_tree.get_graph_weight())
print "...creating a minimum tour"
min_tour = perform_rsl_stsp.start_rsl_stsp(minimum_spanning_tree, start_node)

print finstance















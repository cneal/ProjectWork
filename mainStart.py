import sys
import platform
import read_stsp
from graph import Graph
import perform_kruskal_stsp
import read_kruskal_test_stsp
import perform_prim_stsp
import perform_rsl_stsp
import Graph_Plotter
import read_rsl_test_stsp

#python mainStart.py bayg29.tsp 5 kruskal plot verbose

#python mainStart.py brazil58.tsp all prim

print('Starting TSP Program...')

#Read the instance file name given as argument according of the running platform
if platform.system() == 'Windows':
    finstance = "instances\instances\stsp\\" + sys.argv[1]
else:
    finstance = "instances/instances/stsp/" + sys.argv[1]

if sys.argv[1] != 'test':
    # Reads the instance file
    instance_dict = read_stsp.get_stsp_data(finstance)  # load .stsp file, store information as a dictionary
else:
    finstance = 'test'
    instance_dict = read_kruskal_test_stsp.get_stsp_data() #load the test instance discussed in class
    instance_dict = read_rsl_test_stsp.get_stsp_data()  # load the test instance discussed in class

print "Using file: ", finstance

# Creates the Graph object based on the read instance
my_graph = Graph() #constructor
my_graph.build_from_instance(instance_dict) #initialize with the instance information
print '...created graph!'

#Determine whether to start from a particular node, or whether to find the best node for this instance
find_best = False
if sys.argv[2] == 'all':
    print 'Finding the best starting point for this instance...'
    find_best = True
    start_node = 0
    num_nodes = instance_dict['header']['DIMENSION']
else:
    start_node = int(sys.argv[2])
    print "Starting from node %d..." % (start_node)

min_tree_alg = sys.argv[3]
print min_tree_alg
if min_tree_alg != 'prim' and min_tree_alg != 'kruskal':
    print 'Please enter a valid algorithm: prim OR kruskal'
    print 'exiting!!'
    quit()

if find_best is False: #perform the algorithm for the given start node
    if min_tree_alg == 'prim': #use prim algorithm
        print '...using Prim\'s algorithm!'
        minimum_spanning_tree = perform_prim_stsp.start_prim_algorithm(my_graph, start_node)
    else:
        print '...using Kruskal\'s algorithm!'
        minimum_spanning_tree = perform_kruskal_stsp.start_kruskal_algorithm(my_graph)  # pass in the graph, performs kruskal algorithm, returns new min-span-tree as a graph

    print '...created minimum spanning tree!'
    print "original graph weight: %d, min span tree weight: %d" % (my_graph.get_graph_weight(), minimum_spanning_tree.get_graph_weight())

    print "...creating a minimum tour"
    min_tour = perform_rsl_stsp.start_rsl_stsp(my_graph, minimum_spanning_tree, start_node)
    print "minimum tour cost: %d" % (min_tour.get_graph_weight())

    if 'plot' in sys.argv:
        print 'Creating plot...'
        Graph_Plotter.plot_over_full_graph(instance_dict, min_tour.get_graph_dictionary(), start_node)

else: #perform the algorithm for all nodes in the instance and find the best one

    if min_tree_alg == 'kruskal':
        minimum_spanning_tree = perform_kruskal_stsp.start_kruskal_algorithm(my_graph)  # pass in the graph, performs kruskal algorithm, returns new min-span-tree as a graph

    cur_best_starting_node = -1
    cur_best_tour_length = -1
    cur_best_tour = Graph(my_graph.get_name() + '_RSL_TOUR')

    for start_node in xrange(num_nodes):
        if min_tree_alg == 'prim':
            minimum_spanning_tree = perform_prim_stsp.start_prim_algorithm(my_graph, start_node)

        min_tour = perform_rsl_stsp.start_rsl_stsp(my_graph, minimum_spanning_tree, start_node)
        min_tour_length = min_tour.get_graph_weight()
        print "start_node: %d, min_span_tree: %d, min_tour_length: %d" % (start_node, minimum_spanning_tree.get_graph_weight(), min_tour_length)

        if cur_best_tour_length == -1 or min_tour_length < cur_best_tour_length:
            cur_best_tour_length = min_tour_length
            cur_best_starting_node = start_node
            cur_best_tour = min_tour

    if 'plot' in sys.argv:
        print 'Creating plot...'
        Graph_Plotter.plot_over_full_graph(instance_dict, cur_best_tour.get_graph_dictionary(), cur_best_starting_node)
    print 'Best start_node: %d, Best length: %d' % (cur_best_starting_node, cur_best_tour_length)

print 'done!!'

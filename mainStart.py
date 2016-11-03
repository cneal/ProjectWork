import sys
import platform
import read_stsp
from graph import Graph
import perform_kruskal_stsp
import read_kruskal_test_stsp
import Graph_Plotter
import perform_prim_stsp

print('Starting TSP Program...')

# Read the instance file name given as argument according of the running platform
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

print "Using file: ", finstance

# Creates the Graph object based on the read instance
my_graph = Graph() #constructor
my_graph.build_from_instance(instance_dict) #initialize with the instance information
print '...created graph!'

# Build the minimum-spanning-tree from my_graph
if sys.argv[2] == 'prim': #use prim algorithm
    print '...using Prim\'s algorithm!'
    minimum_spanning_tree = perform_kruskal_stsp.start_kruskal_algorithm(my_graph) #pass in the graph, performs kruskal algorithm, returns new min-span-tree as a graph
else: #use kruskal algorithm
    print '...using Krusgal\'s algorithm!'
    minimum_spanning_tree = perform_prim_stsp.start_prim_algorithm(my_graph)

print '...created minimum spanning tree!'

#check to print out the min span tree information
if len(sys.argv) > 3:
    if sys.argv[3] == 'verbose':
        print 'PRINTING MIN SPAN TREE...'
        print minimum_spanning_tree

print "original graph weight: %d, min span tree weight: %d" % (my_graph.get_graph_weight(), minimum_spanning_tree.get_graph_weight())

#check to plot the min span tree
if len(sys.argv) > 3:
    if sys.argv[3] == 'plot':
        print 'Creating plot...'
        Graph_Plotter.plot_min_span_tree(instance_dict, minimum_spanning_tree.get_graph_dictionary())
if len(sys.argv) > 4:
    if sys.argv[3] == 'plot' or sys.argv[4] == 'plot':
        print 'Creating plot...'
        Graph_Plotter.plot_min_span_tree(instance_dict, minimum_spanning_tree.get_graph_dictionary())

print 'done!!'

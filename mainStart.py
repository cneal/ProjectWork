import sys
import platform
import read_stsp
from graph import Graph
import perform_kruskal_stsp
import read_kruskal_test_stsp
import perform_prim_stsp
import perform_rsl_stsp
import Graph_Plotter

#python mainStart.py bayg29.tsp 5 kruskal plot verbose

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

print "Using file: ", finstance

# Creates the Graph object based on the read instance
my_graph = Graph() #constructor
my_graph.build_from_instance(instance_dict) #initialize with the instance information
print '...created graph!'

#get the starting node
start_node = int(sys.argv[2])
print "Starting from node %d..." % (start_node)

# Build the minimum-spanning-tree from my_graph
if sys.argv[3] == 'prim': #use prim algorithm
    print '...using Prim\'s algorithm!'
    minimum_spanning_tree = perform_prim_stsp.start_prim_algorithm(my_graph, start_node)
elif sys.argv[3] == 'kruskal': #use kruskal algorithm
    print '...using Kruskal\'s algorithm!'
    minimum_spanning_tree = perform_kruskal_stsp.start_kruskal_algorithm(my_graph) #pass in the graph, performs kruskal algorithm, returns new min-span-tree as a graph
else:
    print 'Please enter a valid algorithm: prim OR kruskal'
    print 'exiting!!'
    quit()

print '...created minimum spanning tree!'

print "original graph weight: %d, min span tree weight: %d" % (my_graph.get_graph_weight(), minimum_spanning_tree.get_graph_weight())
print "...creating a minimum tour"
min_tour = perform_rsl_stsp.start_rsl_stsp(minimum_spanning_tree, start_node)

if 'verbose' in sys.argv:
    print 'PRINTING MIN SPAN TREE...'
    print minimum_spanning_tree

if 'plot' in sys.argv:
    print 'Creating plot...'
    Graph_Plotter.plot_min_span_tree(instance_dict, minimum_spanning_tree.get_graph_dictionary())

print 'done!!'

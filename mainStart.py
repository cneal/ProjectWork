import sys
import platform
import read_stsp
from graph import Graph
import perform_kruskal_stsp
import read_kruskal_test_stsp

print('Starting TSP Program...')

# Read the instance file name given as argument according of the running platform
if platform.system() == 'Windows':
    finstance = "instances\instances\stsp\\" + sys.argv[1]
else:
    finstance = "instances/instances/stsp/" + sys.argv[1]

print "Using file: ", finstance

# Reads the instance file
# instance_dict = read_kruskal_test_stsp.get_stsp_data() # load class' example
instanceDict = read_stsp.get_stsp_data(finstance) #load .stsp file, store information as a dictionary

# Creates the Graph object based on the read instance
myGraph = Graph()
myGraph.build_from_instance(instanceDict)

# Print and plot the Graph
print '\n'
print myGraph
myGraph.plot_graph(True)

# Build the minimum-spanning-tree from myGraph
minimum_spanning_tree = perform_kruskal_stsp.start_kruskal_algorithm(myGraph)

# Print the minimum-spanning-tree
print '\n'
print minimum_spanning_tree
import sys
import platform
import read_stsp
from graph import Graph

print('Starting TSP Program...')

# Read the instance file name given as argument according of the running platform
if platform.system() == 'Windows':
    finstance = "instances\instances\stsp\\" + sys.argv[1]
else:
    finstance = "instances/instances/stsp/" + sys.argv[1]

print "Using file: ", finstance

# Reads the instance file
instanceDict = read_stsp.get_stsp_data(finstance) #load .stsp file, store information as a dictionary

# Creates the Graph object based on the read instance
myGraph = Graph(instanceDict)

print '\n'
print myGraph

myGraph.plot_graph(True)
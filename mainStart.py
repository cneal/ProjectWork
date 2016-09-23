import sys
import platform
import read_stsp
import graph

print('Starting TSP Program...')

if __name__ == '__main__':
    str('Starting TSP Program...')
    # Read the instance file name given as argument according of the running plataform
    if platform.system() == 'Windows':
        finstance = "instances\instances\stsp\\" + sys.argv[1]
    else:
        finstance = "instances/instances/stsp/" + sys.argv[1]

print "Using file: ", finstance
# Reads the instance file
readInstance = read_stsp.getStspData(finstance) #load .stsp file, store information as a dictionary

# Creates the Graph object based on the read instance
myGraph = graph.Graph(readInstance) # intialize the graph, pass in its name

print '\n'
print myGraph


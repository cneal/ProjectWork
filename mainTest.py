import read_stsp
import graph

print('TEST: Starting TSP Program...')

#finstance = "instances\instances\stsp\\bayg29.tsp"
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
readInstance = read_stsp.getStspData(finstance) #load .stsp file, store information as a dictionary

# Creates the Graph object based on the read instance
myGraph = graph.Graph(readInstance)

print '\n'
print myGraph

print "...done execution!"




import read_stsp
import graph
import node
import edge

print('TEST: Starting TSP Program...')

finstance = "instances\instances\stsp\\bayg29.tsp"
#finstance = "instances\instances\stsp\\pa561.tsp"
#finstance = "instances\instances\stsp\\brazil58.tsp"
#finstance = "instances\instances\stsp\\gr120.tsp"
#finstance = "instances\instances\stsp\\brg180.tsp"
#finstance = "instances\instances\stsp\\fri26.tsp"

print "Using file: ", finstance
a = read_stsp.getStspData(finstance) #load .stsp file, store information as a dictionnary

print 'Nodes: ', a["nodes"]
print 'Edges: ', a["edges"]

myGraph = graph.Graph(a["header"]["NAME"]) #intialize the graph, pass in its name

#add nodes to graph
numNodes = a["header"]["DIMENSION"] #number of nodes (i.e. dimensions of the problem)
for curNodeVal in xrange(0,numNodes):
    myNode = node.Node(curNodeVal, a["nodes"][curNodeVal]) #create a new node instance
    myGraph.add_node(myNode) #add node to the graph

print myGraph

#add edges to graph
for tuple in a["edges"]:
    fromNodeId = tuple[0]
    toNodeId = tuple[1]
    edgeWeight = tuple[2]
    myEdge = edge.Edge(fromNodeId, toNodeId, edgeWeight) #create a new Edge instance
    print myEdge
    myGraph.add_edge(myEdge)

#Prints out the adjacency matrix for now. This information needs to be represented in the function "Graph.__repr__(self):"
matrix = myGraph.get_adjacency_matrix()
for i in range(0, len(matrix)):
    print matrix[i]

#print myGraph

#print "...done execution!"




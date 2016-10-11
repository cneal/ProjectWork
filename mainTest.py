import read_stsp
import read_kruskal_test_stsp
import perform_kruskal_stsp
from graph import Graph

print('TEST: Starting TSP Program...')

finstance = "instances\instances\stsp\\bayg29.tsp"
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
#instance_dict = read_stsp.get_stsp_data(finstance) #load .stsp file, store information as a dictionary
instance_dict = read_kruskal_test_stsp.get_stsp_data()

# Creates the Graph object based on the read instance
my_graph = Graph(instance_dict)

print '\n'
print my_graph

perform_kruskal_stsp.start_kruskal_algorithm(my_graph)

plt = my_graph.plot_graph(True)

print "...done execution!"




import copy
from heap import Heap

def start_prim_algorithm(my_graph, start_node):
    """
     Perform Primm's algorithm
     @:param: my_graph: Graph object - original complete graph
     @:return: min_spanning_tree: Graph object - minimum spanning graph
    """
    from graph import Graph

    # Creates the min_spanning_tree graph and adds nodes to min_spanning_tree graph as needed
    min_spanning_tree = Graph(my_graph.get_name() + '_MIN_SPAN_TREE_PRIM')

    prim_heap = Heap() #initialize a heap data structure to extract min node
    counter = 0
    for node in my_graph.get_nodes():
        #i) initialize set prim values
        if counter == start_node:
            node.prim_key = 0 #set the root node, is has a key of 0
        else:
            node.prim_key = float("inf") #non-root nodes have key initialized to infinity
        node.prim_parent = node #initialize the parent to itself
        prim_heap.insert(node)
        node.in_prim_heap = True #flag to indicated the node is still in the Prim Heap
        counter += 1
        #ii) initialize new min span tree node
        new_node = copy.copy(node)
        min_spanning_tree.add_node(new_node)

    while prim_heap.get_size() > 0:
        cur_min = prim_heap.extract_minimum() #get minimum node
        #print cur_min
        cur_min.in_prim_heap = False #indicate the node is no longer in the heap

        if cur_min != cur_min.prim_parent:
            edge = my_graph.get_adjacency_matrix_dictionary()[cur_min][cur_min.prim_parent] #get the edge between the current_min node and its parent node
            min_spanning_tree.add_edge(edge) #add the edge to the min-span-tree

        neighbors = my_graph.get_adjacency_matrix_dictionary()[cur_min] #get all the neighbors

        for cur_neighbor, edge in neighbors.iteritems():
            if cur_neighbor.in_prim_heap and edge.get_edge_weight() < cur_neighbor.prim_key: #if neighbor is in the heap AND if the current edge weight is less than its prim_key
                cur_neighbor.prim_parent = cur_min
                cur_neighbor.prim_key = edge.get_edge_weight()
                neighbor_heap_index = prim_heap.get_heap_items().index(cur_neighbor) #find where the node is in the heap
                prim_heap.decrease_key_at(neighbor_heap_index, edge.get_edge_weight()) #update its key value in the heap

    return min_spanning_tree


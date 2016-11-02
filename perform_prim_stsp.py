import copy
from heap import Heap

def start_prim_algorithm(my_graph):
    """
         Perform the kruskal's algorithm
         entry: Graph object
         return: Graph object
        """
    from graph import Graph

    # Creates the min_spanning_tree graph and adds nodes to min_spanning_tree graph
    min_spanning_tree = Graph(my_graph.get_name() + '_MIN_SPAN_TREE')

    # initialize a heap data structure to extract min node
    prim_heap = Heap()
    root_set = False
    for node in my_graph.get_nodes():
        #set prim values
        if root_set == False:
            node.set_prim_key(0)
            root_set = True
        prim_heap.insert(node)
        node.set_in_prim_heap(True)
        #initialize new min span tree node
        new_node = copy.copy(node)
        min_spanning_tree.add_node(new_node)

    while prim_heap.get_size() > 0:
        print prim_heap
        cur_min = prim_heap.extract_minimum()
        print cur_min
        s = '%s --> %s' % (cur_min.get_prim_parent().get_id(), cur_min.get_id())
        print s

        cur_min.set_in_prim_heap(False)

        if cur_min != cur_min.get_prim_parent():
            edge = my_graph.get_adjacency_matrix_dictionary()[cur_min][cur_min.get_prim_parent()]
            min_spanning_tree.add_edge(edge)

        neighbors = my_graph.get_adjacency_matrix_dictionary()[cur_min]

        for node, edge in neighbors.iteritems():
            cur_neighbor = node
            if cur_neighbor.get_in_prim_heap() == True and edge.get_edge_weight() < cur_neighbor.get_prim_key():
                cur_neighbor.set_prim_parent(cur_min)
                cur_neighbor.set_prim_key(edge.get_edge_weight())
                neighbor_heap_index = prim_heap.get_heap_items().index(cur_neighbor) #find where the node is in the heap
                prim_heap.decrease_key_at(neighbor_heap_index, edge.get_edge_weight())

    return min_spanning_tree


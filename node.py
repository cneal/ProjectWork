class Node(object):
    """
    Une classe generique pour representer les noeuds d'un graphe.
    """

    __node_count = -1   # Compteur global partage par toutes les instances.

    def __init__(self, name='Sans nom', data=None):
        self.__name = name
        self.__data = data
        Node.__node_count += 1
        self.__id = Node.__node_count

        self.__kruskal_parent = self
        self.__prim_parent = self
        self.__prim_key = float("inf")
        self.__in_prim_heap = False
        self.__rank = 0

        self.__visited_dfs = False

    def get_name(self):
        "Donne le nom du noeud."
        return self.__name

    def get_id(self):
        "Donne le numero d'identification du noeud."
        return self.__id

    def get_data(self):
        "Donne les donnees contenues dans le noeud."
        return self.__data

    def get_rank(self):
        "Returns the node's rank."
        return self.__rank
    @property
    def kruskal_parent(self):
        "Returns the parent of the node. It's used in kruskal's algorithm"
        return self.__kruskal_parent

    @kruskal_parent.setter
    def kruskal_parent(self, new_kruskal_parent):
        "Sets the parent of the node. It's used in kruskal's algorithm"
        self.__kruskal_parent = new_kruskal_parent

    @property
    def in_prim_heap(self):
        return self.__in_prim_heap

    @in_prim_heap.setter
    def in_prim_heap(self, in_heap):
        "@in_heap: boolean"
        self.__in_prim_heap = in_heap

    def find_disjoint_set(self):
        "Finds the root of the node's disjoint set. This function does path compression."
        if self.__kruskal_parent != self:
            self.__kruskal_parent = self.__kruskal_parent.find_disjoint_set()
        return self.__kruskal_parent

    def increase_rank(self):
        "It increments the node's rank by 1."
        self.__rank += 1

    @staticmethod
    def union_by_rank(set_of_a_root, set_of_b_root):
        "It function unites two disjointed sets considering the roots' ranks"
        if set_of_a_root.get_rank() > set_of_b_root.get_rank():
            set_of_b_root.kruskal_parent = set_of_a_root.kruskal_parent
        else:
            set_of_a_root.kruskal_parent = set_of_b_root

        if set_of_a_root.get_rank == set_of_b_root.get_rank():
            set_of_b_root.increase_rank()

    @property
    def prim_parent(self):
        "Returns the parent of the node. It's used in prim's algorithm"
        return self.__prim_parent

    @prim_parent.setter
    def prim_parent(self, new_prim_parent):
        "Sets the parent of the node. It's used in prim's algorithm"
        self.__prim_parent = new_prim_parent

    @property
    def prim_key(self):
        "Returns the value of prim's key"
        return self.__prim_key

    @prim_key.setter
    def prim_key(self, new_value):
        "Sets the value of prim's key"
        self.__prim_key = new_value

    @property
    def is_visited_dfs(self):
        "Informs if the node was visited in the dfs"
        return self.__visited_dfs

    @is_visited_dfs.setter
    def is_visited_dfs(self, value):
        "Sets the value of __visited_dfs"
        self.__visited_dfs = value

    @staticmethod
    def reset_node_count():
        Node.__node_count = -1

    def __repr__(self):
        id = self.get_id()
        name = self.get_name()
        data = self.get_data()
        s = 'Noeud %s (id %d)' % (name, id)
        s += ' (Coordinates: ' + repr(data) + ') '
        return s

    def __lt__(self, other):
        return self.__id < other.get_id()

if __name__ == '__main__':

    nodes = []
    for k in range(5):
        nodes.append(Node())

    for node in nodes:
        print node

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
        self.__rank = 0

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

    def get_kruskal_parent(self):
        "Returns the parent of the node. It's used in kruskal's algorithm"
        return self.__kruskal_parent

    def set_kruskal_parent(self, new_kruskal_parent):
        "Sets the parent of the node. It's used in kruskal's algorithm"
        self.__kruskal_parent = new_kruskal_parent

    def find_disjoint_set(self):
        "Finds the root of the node's disjoint set. It's function do path compression."
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
            set_of_b_root.set_kruskal_parent(set_of_a_root.get_kruskal_parent())
        else:
            set_of_a_root.set_kruskal_parent(set_of_b_root)

        if set_of_a_root.get_rank == set_of_b_root.get_rank():
            set_of_b_root.increase_rank()

    def get_prim_parent(self):
        "Returns the parent of the node. It's used in prim's algorithm"
        return self.__prim_parent

    def set_prim_parent(self, new_prim_parent):
        "Sets the parent of the node. It's used in prim's algorithm"
        self.__prim_parent = new_prim_parent

    def get_prim_key(self):
        return self.__prim_key

    def set_prim_key(self, new_value):
        self.__prim_key = new_value

    def __repr__(self):
        id = self.get_id()
        name = self.get_name()
        data = self.get_data()
        s = 'Noeud %s (id %d)' % (name, id)
        s += ' (Coordinates: ' + repr(data) + ')'
        return s


if __name__ == '__main__':

    nodes = []
    for k in range(5):
        nodes.append(Node())

    for node in nodes:
        print node

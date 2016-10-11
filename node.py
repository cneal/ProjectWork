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

        self.__krusgall_parent = self

    def get_name(self):
        "Donne le nom du noeud."
        return self.__name

    def get_id(self):
        "Donne le numero d'identification du noeud."
        return self.__id

    def get_data(self):
        "Donne les donnees contenues dans le noeud."
        return self.__data

    def get_krusgall_parent(self):
        return self.__krusgall_parent

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

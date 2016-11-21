import math
from node import Node

class Heap(Node):
    """
    This class implements one heap priority queue of Node objects.
    """

    def __init__(self):
        self.__items = []

    def __get_parent(self, index):
        "It returns the index of the parent one node"
        return int(math.floor((index+1)/2.0)-1)

    def __get_left_child(self, index):
        "It returns the index of the left child of one node"
        return int(((index+1)*2)-1)

    def __get_right_child(self, index):
        "It returns the index of the right child of one node"
        return int((index+1)*2)

    def __min_heapity(self, index):
        " This function is responsible to keep the min-heap property"
        left_child = self.__get_left_child(index)
        right_child = self.__get_right_child(index)

        if left_child <= self.get_size()-1 and self.__items[left_child].get_prim_key() < self.__items[index].get_prim_key():
            lowest = left_child
        else:
            lowest = index

        if right_child <= self.get_size()-1 and self.__items[right_child].get_prim_key() < self.__items[lowest].get_prim_key():
            lowest = right_child

        if lowest != index:
            aux = self.__items[index]
            self.__items[index] = self.__items[lowest]
            self.__items[lowest] = aux

            self.__min_heapity(lowest)

    def minimum(self):
        "Returns the minimal prim-key's value in the heap"
        if self.get_size() == 0:
            print "Empty Heap!"
            return None
        return self.__items[0].get_prim_key()

    def extract_minimum(self):
        "Extracts the Node which has the minimal prim-key's value in heap"
        if self.get_size() == 0:
            print "Empty Heap!"
            return None
        elif self.get_size() == 1:
            return self.__items.pop()

        minimum = self.__items[0]
        last = self.__items.pop()
        self.__items[0] = last
        self.__min_heapity(0)

        return minimum

    def decrease_key_at(self, index, new_value):
        "Changes the value of prim-key in index to new_value"
        if self.get_size() == 0:
            print "Empty Heap!"
            return None

        if new_value > self.__items[index].get_prim_key():
            print "New value: %f for index: %d is bigger than the current." %(new_value, index)
            return None

        self.__items[index].set_prim_key(new_value)
        while index > 0 and self.__items[self.__get_parent(index)].get_prim_key() > new_value:
            aux = self.__items[self.__get_parent(index)]
            self.__items[self.__get_parent(index)] = self.__items[index]
            self.__items[index] = aux
            index = self.__get_parent(index)

    def insert(self, newElement):
        "Inserts one new Node in the heap"
        self.__items.append(newElement)
        self.decrease_key_at(self.get_size()-1, newElement.get_prim_key())

    def get_size(self):
        "Returns heap's size"
        return len(self.__items)

    def get_heap_items(self):
        "Return the items that are in the heap"
        return self.__items

    def __repr__(self):
        s = "["
        for i in self.__items:
            s += "%r," % (i.get_prim_key())
        s += "]"

        return s
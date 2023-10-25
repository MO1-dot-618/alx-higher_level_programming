#!/usr/bin/python3
"""Singly Linked List"""


class Node:
    """class Node"""

    def __init__(self, data, next_node=None):
        """Initialize a new Node"""
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """ getter for data """
        return self.__data

    @data.setter
    def data(self, value):
        """ setter for data """
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """ getter for next_node """
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """ setter for next_node """
        if not isinstance(value, Node) and value is not None:
            raise TypeError("next_node must be a Node object")
        self.__next_node = value

class SinglyLinkedList:
    """ SLL """

    def __init__(self):
        """ initilize SL """
        self.__head = None

    def sorted_insert(self, value):
        """ insert in a sorted list """
        if self.__head == None:
            self.__head = Node(value, None)
        elif self.__head.data > value:
            new = Node(value, self.__head)
            self.__head = new
        else:
            node = self.__head
            while node.next_node != None and node.next_node.data < value:
                node = node.next_node
            new = Node(value, node.next_node)
            node.next_node = new

    def __str__(self):
        """Define the print() representation of a SinglyLinkedList."""
        values = []
        tmp = self.__head
        while tmp is not None:
            values.append(str(tmp.data))
            tmp = tmp.next_node
        return ('\n'.join(values))

#!/usr/bin/python3
"""A module that defines a class Node"""


class Node:
    """class Node that defines a node of a singly linked list"""
    def __init__(self, data, next_node=None):
        """The instantiation method"""
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """The data attribute retriever"""
        return self.__data

    @property
    def next_node(self):
        """Next node retriever"""
        return self.__next_node

    @data.setter
    def data(self, value):
        """The data attribute setter"""
        if isinstance(value, int):
            self.__data = value
        else:
            raise TypeError("data must be an integer")

    @next_node.setter
    def next_node(self, value):
        """The next_node attribute setter"""


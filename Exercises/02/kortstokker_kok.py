#!/usr/bin/python3

from sys import stdin
from itertools import repeat


class Node:
    def __init__(self, value):
        self.value = value
        self.right = None
        self.left = None

    def __lt__(self, other):
        return self.value < other.value


class BinaryTree:
    def __init__(self):
        self.root = None

    def sorted(self, root=False):
        if root == None:
            return []
        if root == False:
            root = self.root
        l = []
        l.extend(self.sorted(root.left))
        l.append(root.value)
        l.extend(self.sorted(root.right))
        return l

    def insert(self, value):
        """Inserts a value in the tree"""
        node = Node(value)
        if self.root:
            self._insert(node, self.root)
        else:
            self.root = node

    def _insert(self, node, root):
        """Inserts a node after a node"""
        if node < root:
            if root.left:
                self._insert(node, root.left)
            else:
                root.left = node
        else:
            if root.right:
                self._insert(node, root.right)
            else:
                root.right = node


def merge(decks):
    # Legg alt til i et binĂŚrtre
    tre = BinaryTree()
    for deck in decks:
        for card in deck:
            tre.insert(card)

    l = [char for value, char in tre.sorted()]
    return "".join(l)


decks = []
for line in stdin:
    (index, list) = line.split(':')
    deck = zip(map(int, list.split(',')), repeat(index))
    decks.append(deck)
print(merge(decks))

__author__ = "K4LI"

################################################################################
# REQUIREMENTS

from toSVG.toSVG import *
from os import *

class BinTree:
    def __init__(self, key, left, right):
        """
        Init Tree
        """
        self.key = key
        self.left = left
        self.right = right

################################################################################
# Write a function that calculates the size of a binary tree.

def size(B):
    if B == None:
        return 0
    else:
        return 1 + size(B.left) + size(B.right)

################################################################################
# Tests

C = BinTree(9, None, None)
D = BinTree(4, None, None)
B = BinTree(3, None, D)
A = BinTree(7, B, C)

toSVG(A, "tree")
print(size(A))

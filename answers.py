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

def size(B, size = 0):
    if B != None:
        size += 1
        if B.left != None:
            size += size(B.left, size)
        if B.right != None:
            size += size(B.right, size)
        return size

################################################################################

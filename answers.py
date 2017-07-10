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

# Write a function that calculates the height of a binary tree.

def height(B):
    if B == None:
        return -1
    else:
        return 1 + max(height(B.left), height(B.right))

#

def bfs(B):
    '''
    Prints keys in breadth-first traversal order
    '''
    if B != None:
        q = queue.Queue()
        q = queue.enqueue(B, q)
        while not queue.isEmpty(q):
            T = queue.dequeue(q)
            print(T.key, end=' ')
            if T.left != None:
                q = queue.enqueue(T.left, q)
            if T.right != None:
                q = queue.enqueue(T.right, q)

# computes the width with a "change-level mark"
def width(B):
    if B == None:
        return 0
    else:
        q = queue.Queue()
        q = queue.enqueue(B, q)
        q = queue.enqueue(None, q)  #change-level mark
        w = 0
        max_w = 0
        while not queue.isEmpty(q):
            T = queue.dequeue(q)
            if T == None:
                max_w = max(max_w, w)
                w = 0
                if not queue.isEmpty(q):
                    q = queue.enqueue(None, q)
            else:
                w = w + 1
                if T.left != None:
                    q = queue.enqueue(T.left, q)
                if T.right != None:
                    q = queue.enqueue(T.right, q)
        return max_w

################################################################################
# Tests

C = BinTree(9, None, None)
D = BinTree(4, None, None)
B = BinTree(3, None, D)
A = BinTree(7, B, C)

toSVG(A, "tree")
print(size(A))

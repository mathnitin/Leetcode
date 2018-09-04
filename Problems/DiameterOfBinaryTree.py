#!/bin/python

'''
https://www.geeksforgeeks.org/diameter-of-a-binary-tree/

Diameter of a Binary Tree

The diameter of a tree (sometimes called the width) is the number of nodes on the longest path between two end nodes. 
The diagram below shows two trees each with diameter nine, the leaves that form the ends of a longest path are shaded 
(note that there is more than one path in each tree of length nine, but no path longer than nine nodes).


        1
       / \
      2   3
     / \
    4   5
Diameter is 4

        1
       / \
      2   3
     / \
    4   5
   / \
  6   7
       \
        8
         \
          9
           \
           10
Diameter is 7

'''

# A binary tree node
class Node:
    # Constructor to create a new node
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def diameter(root):
    # Node is None. Height is 0 and diameter is 0
    if root is None:
        return 0, 0

    lH = 0
    rH = 0
    lD = 0
    rD = 0

    lH, lD = diameter(root.left)
    rH, rD = diameter(root.right)
    diam = max((lH+rH+1), max(lD, rD))
    hegith = max(lH, rH) + 1
    return hegith, diam

if __name__ == "__main__":
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.left.left.left = Node(6)
    root.left.left.right = Node(7)
    root.left.left.right.right = Node(8)
    root.left.left.right.right.right = Node(9)
    root.left.left.right.right.right = Node(10)
    h, d = diameter(root)
    print "Diameter of given binary tree is", d
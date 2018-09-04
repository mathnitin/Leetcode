#!/bin/bash

'''
https://leetcode.com/problems/populating-next-right-pointers-in-each-node-ii/description/

Given a binary tree

struct TreeLinkNode {
  TreeLinkNode *left;
  TreeLinkNode *right;
  TreeLinkNode *next;
}
Populate each next pointer to point to its next right node. If there is no next right node, the next pointer should be set to NULL.

Initially, all next pointers are set to NULL.

Note:

You may only use constant extra space.
Recursive approach is fine, implicit stack space does not count as extra space for this problem.
Example:

Given the following binary tree,

     1
   /  \
  2    3
 / \    \
4   5    7
After calling your function, the tree should look like:

     1 -> NULL
   /  \
  2 -> 3 -> NULL
 / \    \
4-> 5 -> 7 -> NULL

'''

# Definition for binary tree with next pointer.
# class TreeLinkNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None

class Solution:
    # @param root, a tree link node
    # @return nothing
    def connect(self, root):
        if not root:
            return None
    
        level = [root]
        while level: # push level from top to bottom
            next_level = []
        
            while level:   # in one level push from left to right
                if level[0].left:
                    next_level.append(level[0].left)
                if level[0].right:
                    next_level.append(level[0].right)
                level.pop(0)
            
            for i in range(len(next_level)-1):
                next_level[i].next = next_level[i+1]
        
            level = next_level
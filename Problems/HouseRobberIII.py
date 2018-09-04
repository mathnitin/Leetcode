#!/bin/python

'''
https://leetcode.com/problems/house-robber-iii/description/
The thief has found himself a new place for his thievery again. There is only one entrance to this area, called the "root." 
Besides the root, each house has one and only one parent house. After a tour, the smart thief realized that "all houses in this 
place forms a binary tree". It will automatically contact the police if two directly-linked houses were broken into on the same night.

Determine the maximum amount of money the thief can rob tonight without alerting the police.

Example 1:
     3
    / \
   2   3
    \   \ 
     3   1
Maximum amount of money the thief can rob = 3 + 3 + 1 = 7.
Example 2:
     3
    / \
   4   5
  / \   \ 
 1   3   1
Maximum amount of money the thief can rob = 4 + 5 = 9.
'''

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class BinaryTree():
    def __init__(self):
        self.root = None

    def insert(self, val):
        node = TreeNode(val)
        if self.root is None:
            self.root = node
        else:
            curNode = self.root
            while curNode is not None:
                if val <= curNode:
                    if curNode.left is None:
                        curNode.left = node
                        return
                    else:
                        curNode = curNode.left
                else:
                    if curNode.right is None:
                        curNode.right = node
                        return
                    else:
                        curNode = curNode.right


class Solution(object):
    def rob(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        map = {}
        return self.robSub(root, map)
        
    def robSub(self, root, map):
        if root is None: 
            return 0
        if root in map: 
            return map[root]
        val = 0
        if root.left is not None:
            val += self.robSub(root.left.left, map) + self.robSub(root.left.right, map)
        if root.right is not None:
            val += self.robSub(root.right.left, map) + self.robSub(root.right.right, map)
        val = max(val + root.val, self.robSub(root.left, map) + self.robSub(root.right, map))
        map[root] = val
        return val


if __name__ == "__main__":
    arr = [3,2,3,3,1]
    tree = BinaryTree()
    for i in arr:
        tree.insert(i)
    so = Solution()
    print so.rob(tree.root)
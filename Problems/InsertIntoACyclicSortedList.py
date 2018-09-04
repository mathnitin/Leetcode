#!/bin/python
'''
https://leetcode.com/problems/insert-into-a-cyclic-sorted-list/description/

Given a node from a cyclic linked list which is sorted in ascending order, 
write a function to insert a value into the list such that it remains a cyclic 
sorted list. The given node can be a reference to any single node in the list, 
and may not be necessarily the smallest value in the cyclic list.

If there are multiple suitable places for insertion, you may choose any place to 
insert the new value. After the insertion, the cyclic list should remain sorted.

If the list is empty (i.e., given node is null), you should create a new single 
cyclic list and return the reference to that single node. Otherwise, you should 
return the original given node.

The following example may help you understand the problem better:

 2
        1
       / \
      /   \
     4-----3 <--- head

In the figure above, there is a cyclic sorted list of three elements. You are 
given a reference to the node with value 3, and we need to insert 2 into the list.

   1----->2
   |      |
   |      |
   4<-----3

The new node should insert between node 1 and node 3. After the insertion, 
the list should look like this, and we should still return node 3.
'''

class Node():
    def __init__(self, value):
        self.val = value
        self.next = None

class CyclicLinkList():
    def insert(self, node, newNode):
        if node is None:
            newNode.next = newNode
            return newNode
        else:
            curNode = node
            if curNode.next is node:
                curNode.next = newNode
                newNode.next = node
            else:
                if curNode.val == newNode.val:
                    newNode.next = curNode.next
                    curNode.next = newNode
                elif curNode.val < newNode.val:
                    while curNode.next is not node:
                        if curNode.next.val > newNode.val:
                            break
                        curNode = curNode.next
                    newNode.next = curNode.next
                    curNode.next = newNode
                elif curNode.next.val > newNode.val:
                    while curNode.next is not node:
                        if curNode.next.val < newNode.val:
                            break
                        curNode = curNode.next
                    newNode.next = curNode.next
                    curNode.next = newNode
        return node

    def traverse(self, node):
        nodeDict = {}
        output = []
        if node is None:
            return ""
        while node not in nodeDict:
            output.append(str(node.val)+"-->")
            nodeDict[node] = node.val
            node = node.next
        return output


if __name__ == "__main__":
    arr = [4, 1]
    cl = CyclicLinkList()
    head = cl.insert(None, Node(3))
    for i in arr:
        head = cl.insert(head, Node(i))
    print cl.traverse(head)
    cl.insert(head, Node(2))
    print cl.traverse(head)
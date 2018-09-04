#!/bin/python

'''
https://leetcode.com/problems/maximal-square/description/

Given a 2D binary matrix filled with 0's and 1's, find the largest square containing only 1's and return its area.

Example:

Input: 

1 0 1 0 0
1 0 1 1 1
1 1 1 1 1
1 0 0 1 0

Output: 4
'''

class Solution(object):
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        totalSize = 0
        output = []
        maxRow = len(matrix)
        if maxRow == 0:
            return 0
        maxCol = len(matrix[0])
        
        # Create empty array.
        output = [[0 for x in range(maxCol)] for y in range(maxRow)] 

        # Handle all the rows and values.
        for row in range((maxRow-1), -1, -1):
            for col in range((maxCol-1), -1, -1):
                if matrix[row][col] == "1":
                    if row == (maxRow-1) and col == (maxCol-1):
                        output[row][col] = int(matrix[row][col])
                    elif row == maxRow-1 or col == maxCol-1:
                        output[row][col] = int(matrix[row][col])
                    else:
                        output[row][col] = int(matrix[row][col]) + (min(int(output[row][col+1]), int(output[row+1][col]), int(output[row+1][col+1])))
                    if output[row][col] > totalSize:
                        totalSize = output[row][col]
                else:
                    output[row][col] = 0

        return pow(totalSize,2)
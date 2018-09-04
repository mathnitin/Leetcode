#!/bin/python

'''
https://leetcode.com/problems/number-of-islands/description/

Given a 2d grid map of '1's (land) and '0's (water), count the number of islands. An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

Example 1:

Input:
11110
11010
11000
00000

Output: 1
Example 2:

Input:
11000
11000
00100
00011

Output: 3
'''

class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        counter = 0
        
        # Grid is empty or not provided.
        if grid is None or len(grid) == 0:
            return counter
                
        maxRow = len(grid)
        maxCol = len(grid[0])

        for row in range(maxRow):
            for col in range(maxCol):
                if grid[row][col] == "1":
                    counter += 1
                    self.numIslandsUtil(grid, row, col)
        return counter
    
    
    def numIslandsUtil(self, grid, xCord, yCord):
        if xCord<0 or xCord>=len(grid) or yCord<0 or yCord>=len(grid[0]) or grid[xCord][yCord]=="0":
            return
        grid[xCord][yCord] = "0"
        self.numIslandsUtil(grid, xCord+1, yCord)
        self.numIslandsUtil(grid, xCord-1, yCord)
        self.numIslandsUtil(grid, xCord, yCord+1)
        self.numIslandsUtil(grid, xCord, yCord-1)
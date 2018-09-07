#!/bin/python

'''
https://leetcode.com/problems/two-sum/description/

Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:

Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
'''

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        dic = {}
        for i in range(len(nums)):
            comp = (target - nums[i])
            if nums[i] in dic:
                return [dic[nums[i]], i]
            dic[comp] = i
        return []

if __name__ == "__main__":
    s = Solution()
    print s.twoSum([2, 7, 11, 15], 9)
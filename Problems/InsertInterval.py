#!/bin/python
'''
https://leetcode.com/problems/insert-interval/description/
Given a set of non-overlapping intervals, insert a new interval into the intervals (merge if necessary).

You may assume that the intervals were initially sorted according to their start times.

Example 1:

Input: intervals = [[1,3],[6,9]], newInterval = [2,5]
Output: [[1,5],[6,9]]
Example 2:

Input: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
Output: [[1,2],[3,10],[12,16]]
Explanation: Because the new interval [4,8] overlaps with [3,5],[6,7],[8,10].
'''

# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[Interval]
        :type newInterval: Interval
        :rtype: List[Interval]
        """
        if not intervals:
            return [newInterval]
        # Find the insert location of newInterval.start
        # Binary search codes can be refactored to a helper function
        s = 0
        lo, hi = 0, len(intervals)-1
        while lo<=hi:
            mid = lo + (hi-lo)/2
            if intervals[mid].end == newInterval.start:
                s = mid
                break
            elif intervals[mid].end > newInterval.start:
                hi = mid - 1
            else:
                lo = mid + 1
        else:        
            s = lo
        
        # Find the insert location of newInterval.end
        # Binary search codes can be refactored to a helper function
        e = 0
        lo, hi = 0, len(intervals)-1       
        while lo<=hi:
            mid = lo + (hi-lo)/2
            if intervals[mid].start == newInterval.end:
                e = mid + 1
                break
            elif intervals[mid].start > newInterval.end:
                hi = mid - 1
            else:
                lo = mid + 1
        else:
            e = lo

        # newInterval should be merged with intervals[s:e]
        tmp = [Interval(min(intervals[s].start, newInterval.start), max(intervals[e-1].end, newInterval.end))] if s < e else [newInterval]
        return intervals[:s] + tmp + intervals[e:]
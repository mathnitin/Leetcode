#!/bin/bash
'''
https://www.geeksforgeeks.org/longest-common-prefix-matching-set-6/

Longest Common Prefix Matching | Set-6
Given a set of strings, find the longest common prefix.

Examples:

Input: str[] = {geeksforgeeks, geeks, geek, geezer}
Output: gee

Input: str[] = {apple, ape, april}
Output: ap
'''

def commonSequence(input, start, end):
    string1 = input[0][start:end+1]
    for string in input:
        if string[start:end+1] != string1:
            return False
    return True


if __name__ == "__main__":
    input = ["geeksforgeeks", "geeks", "geek", "geezer"]
    
    if len(input) == 0:
        print ''

    index = 0
    prefix = ''
    smallestLength = len(input[index])
    for i in range(1, len(input)):
        if len(input[i]) < smallestLength:
            index = i
            smallestLength = len(input[i])
    
    start = 0
    end = smallestLength
    while start <= end:
        mid = (start + end)/2
        result = commonSequence(input, start, mid)
        if result == True:
            prefix += input[0][start:(mid+1)]
            start = mid+1
        else:
            end = mid-1
    print "Result:", prefix
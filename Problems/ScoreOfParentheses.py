#!/bin/python

'''
https://leetcode.com/problems/score-of-parentheses/description/

Given a balanced parentheses string S, compute the score of the string based on the following rule:

() has score 1
AB has score A + B, where A and B are balanced parentheses strings.
(A) has score 2 * A, where A is a balanced parentheses string.
 

Example 1:

Input: "()"
Output: 1
Example 2:

Input: "(())"
Output: 2
Example 3:

Input: "()()"
Output: 2
Example 4:

Input: "(()(()))"
Output: 6
 

Note:

S is a balanced parentheses string, containing only ( and ).
2 <= S.length <= 50
'''

class Solution(object):
    def scoreOfParentheses(self, S):
        """
        :type S: str
        :rtype: int
        """
        stack = []
        for ch in S:
            if ch == '(':
                stack.append(ch)
            else:
                if stack[-1] == '(':
                    stack[-1] = '1'
                else:
                    lastChar = str(stack.pop())
                    evalString = "0"
                    while lastChar != '(':
                        evalString += '+'
                        evalString += lastChar
                        lastChar = str(stack.pop())
                    evalString = "2*("+evalString+")"
                    stack.append(eval(evalString))
        retVal = '0'
        while stack:
            retVal += '+' + str(stack.pop())
        return eval(retVal)
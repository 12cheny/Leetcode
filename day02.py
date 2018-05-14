'''
Determine whether an integer is a palindrome. An integer is a palindrome when it reads the same backward as forward.
Example 1:
Input: 121
Output: true

Example 2:
Input: -121
Output: false
'''

class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        x_str=str(x)
        if x_str[::-1]==x_str:
            return True
        else :
            return False

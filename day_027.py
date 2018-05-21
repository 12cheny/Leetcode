#Given a non-negative integer num, repeatedly add all its digits until the result has only one digit.

class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        while(num>=10):
            string=str(num)
            lenth=len(string)
            num=0
            for i in range(lenth):
                num+=int(string[i])
        return num

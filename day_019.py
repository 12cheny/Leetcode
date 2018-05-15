#Given a non-empty array of digits representing a non-negative integer, plus one to the integer.

class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        num=0
        for i in range(len(digits)):
            num+=digits[i]*pow(10,len(digits)-i-1)
        num+=1
        num=str(num)
        return [int(i) for i in num]

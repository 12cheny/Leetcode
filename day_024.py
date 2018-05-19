#The gray code is a binary numeral system where two successive values differ in only one bit.

class Solution(object):
    def grayCode(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        if n==0:
            return [0]
        if n==1:
            return [0,1]
        else:
            return self.grayCode(n-1)+[x+pow(2,n-1) for x in reversed(self.grayCode(n-1))]

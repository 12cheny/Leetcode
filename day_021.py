#Implement int sqrt(int x).
#Compute and return the square root of x, where x is guaranteed to be a non-negative integer.

class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        import math
        return int(math.sqrt(x))

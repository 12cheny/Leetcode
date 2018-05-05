#Implement pow(x, n), which calculates x raised to the power n (xn).

#range()有范围，不能直接累乘，会报错MemoryError

class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        
        if n == 0:
            return 1
        elif n == 1:
            return x
        is_negative = 0
        if n < 0:
            n = -1 * n
            is_negative = 1
        half = self.myPow(x, n // 2)
        if n % 2 == 0:
            result = half * half
        else:
            result = x * half * half
        if is_negative:
            return 1 / result
        return result

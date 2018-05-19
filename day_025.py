#Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:

class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if matrix==[[]] or matrix==[]:
            return False
        for i in range(len(matrix)):
            if target in matrix[i]:
                return True
            elif target<matrix[i][-1]:
                return False
        return False

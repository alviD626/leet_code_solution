class Solution(object):
    def diagonalSum(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: int
        """
        total = 0
        n = len(mat[0])-1
        
        for i in range(len(mat)):
            total += mat[i][i]
            if i != n-i:
                total += mat[i][n-i]
        return total
class Solution(object):
    def minTimeToVisitAllPoints(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        def rule(A,B):
            return max(abs(A[0]-B[0]),abs(A[1]-B[1]))
        sum = 0
        for tup1,tup2 in zip(points[:-1],points[1:]):
            sum += rule(tup1,tup2)
        return sum
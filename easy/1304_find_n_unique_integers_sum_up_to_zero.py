class Solution(object):
    def sumZero(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        a = []
        if n%2 == 1:
            a.append(0)
        for i in range(1,n):
            if len(a) == n:
                break
            a.append(i)
            a.append(-i)
        return a
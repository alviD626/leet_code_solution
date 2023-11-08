class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        
        if x == 0:
            return 1
        else:
            return format(x**n,".5f")
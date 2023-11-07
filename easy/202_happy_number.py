class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        result = set()
        while n!=1:
            n = sum(int(i) ** 2 for i in str(n))
            if n in result:
                return False
            else:
                result.add(n)
        else:
            return True
            
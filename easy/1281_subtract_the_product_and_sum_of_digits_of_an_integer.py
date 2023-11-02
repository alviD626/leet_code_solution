# For solution2
from functools import reduce
class Solution(object):
    def subtractProductAndSum(self, n):
        """
        :type n: int
        :rtype: int
        """
        # Solution 1
        # prod = 1
        # sum = 0
        # s = str(n)
        # for i in s:
        #     digit = int(i)
        #     prod *= digit
        #     sum += digit
        # return prod - sum
        
        # Solution 2
        a = [int(x) for x in str(n)]
        return reduce((lambda x, y: x * y), a) - reduce((lambda x, y: x + y), a)
        

n = int(input("Enter the number: "))
print(Solution().subtractProductAndSum(n)) 
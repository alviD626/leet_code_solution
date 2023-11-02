class Solution(object):
    def smallestEvenMultiple(self, n):
        """
        :type n: int
        :rtype: int
        """
        # solution 1
        # if n % 2 == 1:
        #     return n*2
        # else:
        #     return n
        
        # solution 2
        return n if n % 2 == 0 else n * 2

number = int(input())
solution = Solution()
result = solution.smallestEvenMultiple(number)
print(result)
class Solution(object):
    def theMaximumAchievableX(self, num, t):
        """
        :type num: int
        :type t: int
        :rtype: int
        """
        return num+t*2

num = int(input())
target = int(input())
solution = Solution()
result = solution.theMaximumAchievableX(num,target)
print(result)
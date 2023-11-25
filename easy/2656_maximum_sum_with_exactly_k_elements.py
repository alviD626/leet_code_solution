class Solution(object):
    def maximizeSum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        max_value = max(nums)
        ans = 0
        for i in range(k):
            ans+=max_value
            max_value+=1
        return ans

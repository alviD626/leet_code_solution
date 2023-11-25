class Solution(object):
    def sumCounts(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        result = []
        for i in range(len(nums)):
            for j in range(0,len(nums)+1):
                result.append(len(set(nums[i:j]))**2)
        return sum(result)
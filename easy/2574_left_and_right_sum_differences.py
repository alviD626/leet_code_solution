class Solution(object):
    def leftRightDifference(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        result = []
        for i in range(len(nums)):
            left = sum(nums[:i+1])
            right = sum(nums[i:])
            result.append(abs(left-right))
        return result
class Solution(object):
    def maximumStrongPairXor(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max = 0
        for i in range(len(nums)):
            for j in range(len(nums)):
                x = nums[i]
                y = nums[j]
                if abs(x-y) <= min(x,y):
                    res = x^y
                    if res>max:
                        max = res
        return max
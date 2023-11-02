import logging
class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        # Solution 1
        for i in range(k):
            previous = nums[-1]
            for j in range(len(nums)):
                nums[j], previous= previous, nums[j]
                
        # Solution 2
        k=k%len(nums)
        nums[:]=nums[-k:]+nums[:-k]
import logging
class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        for i in range(k):
            previous = nums[-1]
            for j in range(len(nums)):
                temp = nums[i]
                nums[i] = previous
                previous = temp
        logging.debug(f"nums: {nums}")
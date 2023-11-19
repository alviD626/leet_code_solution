class Solution(object):
    def decompressRLElist(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        length, result = len(nums), []
        for i in range(0,length,2):
            result.extend(nums[i]*[nums[i+1]])
        return result
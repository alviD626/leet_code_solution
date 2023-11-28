class Solution(object):
    def distinctDifferenceArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
       
            
        res = []
        for i in range(len(nums)):
            res.append(len(set(nums[:i+1]))-len(set(nums[i+1:])))
        return res
class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        result = None
        count = 0
        for i in nums:
            if count == 0:
                result = i
            count += (1 if i == result else -1)
        return result
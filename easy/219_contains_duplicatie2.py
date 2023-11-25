class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        result = {}
        for i, n in enumerate(nums):
            if n in result and abs(i - result[n]) <= k:
                return True
            else:
                result[n] = i
        return False
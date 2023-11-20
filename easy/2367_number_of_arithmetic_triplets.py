class Solution(object):
    def arithmeticTriplets(self, nums, diff):
        """
        :type nums: List[int]
        :type diff: int
        :rtype: int
        """
        count = 0
        for num in nums:
            if num+diff in nums and num+diff*2 in nums:
                count +=1
        return count
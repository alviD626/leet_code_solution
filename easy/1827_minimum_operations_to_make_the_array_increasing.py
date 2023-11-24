class Solution(object):
    def minOperations(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        current = count = 0
        for n in nums:
            if n<=current:
                current+=1
                count += current-n
            else:
                current = n
        return count
class Solution(object):
    def sumOfUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        value = []
        [value.append(num) for num in nums if nums.count(num) == 1]
        return sum(value)
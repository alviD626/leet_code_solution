class Solution(object):
    def differenceOfSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        all_sum = sum(nums)
        digit_sum = 0 
        all_digit = "".join(str(digit) for digit in nums)
        for digit in all_digit:
            digit_sum += int(digit)
        return abs(all_sum-digit_sum)
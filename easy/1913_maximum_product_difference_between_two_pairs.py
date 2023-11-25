class Solution(object):
    def maxProductDifference(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        def multiply_list_elements(num):
            result = 1
            for n in num:
                result *= n
            return result
        s = sorted(nums)
        minimum = s[:2]
        maximum_rev = s[::-1]
        maximum = maximum_rev[:2]
        output1 = multiply_list_elements(minimum)
        output2 = multiply_list_elements(maximum)
        return output2-output1

nums = [5,6,2,7,4]
print(Solution.maxProductDifference(nums))
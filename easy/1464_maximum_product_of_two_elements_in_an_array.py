class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        x = sorted(nums)
        reverse = x[::-1]
        for i in reverse:
            output1= reverse[0]-1
            output2= reverse[1]-1
        return output1*output2
nums = [3,4,5,2]
print(Solution.maxProduct(nums))
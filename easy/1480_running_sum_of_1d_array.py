class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        for i in range(1,len(nums)):
            nums[i] += nums[i-1]
        return nums

input_str = input("Enter the list: ")
nums = input_str.split()
for i in range(len(nums)):
    nums[i] = int(nums[i])

print (Solution().runningSum(nums))
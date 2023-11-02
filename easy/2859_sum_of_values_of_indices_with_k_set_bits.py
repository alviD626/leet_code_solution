class Solution(object):
    def sumIndicesWithKSetBits(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        
        result = 0
        for i in range(len(nums)):
            if bin(i).count('1') == k:
                result += nums[i]
        
        return result
    

input_usr = input("Enter the list: ")
nums = input_usr.split()
for i in range(len(nums)):
    nums[i] = int(nums[i])
    
target = int(input("Enter the target: "))

print(Solution().sumIndicesWithKSetBits(nums,target))
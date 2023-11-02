class Solution(object):
    def numIdenticalPairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        result = 0
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if (nums[j]) == (nums[i]):
                    result += 1
        return result
    
input_usr = input("Enter the list: ")
nums = input_usr.split()
for i in range(len(nums)):
    nums[i] = int(nums[i])
    
print(Solution().numIdenticalPairs(nums))
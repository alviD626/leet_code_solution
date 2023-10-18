class Solution(object):
    def numIdenticalPairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        memo = sorted(nums)
        count = 0
        for i in range(memob-+` -+):
            if memo[i] == memo[i+1]:
                count +=1
        return count
    
input_str = input("Input: ")
nums = input_str.split()
for i in range(len(nums)):
    nums[i] = int(nums[i])

solution = Solution()
result = solution.numIdenticalPairs(nums)
print(result)   
class Solution(object):
    def minimumOperations(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = 0
        for number in nums:
            if number % 3 != 0:
                count += 1
        return count
    
    
nums = [1,2,3,4]
solution = Solution()
print(solution.minimumOperations(nums))
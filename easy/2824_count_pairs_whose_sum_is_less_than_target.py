class Solution(object):
    def countPairs(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        n = len(nums)
        ans = 0
        for i in range(n):
            for j in range(i,n):
                if i<j and nums[i]+nums[j]<target:
                    ans+=1
        return ans

input_user = input("Enter the numbers: ")
nums = input_user.split()
for i in range(len(nums)):
    nums[i] = int(nums[i])
    
target = int(input("Enter the target: "))
print (Solution().countPairs(nums, target))
class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # Solution 1 
        # if not nums:
        #     return False
        # elif len(nums)==1:
        #     return False
        # else:
        #     duplicate = {}
        #     for i in nums:
        #         if i in duplicate:
        #             return True
        #         else:
        #             duplicate[i]=1
        #     return False
        
        # Solution 2
        n = len(nums)
        for i in range(n-1):
            for j in range (i+1,n):
                if nums[i] == nums[j]:
                    return True
        return False
                
int_usr = input("Eneter the list: ")
nums = int_usr.split()
for i in range(len(nums)):
    nums[i] = int(nums[i])
    
print (Solution().containsDuplicate(nums))
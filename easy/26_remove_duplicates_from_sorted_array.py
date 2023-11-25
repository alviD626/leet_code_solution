class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Solution 1
        # nums[:] = sorted(set(nums))
        # return len(nums)

        # Solution 2
        x = 1
        for i in range(len(nums)-1):
            if (nums[i]!= nums[i+1]):
                nums[x] = nums[i+1]
                x += 1
        return x
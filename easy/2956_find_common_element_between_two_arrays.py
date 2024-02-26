class Solution(object):
    def findIntersectionValues(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        count1 = 0
        count2 = 0
        for i in nums1:
            if i in nums2:
                count1 +=1
        for i in nums2:
            if i in nums1:
                count2 +=1
        return count1,count2
nums1 = [4,3,2,3,1]
nums2 = [2,2,5,2,3,6]
solution = Solution()
print(solution.findIntersectionValues(nums1,nums2))
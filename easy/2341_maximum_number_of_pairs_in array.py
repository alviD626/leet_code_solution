class Solution(object):
    def numberOfPairs(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        ans = [0]*2
        c = Counter(nums)
        for v in c.values():
            ans[0] += (v//2)
            ans[1] += (v%2)
        return ans
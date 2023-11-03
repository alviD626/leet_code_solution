class Solution(object):
    def buildArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        es = []
        for k, _ in enumerate(nums):
            res.append(nums[nums[k]])
        return res
r
input_str = input()
user_str = input_str.split()
for i in range(len(user_str)):
    user_str[i] = int(user_str[i])
    
soluton = Solution()
result = soluton.buildArray(user_str)
print(user_str)
class Solution(object):
    def shuffle(self, nums, n):
        """
        :type nums: List[int]
        :type n: int
        :rtype: List[int]
        """
        res = []
        for i in range(n):
            res.append(nums[i])
            print("res1:",res)
            res.append(nums[i+n])
            print("res2:",res)
        return res

        # res = []
        # for i, j in zip(nums[:n],nums[n:]):
        #     res+=[i,j]
        # return res 

input_str = input()
nums = input_str.split()
for i in range(len(nums)):
    nums[i] = int(nums[i])

target = int(input())

solution = Solution()
result = solution.shuffle(nums,target)

print(result)
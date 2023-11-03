# class Solution:
#     def twoSum(self, nums: list[int], target: int) -> list[int]:
#         for i in range(len(nums)-1):
#             for j in range(i+1,len(nums)):
#                 if nums[i] + nums[j] == target:
#                     print("Output: ",[i,j]) 

# input_string  = input("nums = ")
# user_list = input_string .split()

# for i in range(len(user_list)):
#     user_list[i] = int(user_list[i])

# #declare the target number
# target = int(input("target = "))

# solution = Solution()
# result = solution.twoSum(user_list,target)

# brute force algorithm


class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        for i in range(len(nums)-1):
            for j in range(i+1,len(nums)):
                if nums[i] + nums[j] == target:
                    return [i,j]
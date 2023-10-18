class Solution:
    def isMonotonic(self, nums: list[int]) -> bool:
        return nums == sorted(nums) or nums == sorted(nums, reverse = True)
    
number_str = input("input: ")
number = number_str.split()
for i in range(len(number)):
    number[i] = int(number[i])
solution = Solution()
result = solution.isMonotonic(number)
print(result)
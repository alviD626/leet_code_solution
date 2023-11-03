class Solution(object):
    def getConcatenation(self,nums):
        # num2 = nums
        # concate = nums+num2
        # return concate
        
        # nums.extend(nums)
        # return nums
        
        return nums*2
    
list1 = [1,2,3,1]
solution = Solution()
result = solution.getConcatenation(list1)
print(result)
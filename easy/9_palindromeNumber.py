# class Solution:
#     def isPalindrome(self,x:int)->bool:
#         if str(x) == str(x)[::-1]:
#             print("true")
#         else:
#             print("false")
         
            
# num = int(input("X = "))
# solution = Solution()
# result = solution.isPalindrome(num)


class Solution:
    def isPalindrome(self, x: int) -> bool:
        if str(x) == str(x)[::-1]:
            return True
        else:
            return False
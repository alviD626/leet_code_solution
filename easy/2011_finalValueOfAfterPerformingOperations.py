class Solution:
    def finalValueAfterOperations(self, operations: list[str]) -> int:
        a=operations.count("++X")
        b=operations.count("X++")
        c=operations.count("--X") 
        d=operations.count("X--")
        
        return a+b-c-d  
input_str = input("input: ")
solution = Solution()
result = solution.finalValueAfterOperations(input_str)
print(result)
class Solution:
    def interpret(self, command: str) -> str:
        return command.replace("()","o").replace("(al)","al")
    
word = input("Input: ")
solution = Solution()
result = solution.interpret(word)
print(result)
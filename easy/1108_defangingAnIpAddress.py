class Solution:
    def defangIPaddr(self, address: str) -> str:
        # for i in address:
        #     if i == ".":
        #         return address.replace(".","[.]")
        return address.replace(".","[.]")

input_str = input("input: ")
solution = Solution()
result = solution.defangIPaddr(input_str)
print(result)
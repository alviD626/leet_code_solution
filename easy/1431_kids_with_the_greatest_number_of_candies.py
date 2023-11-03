class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        """
        :type candies: List[int]
        :type extraCandies: int
        :rtype: List[bool]
        """
        max_value = max(candies)
        result = []
        
        for i in candies:
            if i + extraCandies >= max_value:
                result.append(True)
            else:
                result.append(False)
        return result
            
user_input = input("Enter the number of candies: ")
candies = user_input.split()
for i in range(len(candies)):
    candies[i] = int(candies[i])

extraCandies = int(input("Enter the number of extra Candies: "))
solution = Solution()
result = solution.kidsWithCandies(candies,extraCandies)
print(result)
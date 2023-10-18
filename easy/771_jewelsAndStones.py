class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        count = 0
        jewel = list(jewels)
        for stone in stones:
            if stone in jewel:
                count +=1
        return count
        
        # return sum(map(stones.count,list(jewels)))

input_jew = input("Jewels: ")
input_tar = input("Stones: ")
solution = Solution()
result = solution.numJewelsInStones(input_jew,input_tar)
print(result)



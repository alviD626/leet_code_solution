class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        result = []
        tempNums = nums.copy()
        nums.sort()
        for i in tempNums:
            result.append(nums.index(i))
        return result
    
    #solution 2
        # return [sorted(nums).index(n) for n in nums]
        
    
user_input = input("Enter the number of candies: ")
candies = user_input.split()
for i in range(len(candies)):
    candies[i] = int(candies[i])

print(Solution().smallerNumbersThanCurrent(candies))
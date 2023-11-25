class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        count = 0
        for i in nums:
            if i!= val:
                nums[count] = i
                count += 1
        return count
    
int_usr = input("Enter the list: ")
user = int_usr.split()
for i in range(len(user)):
    user[i] = int(user[i])

val = int(input("Enter the val: "))
print(Solution.removeElement(user,val))
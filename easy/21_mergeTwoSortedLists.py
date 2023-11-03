class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        listt = list1 + list2
        listt.sort()
        return listt
        
        
list1 = [1,2,4]
list2 = [1,3,4]
solution = Solution()
result = solution.mergeTwoLists(list1,list2)
print(result)
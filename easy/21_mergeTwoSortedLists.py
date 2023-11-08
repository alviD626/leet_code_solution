class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        # Solution 1
        # listt = list1 + list2
        # listt.sort()
        # return listt
        
        # Solution 2
        if list1 and list2:
            if list1.val > list2.val:
                list1, list2 = list2, list1
            list1.next = self.mergeTwoLists(list1.next, list2)
        return list1 or list2
        
list1 = [1,2,4]
list2 = [1,3,4]
solution = Solution()
result = solution.mergeTwoLists(list1,list2)
print(result)
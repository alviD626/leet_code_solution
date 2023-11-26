# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        l1.reverse()
        l2.reverse()
        l3 = ''.join(map(str,l1))
        l4 = ''.join(map(str,l2))
        l5 = int(l3)
        l6 = int(l4)
        l7 = l5 + l6
        l8 = list(map(int,str(l7)))
        return l8

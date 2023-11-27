class Solution(object):
    def canBeEqual(self, target, arr):
        """
        :type target: List[int]
        :type arr: List[int]
        :rtype: bool
        """
        sort1 = sorted(target)
        sort2 = sorted(arr)
        if sort1 == sort2:
            return True
        return False
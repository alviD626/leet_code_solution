class Solution(object):
    def maxDepth(self, s):
        """
        :type s: str
        :rtype: int
        """
        result = count = 0
        for ch in s:
            if ch == '(':
                count+=1
                result = max(result,count)
            elif ch == ')':
                count -= 1
        return result
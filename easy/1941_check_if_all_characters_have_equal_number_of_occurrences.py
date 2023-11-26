class Solution(object):
    def areOccurrencesEqual(self, s):
        """
        :type s: str
        :rtype: bool
        """
        m = s.count(s[0])
        for i in s:
            if s.count(i)!=m:
                return False
        return True
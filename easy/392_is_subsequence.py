class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        for character in s:
            i = t.find(character)
            if i == -1: 
                return False
            else:
                t =  t[i+1:]
        return True
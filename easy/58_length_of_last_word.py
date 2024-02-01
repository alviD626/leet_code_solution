class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        worlist = s.split()
        return len(worlist[-1])
        
        # len(s.strip().split()[-1])
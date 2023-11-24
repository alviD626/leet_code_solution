class Solution(object):
    def countAsterisks(self, s):
        """
        :type s: str
        :rtype: int
        """
        return sum([a.count("*") for a in s.split("|")][0::2])
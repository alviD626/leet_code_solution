from collections import Counter
class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        str1 = Counter(ransomNote)
        str2 = Counter(magazine)
        if str1 & str2 == str1:
            return True
        return False
class Solution(object):
    def firstPalindrome(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        for char in words:
            if char == char[::-1]:
                return char
        return ""
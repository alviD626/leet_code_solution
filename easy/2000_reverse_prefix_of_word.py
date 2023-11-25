class Solution(object):
    def reversePrefix(self, word, ch):
        """
        :type word: str
        :type ch: str
        :rtype: str
        """
        result = word.find(ch)
        if result:
            return word[:result+1][::-1]+word[result+1:]
        return word
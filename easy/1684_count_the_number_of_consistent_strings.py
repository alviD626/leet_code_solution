class Solution(object):
    def countConsistentStrings(self, allowed, words):
        """
        :type allowed: str
        :type words: List[str]
        :rtype: int
        """
        allowed_word = set(allowed)
        count = 0
        for word in words:
            p = set(word)
            if p.issubset(allowed_word):
                count+=1
        return count
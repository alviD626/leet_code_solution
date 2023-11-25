class Solution(object):
    def replaceDigits(self, s):
        """
        :type s: str
        :rtype: str
        """
        result = []
        for i in range(len(s)):
            if i % 2 == 0:
                result.append(s[i])
            if i % 2 == 1:
                result.append(chr(ord(s[i-1])+int(s[i])))
        return ''.join(result)
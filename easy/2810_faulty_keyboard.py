class Solution(object):
    def finalString(self, s):
        """
        :type s: str
        :rtype: str
        """
        result = []
        for ch in s:
            if ch == 'i':
                result.reverse()
            else:
                result.append(ch)
        return ''.join(result)
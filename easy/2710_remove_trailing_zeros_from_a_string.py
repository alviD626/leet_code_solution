class Solution(object):
    def removeTrailingZeros(self, num):
        """
        :type num: str
        :rtype: str
        """
        res = ''
        for i in range(len(num) - 1, -1, -1):
            if num[i] != '0':
                res = num[:i + 1]
                break
        return res
class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return -1
        m, M, i = min(strs), max(strs), 0
        for i in range(min(len(m),len(M))):
            if m[i] != M[i]:
                break
        else:
            i +=1
        return m[:i]
class Solution(object):
    def cellsInRange(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        result = []
        for i in range(ord(s[0]),ord(s[3])+1):
            rs = ""
            for j in range(int(s[1]),int(s[4])+1):
                rs = chr(i)+str(j)
                result.append(rs)
        return result
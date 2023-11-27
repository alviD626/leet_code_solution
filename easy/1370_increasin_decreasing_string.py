class Solution(object):
    def sortString(self, s):
        """
        :type s: str
        :rtype: str
        """
        S = list(s)
        result = []
        while len(S)>0:
            smallest = sorted(set(S))
            for small in smallest:
                result.append(small)
                S.remove(small)

            largest = sorted(set(S),reverse=True)
            for large in largest:
                result.append(large)
                S.remove(large)
        
        return ''.join(result)
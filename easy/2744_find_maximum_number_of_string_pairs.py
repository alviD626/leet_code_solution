class Solution(object):
    def maximumNumberOfStringPairs(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        ans = 0 
        for i in range(len(words)):
            for j in range(i+1,len(words)):
                if words[i][0] == words[j][1] and words[i][1] == words[j][0]:
                    ans+=1
        return ans 
class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        return " ".join(list(map(lambda x:x[::-1],s.split())))
    
        # return " ".join(x[::-1] for x in s.split(" "))

int_str = input()
solution = Solution()
result = solution.reverseWords(int_str)
print(result)
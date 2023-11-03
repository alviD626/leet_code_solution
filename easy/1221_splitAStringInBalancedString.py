class Solution(object):
    def balancedStringSplit(self, s):
        """
        :type s: str
        :rtype: int
        """
        word_count = l_count = r_count = 0
        for word in s:
            if word == "L":
                l_count += 1
            else:
                r_count += 1
            if l_count == r_count:
                word_count += 1
        return word_count

word = input("Input: ")
solution = Solution()
result = solution.balancedStringSplit(word)
print(result)
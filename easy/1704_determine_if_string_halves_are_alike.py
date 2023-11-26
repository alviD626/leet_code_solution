class Solution(object):
    def halvesAreAlike(self, s):
        """
        :type s: str
        :rtype: bool
        """
        vowels = 'aeiouAEIOU'
        mid , ans = len(s)//2 , 0
        for i in range(mid):
            if s[i] in vowels:
                ans +=1
            if s[mid+1] in vowels:
                ans -= 1
        return ans == 0
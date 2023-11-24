class Solution(object):
    def decodeMessage(self, key, message):
        """
        :type key: str
        :type message: str
        :rtype: str
        """
        mapping = {' ':' '}
        i = 0
        res = ''
        letter = 'abcdefghijklmnopqrstuvwxyz'
        for char in key:
            if char not in mapping:
                mapping[char] = letter[i]
                i+=1
        for char in message:
            res += mapping[char]
        
        return res
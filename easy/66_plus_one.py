class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        strings = ""
        for number in digits:
            strings += str(number)
        temp = str(int(strings)+1)
        return [int(temp[i]) for i in range(len(temp))]
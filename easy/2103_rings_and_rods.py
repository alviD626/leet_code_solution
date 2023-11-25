class Solution(object):
    def countPoints(self, rings):
        """
        :type rings: str
        :rtype: int
        """
        countt = 0
        for i in range(10):
            if rings.count('R'+str(i)) and rings.count('G'+str(i)) and rings.count('B'+str(i)):
                countt+=1
        return countt
class Solution(object):
    def squareIsWhite(self, coordinates):
        """
        :type coordinates: str
        :rtype: bool
        """
        c = coordinates
        if c[0] in 'aceg':
            return int(c[1])%2==0
        elif c[0] in 'bdfh':
            return int(c[1])%2==1
        return False
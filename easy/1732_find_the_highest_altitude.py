class Solution(object):
    def largestAltitude(self, gain):
        """
        :type gain: List[int]
        :rtype: int
        """
        result = 0
        current_altitude = 0
        for g in gain:
            current_altitude += g
            if current_altitude > result:
                result = current_altitude
        return result
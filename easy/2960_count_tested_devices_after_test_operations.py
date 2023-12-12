class Solution(object):
    def countTestedDevices(self, batteryPercentages):
        """
        :type batteryPercentages: List[int]
        :rtype: int
        """
        my_set = batteryPercentages
        count = 0
        for i in my_set:
            count += i>count
        return count
class Solution(object):
    def convertTemperature(self, celsius):
        """
        :type celsius: float
        :rtype: List[float]
        """
        kelvin = celsius + 273.15
        fahrenheit = (celsius * 1.80) + 32.0
        return [kelvin,fahrenheit]

celsius = float(input())
solution = Solution()
result = solution.convertTemperature(celsius)
print(result)
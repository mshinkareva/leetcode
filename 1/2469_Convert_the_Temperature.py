
class Solution:
    def convertTemperature(self, celsius: float) -> list[float]:
        return [celsius + 273.15, celsius * 1.80 + 32.00]


if __name__ == '__main__':
    print(Solution().convertTemperature(36.50))

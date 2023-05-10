class Solution:
    def removeDigit(self, number: str, digit: str) -> str:
        list_numbers = [number[:index]+number[index+1:] for index, val in enumerate(number) if val == digit]

        return max(list_numbers)


if __name__ == '__main__':
    print(Solution().removeDigit(number="133235", digit="3"))

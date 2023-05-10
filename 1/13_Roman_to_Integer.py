class Solution:
    def romanToInt(self, s: str) -> int:
        roman_int = {'I': 1,
                     'V': 5,
                     'X': 10,
                     'L': 50,
                     'C': 100,
                     'D': 500,
                     'M': 1000}
        s = s.replace('IV', 'IIII').replace('IX', 'VIIII')
        s = s.replace('XC', 'XXXXXXXXX').replace('CM', 'CCCCCCCCC')
        s = s.replace('CD', 'CCCC').replace('XL', 'XXXX')
        num = 0
        for char in s:
            num += roman_int[char]
        return num


if __name__ == '__main__':
    print(Solution().romanToInt('MMMXLV'))

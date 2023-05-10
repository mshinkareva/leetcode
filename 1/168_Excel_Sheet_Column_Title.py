class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        ans = ''
        while columnNumber:
            columnNumber -= 1
            result, remainder = divmod(columnNumber, 26)
            ans = chr(remainder + 65) + ans
            columnNumber = result
        return ans


if __name__ == '__main__':
    print(Solution().convertToTitle(701))

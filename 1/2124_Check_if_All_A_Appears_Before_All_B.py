class Solution:
    def checkString(self, s: str) -> bool:
        for first, second in zip(s[:-1], s[1:]):
            if ord(first) > ord(second):
                return False
        return True


if __name__ == '__main__':
    print(Solution().checkString('ba'))

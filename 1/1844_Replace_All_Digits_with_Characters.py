class Solution:
    def replaceDigits(self, s: str) -> str:
        new = [c if i % 2 == 0 else chr(ord(s[i - 1]) + int(c)) for i, c in enumerate(s)]
        return ''.join(new)


if __name__ == '__main__':
    print(Solution().replaceDigits('a1c1e1'))

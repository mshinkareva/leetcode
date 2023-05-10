class Solution:
    def validPalindrome(self, s: str) -> bool:
        if s[::-1] == s:
            return True
        for index_ in range(len(s)):
            new = ''.join(s[:index_]+''+s[index_+1:])
            if new[::-1] == new:
                return True

if __name__ == '__main__':
    print(Solution().validPalindrome(s='abca'))
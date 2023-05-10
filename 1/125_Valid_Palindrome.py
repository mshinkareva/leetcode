class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned_s = ''.join(char.lower() for char in s if char.isalnum())
        reversed = cleaned_s[::-1]
        return cleaned_s == reversed

if __name__ == '__main__':
    print(Solution().isPalindrome("ab@a"))
class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        if word.isupper() | word.islower():
            return True
        if word[0].isupper() & word[1:].islower():
            return True
        return False

if __name__ == '__main__':
    print(Solution().detectCapitalUse("usA"))
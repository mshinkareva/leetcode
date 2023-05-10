class Solution:
    def secondHighest(self, s: str) -> int:
        digits_ = {int(char) for char in s if char.isdigit()}
        return -1 if len(digits_) < 2 else sorted(digits_, reverse=True)[1]

if __name__ == '__main__':
    print(Solution().secondHighest('dfa12321afd'))
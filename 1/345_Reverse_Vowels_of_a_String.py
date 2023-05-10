class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = 'aeiouAEIOU'
        s_list = list(s)
        reversed_vowels = reversed([char for char in s if char in vowels])
        for index, char in enumerate(s_list):
            if char in vowels:
                s_list[index] = next(reversed_vowels)
        return ''.join(s_list)


if __name__ == '__main__':
    print(Solution().reverseVowels("Aa"))

class Solution:
    def reverseWords(self, s: str) -> str:
        return ' '.join([word[::-1] for word in s.split(' ')])


if __name__ == '__main__':
    print(Solution().reverseWords("Let's take LeetCode contest"))
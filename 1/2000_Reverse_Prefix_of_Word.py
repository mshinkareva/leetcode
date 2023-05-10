class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        if not word.__contains__(ch):
            return word
        index_ch = word.index(ch)+1
        return f'{word[:index_ch][::-1]}{word[index_ch:]}'


if __name__ == '__main__':
    print(Solution().reversePrefix('abcdefd', 'dw'))
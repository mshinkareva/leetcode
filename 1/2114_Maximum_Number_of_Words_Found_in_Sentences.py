class Solution:
    def mostWordsFound(self, sentences: list[str]) -> int:
        max_item = 0
        for sentence in sentences:
            s_list = len(sentence.split(' '))
            if max_item < s_list:
                max_item = s_list
        return max_item


if __name__ == '__main__':
    print(
        Solution().mostWordsFound(["please wait","continue to fight","continue to win"]))

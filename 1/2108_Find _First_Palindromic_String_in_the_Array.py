class Solution:
    def firstPalindrome(self, words: list[str]) -> str:
        for word in words:
            list_w = [_ for _ in word]
            polindrom = True
            for i, j in zip(list_w, reversed(list_w)):
                if i != j:
                    polindrom = False
                    break
            if polindrom:
                return word
        return ''



if __name__ == '__main__':
    print(Solution().firstPalindrome(["racgecar","car","rer1","racgecar","cool"]))




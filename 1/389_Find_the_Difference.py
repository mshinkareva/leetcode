class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        new_list = list(t)
        for _ in s:
            new_list.remove(_)
        return ''.join(new_list)



if __name__ == '__main__':
    print(Solution().findTheDifference('a', 'aa'))
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        temp_t = t
        for _ in s:
            if _ not in temp_t:
                return False
            index_ = temp_t.index(_)
            temp_t = temp_t[index_+1:]
        return True

if __name__ == '__main__':
    print(Solution().isSubsequence('abc', 'ahbgdc'))

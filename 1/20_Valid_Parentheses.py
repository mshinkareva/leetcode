class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2:
            return False
        while True:
            s_temp = s
            s = s.replace('()', '')
            s = s.replace('{}', '')
            s = s.replace('[]', '')
            if s_temp == s:
                return False
            if s == '':
                return True



if __name__ == '__main__':
    print(Solution().isValid("({{{{}}}))"))

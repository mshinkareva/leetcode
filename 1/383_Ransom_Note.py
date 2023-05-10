class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ransomNote_dict = {_: ransomNote.count(_) for _ in set(ransomNote)}
        for key, val in ransomNote_dict.items():
            if val > magazine.count(key):
                return False
        return True

if __name__ == '__main__':
    print(Solution().canConstruct('b', 'bbv'))



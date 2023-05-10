class Solution:
    def countSegments(self, s: str) -> int:
        return len(s.split())


if __name__ == '__main__':
    print(Solution().countSegments("Hello, my name is John"))


def push_number(num: int) -> str:
    if num == 10:
        return 'This is 10'

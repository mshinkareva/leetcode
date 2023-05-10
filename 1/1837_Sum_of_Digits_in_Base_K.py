class Solution:
    def sumBase(self, n: int, k: int) -> int:
        if n == 0:
            return 0
        result = 0
        while n:
            n, res = divmod(n, k)
            result += res
        return result


if __name__ == '__main__':
    print(Solution().sumBase(34, 6))

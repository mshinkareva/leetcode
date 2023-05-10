class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n == 1:
            return True
        if n < 1:
            return False
        while True:
            mod = n % 2
            if mod:
                return False
            n = n / 2
            if n == 1:
                return True


if __name__ == '__main__':
    print(Solution().isPowerOfTwo(15))

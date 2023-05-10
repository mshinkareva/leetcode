class Solution:
    def isprime(self, num):
        if num == 1 or num == 0:
            return False
        mods = []
        for _ in range(1, num+1):
            if not num % _:
                mods.append(_)
            if len(mods) == 3:
                return False
        if len(mods) == 2:
            return True
        return False

    def countPrimes(self, n: int) -> int:
        return len([num for num in range(n) if self.isprime(num)])


if __name__ == '__main__':
    print(Solution().countPrimes(499979))

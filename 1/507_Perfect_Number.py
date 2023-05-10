class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        if num == 1:
            return False
        count = 1
        for i in range(2, int(num ** 0.5) + 1):
            if not num % i:
                count += i + num // i
        return num == count


if __name__ == '__main__':
    print(Solution().checkPerfectNumber(28))

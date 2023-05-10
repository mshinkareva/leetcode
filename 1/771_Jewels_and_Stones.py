class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        return len([word for word in stones if word in jewels])


if __name__ == '__main__':
    print(Solution().numJewelsInStones(jewels="z", stones="ZZ"))

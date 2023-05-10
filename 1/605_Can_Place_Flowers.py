class Solution:
    def canPlaceFlowers(self, flowerbed: list[int], n: int) -> bool:
        empty = flowerbed.count(0)
        flowers = flowerbed.count(1)

        if empty > flowers+n:
            return True
        if n < empty-n:
            return True
        return False

if __name__ == '__main__':
    print(Solution().canPlaceFlowers([1,0,1,0,1,0,1], n=0))
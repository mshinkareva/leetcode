class Solution:
    def distributeCandies(self, candyType: list[int]) -> int:
        types = len(set(candyType))
        candies_limit = int(len(candyType)/2)
        return types if candies_limit > types else candies_limit

if __name__ == '__main__':
    print(Solution().distributeCandies([1,1,2,2,3,3]))
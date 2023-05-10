class Solution:
    def numIdenticalPairs(self, nums: list[int]) -> int:
        count = 0
        hashmap = {}
        for _ in nums:
            if _ in hashmap:
                count += hashmap[_]
                hashmap[_] += 1
            else:
                hashmap[_] = 1
        print(hashmap)
        return max(hashmap, key=hashmap.get)




if __name__ == '__main__':
    print(Solution().numIdenticalPairs([1,2,3,1,1,3])   )
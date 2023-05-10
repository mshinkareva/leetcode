import heapq


class Solution:
    def lastStoneWeight(self, stones: list[int]) -> int:
        # convert stones list into a max heap
        stones = [-x for x in stones]
        heapq.heapify(stones)

        while len(stones) > 1:
            x = heapq.heappop(stones)
            y = heapq.heappop(stones)
            stone_weight_diff = x - y
            if stone_weight_diff != 0:
                heapq.heappush(stones, stone_weight_diff)

        return -stones[0] if stones else 0


if __name__ == '__main__':
    print(Solution().lastStoneWeight([2, 2, 5,6,8,1,8, 3]))

class Solution:
    def bestHand(self, ranks: list[int], suits: list[str]) -> str:
        ranks_count, ranks_suits = len(set(ranks)), len(set(suits))
        if ranks_count == 5 and ranks_suits == 1:
            return 'Flush'
        if ranks_count == 2 and ranks_suits == 4:
            return 'Three of a Kind'
        if ranks_count == 5 and ranks_suits == 3:
            return 'High Card'
        if ranks_count == 4 and ranks_suits == 3:
            return 'Pair'
        if ranks_count == 4 and ranks_suits == 4:
            return 'Pair'
        if ranks_count == 3 and ranks_suits == 3:
            return 'Three of a Kind'
        if ranks_count == 3 and ranks_suits == 4:
            return 'Pair'
        if ranks_count == 3 and ranks_suits == 2:
            return 'Pair'
        if ranks_count == 5 and ranks_suits == 4:
            return 'High Card'
        if ranks_count == 5 and ranks_suits == 2:
            return 'High Card'





if __name__ == '__main__':
    print(Solution().bestHand(ranks = [2,10,7,10,7], suits =["a","b","a","d","b"]))
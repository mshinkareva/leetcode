class Solution:
    def isWinner(self, player1: list[int], player2: list[int]) -> int:
        player1_sum = sum([val*2 if 10 in player1[max(0, num - 2):num] else val for num, val in enumerate(player1)])
        player2_sum = sum([val*2 if 10 in player2[max(0, num - 2):num] else val for num, val in enumerate(player2)])
        if player2_sum == player1_sum:
            return 0
        return 1 if player1_sum > player2_sum else 2


if __name__ == '__main__':
    print(Solution().isWinner(player1=[10,2,2,3], player2=[3,8,4,5]))

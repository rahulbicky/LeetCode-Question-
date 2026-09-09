class Solution:
    def minimumAddedCoins(self, coins: List[int], target: int) -> int:
        coins.sort()

        reach = 1
        count = 0
        i = 0

        while reach <= target:
            if i < len(coins) and coins[i] <= reach:
                reach += coins[i]
                i += 1
            else:
                reach += reach
                count += 1

        return count
        
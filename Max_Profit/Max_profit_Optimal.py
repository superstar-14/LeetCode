class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        mini = prices[0]
        best = 0
        for p in prices:
            if p < mini:
                mini = p
            elif p - mini > best:
                best = p - mini
        return best


# test it
sol = Solution()
print(sol.maxProfit([7,1,5,3,6,4]))
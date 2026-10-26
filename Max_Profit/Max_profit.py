class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        n=len(prices)
        max=0
        for i in range(n):
            for j in range(i+1,n):
                if prices[j]-prices[i]>max:
                    max=prices[j]-prices[i]
        return max

# test it
sol = Solution()
print(sol.maxProfit([7,1,5,3,6,4]))

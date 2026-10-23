class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        total=0
        best=float("-inf")
        for i in nums:
            total+=i
            if total>best:
                best=total
            if total<0:
                total=0
                continue
        return best

# test it
sol = Solution()
print(sol.maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))
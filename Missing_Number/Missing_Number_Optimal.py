class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        n=len(nums)
        return ((n*(n+1))//2)-sum(nums)

# test it
sol = Solution()
print(sol.missingNumber([0,1,2]))
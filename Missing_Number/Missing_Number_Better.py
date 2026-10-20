class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        n=len(nums)
        s=set()
        for i in nums:
            s.add(i)
        for j in range(n+1):
            if j not in s:
                return j

# test it
sol = Solution()
print(sol.missingNumber([0,1,2]))
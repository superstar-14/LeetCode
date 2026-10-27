class Solution:
    def rearrangeArray(self, nums: list[int]) -> list[int]:
        n=len(nums)
        l=[0]*n
        po,ne=0,1
        for i in nums:
            if i>0:
                l[po]=i
                po+=2
            else:
                l[ne]=i
                ne+=2
        return l

# test it
sol = Solution()
print(sol.rearrangeArray([3,1,-2,-5,2,-4]))
class Solution:
    def prod(self,nums):
        n=len(nums)
        count=0
        best=0
        for i in range(n):
            if nums[i]==1:
                count+=1
                if count>best:
                    best=count
            if nums[i] != 1:
                count=0
        return best
            
# test it
sol = Solution()
print(sol.prod([1,1,0,1,1,1]))
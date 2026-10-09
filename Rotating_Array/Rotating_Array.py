class Solution:
    def rev(self,nums,k):
        n=len(nums)
        k%=n
        nums[:]=nums[n-k:]+nums[:n-k]
        return nums
        

        
# test it
sol = Solution()
print(sol.rev([1,2,3,4],2))
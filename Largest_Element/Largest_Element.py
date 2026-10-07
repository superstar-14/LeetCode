class Solution:
    def largest(self,nums):
        large=nums[0]
        for i in range(1,len(nums)):
            if nums[i]>large:
                large=nums[i]
        return large
        

                           
# test it
sol = Solution()
print(sol.largest([9,8,100,-99,-88,10000,9999999,78]))
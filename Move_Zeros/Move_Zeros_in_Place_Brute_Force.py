class Solution:
    def rev(self,nums):
        n=len(nums)
        i=0
        while i<n:
            if nums[i] !=0:
                i+=1
            else:
                z=nums.pop(i)
                nums.insert(n,z)
                n-=1
        return nums
# test it
sol = Solution()
print(sol.rev([0,0,1,2]))
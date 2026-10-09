class Solution:
    def rev(self,nums):
        n=len(nums)
        i=0
        while i<n:
            if nums[i]==0:
                break
            i+=1
        if i==n:
            return
        j=i+1
        while j<n:
            if nums[j]!=0:
                nums[i],nums[j]=nums[j],nums[i]
                i+=1
            j+=1
        return nums
        

        
# test it
sol = Solution()
print(sol.rev([0,0,1,2]))
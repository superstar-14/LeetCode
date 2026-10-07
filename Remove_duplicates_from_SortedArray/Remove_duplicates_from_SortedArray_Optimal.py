class Solution:
    def dupli(self,nums):
        n=len(nums)
        if n==1:
            return 1
        i=0; j=1
        while j<n:
            if nums[i] != nums[j]:
                i+=1
                nums[i],nums[j]=nums[j], nums[i]
            j+=1
        return i+1

                           
# test it
sol = Solution()
print(sol.dupli([1,1,2,2,3,4,4,5,6,7,8,9,10]))
class Solution:
    def dupli(self,nums):
        d={}
        for i in range(0,len(nums)):
            d[nums[i]]=0
        k=0
        for j in d:
            nums[k]=j
            k+=1
        return k
                           
# test it
sol = Solution()
print(sol.dupli([1,1,2]))
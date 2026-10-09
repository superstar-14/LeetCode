class Solution:
    def rev(self,nums):
        n=len(nums)
        arr=[]
        count=0
        for i in range(n):
            if nums[i]!=0:
                arr.append(nums[i])
            if nums[i]==0:
                count+=1
        zero=[0]*count
        arr.extend(zero)
        nums[:]=arr
        return nums
        

        
# test it
sol = Solution()
print(sol.rev([0,0,1,2]))
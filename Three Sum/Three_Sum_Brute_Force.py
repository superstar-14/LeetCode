class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        l=[]
        for i in range(len(nums)):
           for j in range(i+1,len(nums)):
            ele=0-nums[i]-nums[j]
            for k in range(j+1,len(nums)):
                if nums[k]==ele:
                    trip=sorted([nums[i],nums[j],0-nums[i]-nums[j]])
                    if trip in l:
                        continue
                    else:     
                        l.append(trip)           
        return l

                    
# test it
sol = Solution()
print(sol.threeSum(nums=[-1,0,1,2,-1,-4]))
class Solution:
    def quick(self, nums,low,high):
        if low>=high:
            return nums
        i=low
        j=high
        pivot=nums[low]
        while i<=j:
            if nums[i]<=pivot:
                i+=1
            elif nums[j]>pivot:
                j-=1
            else:
                nums[i],nums[j]=nums[j],nums[i]
                j-=1
                i+=1
        nums[j],nums[low]=nums[low],nums[j]
        self.quick(nums,low,j-1)
        self.quick(nums,j+1,high)
        return nums

                           
# test it
sol = Solution()
print(sol.quick([9,8],0,1))
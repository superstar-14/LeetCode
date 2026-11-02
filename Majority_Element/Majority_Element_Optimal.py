class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        candidate,count=nums[0],0
        for i in nums:
            if count==0:
                candidate=i
            if i==candidate:
                count+=1
            else:
                count-=1
        return candidate

# test it
sol = Solution()
print(sol.majorityElement([2,2,1,1,1,2,2]))
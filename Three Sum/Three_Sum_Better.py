class Solution:
  def threeSum(self, nums: list[int]) -> list[list[int]]:
    l=[]
    for i in range(0,len(nums)):
        s=set()
        for j in range(i+1,len(nums)):
            target =  -(nums[i]+nums[j])
            if target in s:
                m=[nums[i],nums[j],target]
                m.sort()
                if m not in l:
                    l.append(m)
            else :
                s.add(nums[j])
    return l

# test it
sol = Solution()
print(sol.threeSum(nums=[-1,0,1,2,-1,-4]))
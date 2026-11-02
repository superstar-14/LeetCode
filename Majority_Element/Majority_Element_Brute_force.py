class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        n=len(nums)
        count,best,best_num=0,0,0
        s=set()
        for i in range(n):
            s.add(nums[i])
            count=0
        for j in s:
            for i in nums:
                if j==i:
                    count+=1
            if count>best:
                best=count
                best_num=j
        return best_num

# test it
sol = Solution()
print(sol.majorityElement([2,2,1,1,1,2,2]))
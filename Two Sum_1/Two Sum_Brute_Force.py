from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        result = []
        for i in range(0, len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    result.extend([i, j])
                    return result
        return[]

# test it
sol = Solution()
print(sol.twoSum([2, 6, 11, 15], 9))

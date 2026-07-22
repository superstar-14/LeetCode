from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        L=[]
        Map= {}

        for i in range(len(nums)):
            tar= target - nums[i]
            if tar in Map:
                L.extend([Map[tar],i])
                return L
            else: 
                Map[nums[i]]=i
        return []
       
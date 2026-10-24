class Solution:
    def intersection(self, nums1: list[int], nums2: list[int]) -> list[int]:
        s=set()
        l=[]
        for i in nums1:
            s.add(i)
        for j in nums2:
            if j in s and j not in l:
                l.append(j)
        return l

# test it
sol = Solution()
print(sol.intersection([1,2,2,1],[2,2]))
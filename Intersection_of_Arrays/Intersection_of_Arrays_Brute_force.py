class Solution:
    def intersection(self, nums1: list[int], nums2: list[int]) -> list[int]:
        s1=set(nums1)
        s2=set(nums2)
        s3=set()
        n=len(s1)
        m=len(s2)
        if n>=m:
            for i in s2:
                if i in s1:
                    s3.add(i)
        if m>n:
            for j in s1:
                if j in s2:
                    s3.add(j)
        return list(s3)

# test it
sol = Solution()
print(sol.intersection([1,2,2,1],[2,2]))
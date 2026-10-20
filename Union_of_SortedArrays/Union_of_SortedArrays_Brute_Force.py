class Solution:
    def unionArray(self, nums1, nums2):
        s=set()
        l=[]
        n=len(nums1)
        m=len(nums2)
        for i in range(0,n):
            s.add(nums1[i])
        for j in range(0,m):
            s.add(nums2[j])
        for k in s:
            l.append(k)
        l.sort()
        return l

# test it
sol = Solution()
print(sol.unionArray([2, 7, 8 , 9, 10],[1,2,3,4,5,6,7]))
class Solution:
    def unionArray(self, nums1, nums2):
        i = 0
        j = 0
        n = len(nums1)
        m = len(nums2)
        l = []
        while i < n and j < m:
            if nums1[i] <= nums2[j]:
                if not l or nums1[i] != l[-1]:
                    l.append(nums1[i])
                i += 1
            else:
                if not l or nums2[j] != l[-1]:
                    l.append(nums2[j])
                j += 1
        while i < n:
            if not l or nums1[i] != l[-1]:
                l.append(nums1[i])
            i += 1
        while j < m:
            if not l or nums2[j] != l[-1]:
                l.append(nums2[j])
            j += 1
        return l

# test it
sol = Solution()
print(sol.unionArray([2, 7, 8 , 9, 10],[1,2,3,4,5,6,7]))
class Solution:
    def rearrangeArray(self, nums: list[int]) -> list[int]:
        lp=[]
        ln=[]
        l=[]
        k,m=0,0
        for i in nums:
            if i>0:
                lp.append(i)
            else:
                ln.append(i)
        while k<len(lp) and m<len(ln):
            l.append(lp[k])
            l.append(ln[m])
            k+=1
            m+=1
        return l

# test it
sol = Solution()
print(sol.rearrangeArray([3,1,-2,-5,2,-4]))
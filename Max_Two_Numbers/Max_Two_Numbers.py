class Solution:
    def max(self,l):
        m1,m2=0,0
        for i in range(0,len(l)):
            if l[i]>m1:
                m1=l[i]
            l.pop(m1)              
            for j in range(0,len(l)):
                if l[j]>m2:
                    m2=l[j]
                    
# test it
sol = Solution()
print(sol.max(l=[1,2,3,4,5,6,7,8,9,9]))

class Solution:
    def prod(self,n):
        a=list((str(n)))
        m1=int(max(a))
        a.remove(str(m1))
        m2=int(max(a))
        return m1*m2
            
# test it
sol = Solution()
print(sol.prod(1234))





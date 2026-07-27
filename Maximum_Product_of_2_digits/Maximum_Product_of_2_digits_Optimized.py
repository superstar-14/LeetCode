class Solution:
    def prod(self,n):
        m1,m2=0,0
        while n>0:
            a=n%10
            if a>m1:
                m2=m1
                m1=a
            elif a>m2:
                m2=a
            n=n//10
        return m1*m2           
            
# test it
sol = Solution()
print(sol.prod(31))










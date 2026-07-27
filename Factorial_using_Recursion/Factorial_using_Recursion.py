
class Solution:
    def fact(self,n):
        if n==0 or n==1:
            return 1
        return(n*self.fact(n-1))
 
# test it
sol = Solution()
print(sol.fact(5))
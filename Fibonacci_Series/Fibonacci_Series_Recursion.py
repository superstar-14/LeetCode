class Solution:
    def fib(self,s,i,j,l):
        if len(l)<s+1:
            l.append(l[i]+l[j])
            return self.fib(s,i+1,j+1,l)
        else:
            return l[-1]

        

       

        
        
# test it
sol = Solution()
print(sol.fib(9,0,1,l=[0,1]))
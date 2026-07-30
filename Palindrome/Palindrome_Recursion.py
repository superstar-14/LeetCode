class Solution:
    def pal(self,st,i,j):
        if st[i]==st[j]:
            i=i+1
            j=j-1
            if i+1<-j:
                self.pal(st,i,j)
            return "Palindrome"
        else:
            return "Not Palindrome"
                  
# test it
sol = Solution()
print(sol.pal("malyalam",0,-1))





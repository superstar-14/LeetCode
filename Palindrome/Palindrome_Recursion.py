class Solution:
    def pal(self,st,i,j):
        if st[i] != st[j]:
            return "Not Palindrome"
        if i>=j:
            return "Palindrome"
        return self.pal(st,i+1,j-1)  
# test it
sol = Solution()
print(sol.pal("malayalam",0,len("malayalam")-1))






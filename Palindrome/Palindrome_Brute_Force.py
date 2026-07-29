class Solution:
    def pal(self,s):
        a=len(s)-1
        for i in range(0,a):
            if s[i]==s[a]:
                return "Palindrome"
        return "Not Palindrome"
        i+=1
        a-=1
# test it
sol = Solution()
print(sol.pal("malayalam"))
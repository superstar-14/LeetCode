class Solution:
    def dic(self,lis):
        d={}
        for i in lis:
            if i in d:
                d[i]+=1
            elif i not in d:
                d[i]=1
        return d
            
# test it
sol = Solution()
print(sol.dic([5,5,5,6,7,8,7,7,8,8,9,0,1,2,2,1,1]))
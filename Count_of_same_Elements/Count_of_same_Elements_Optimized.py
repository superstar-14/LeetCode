class Solution:
    def com(self,lis1,lis2):
        d={}
        count=0
        for i in lis1:
            d[i]=1
            if i in d.keys():
                d[i]+=1
        for j in lis2:
            if j in d.keys():
                count+=1
        return count
            
# test it
sol = Solution()
print(sol.com([1,2,3],[1,2,3,4,5]))
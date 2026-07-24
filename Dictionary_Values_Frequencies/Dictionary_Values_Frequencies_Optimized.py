class Solution:
    def dic(self,lis):
        d={}
        for i in range(0, len(lis)):
            d[lis[i]]=d.get(lis[i],0)+1
        return d
            
# test it
sol = Solution()
print(sol.dic([5,5,5,6,7,8,7,7,8,8,9,0,1,2,2,1,1]))
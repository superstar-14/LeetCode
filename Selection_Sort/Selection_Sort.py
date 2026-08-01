class Solution:
    def sels(self,lis):
        for i in range(0,len(lis)):
            for j in range(i+1,len(lis)):
                if lis[j]<lis[i]: #use this line for descending sort  -->if lis[j]>lis[i]:
                    lis[i],lis[j]=lis[j],lis[i]
        return lis


# test it
sol = Solution()
print(sol.sels([2,3,5,7,9,0,1,4,6,8]))
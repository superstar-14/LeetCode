class Solution:
    def sels(self,lis):
        for i in range(0,len(lis)):
            min_ind=i
            for j in range(i+1,len(lis)):
                if lis[j]<lis[min_ind]: #use this line for descending sort  -->if lis[j]>lis[min_ind]:
                    min_ind=j
            lis[i],lis[min_ind]=lis[min_ind],lis[i]

        return lis


# test it
sol = Solution()
print(sol.sels([2,3,5,7,9,0,1,4,6,8]))
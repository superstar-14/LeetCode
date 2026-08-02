class Solution:
    def bubble(self,lis):
        swapped=False
        for i in range(len(lis)-1):
            if lis[i]>lis[i+1]:
                lis[i],lis[i+1]=lis[i+1],lis[i]
                swapped=True
        if not swapped:
            return lis
        return self.bubble(lis)
            
# test it
sol = Solution()
print(sol.bubble([2,4,6,8,9,0,7,5,3,1]))




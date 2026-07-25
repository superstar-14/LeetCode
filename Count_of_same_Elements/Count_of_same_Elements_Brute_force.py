class Solution:
    def com(self,lis1,lis2):
        count=0
        for i in lis1:
            for j in lis2:
                if i==j:
                    count+=1
        return count
            
# test it
sol = Solution()
print(sol.com([1,2,3,4,5,6,7,8,9,0],[1,2,3,4,5,99,10,45]))
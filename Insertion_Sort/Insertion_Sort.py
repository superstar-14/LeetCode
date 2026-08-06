class Solution:
    def insertion(self, l):
        for i in range(1,len(l)):
            j=i-1
            key=l[i]
            while j>=0 and l[j]>key:
                l[j+1]=l[j]
                j=j-1
            l[j+1]=key
        return l                        
# test it
sol = Solution()
print(sol.insertion([9,8]))





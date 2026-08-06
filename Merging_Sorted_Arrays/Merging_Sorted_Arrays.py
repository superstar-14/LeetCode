class Solution:
    def merge(self, l,m):
        i,j=0,0 #Created 2 variables for 2 pointers in 2 lists
        r=[]
        while i<len(l) and j<len(m): #Run loop till one of the list gets exhausted             
            if  l[i]<=m[j]:
                r.append(l[i])
                i+=1
            else:
                r.append(m[j])
                j+=1
        if i<len(l): #if j gets exhausted
            while i<len(l): 
                r.append(l[i])
                i+=1
        if j<len(m): #if i gets exhausted
            while j<len(m):
                r.append(m[j])
                j+=1
                    
        return r
# test it
sol = Solution()
print(sol.merge([5,6,7,8,9],[0,1,2,3,4]))
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
    
    def merge_sort(self,l):
        if len(l)<=1:
            return l
        mid=len(l)//2
        left=l[:mid]
        right=l[mid:]
        left=self.merge_sort(left)
        right=self.merge_sort(right)
        return self.merge(left,right)

# test it
sol = Solution()
print(sol.merge_sort([9,8,7,6,5,4,3,2,1]))
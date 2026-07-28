class Solution:
    def rev(self,arr,i,n):
        arr[i],arr[n]=arr[n],arr[i]
        if len(arr)%2==0:
            if i+1==len(arr)//2:
                return arr
        if len(arr)%2!=0:
            if arr[i]==arr[n]:
                return arr
        i+=1
        n-=1
        self.rev(arr,i,n)
        return arr


        
# test it
sol = Solution()
print(sol.rev([8,99,0,1],0,-1))


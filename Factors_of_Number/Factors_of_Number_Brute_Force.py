class Solution:
    def factor(self,num):
        l=[]
        if num==0:
            return [0]
        for i in range(1,num+1): #Searches for all natural numbers in range of 1 to num/2
            if num%i==0: #searches for divisors of num
                l.append(i) #appends numbers to l for final result
        return l
            
# test it
sol = Solution()
print(sol.factor(0))
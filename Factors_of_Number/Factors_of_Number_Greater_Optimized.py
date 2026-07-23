class Solution:
    def factor(self,num):
        l=[]
        if num==0:
            return [0]
        for i in range(1,int(num**0.5)+1): #Searches for numbers from 1 to sqrt(n) because if i is a factor then n/i is also a factor
            if num%i==0: #searches for divisors of num
                l.append(i) #appends numbers to l for final result
                if i*i != num:
                    l.append(num//i)
        l.sort()
        return l
            
# test it
sol = Solution()
print(sol.factor(36))
class Solution:
    def factorial(self,num):
        l=[]
        if num==0:
            return [0]
        for i in range(1,(num//2)+1): #Searches for numbers from 1 to n/2 because  no factors of n lie beyond n/2 except for n itself
            if num%i==0: #searches for divisors of num
                l.append(i) #appends numbers to l for final result
        l.append(num)
        return l
            
# test it
sol = Solution()
print(sol.factorial(100))
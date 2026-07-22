class Solution:
    def armstrong(self,num):
        num_add = 0
        num_le=len(str(num))
        original= num
        
        
        while num>0:
            num_ext= num%10 #Extracts Digits
            num_add+= num_ext**num_le #Raising Individual Digits to length
            num=num//10
        if num_add==original:
            return "Armstrong Number"
        else:
            return "Not Armstrong Number"
        
# test it
sol = Solution()
print(sol.armstrong(153))

class Solution:
    def reverse(self,num):
        num_rev=0
        while num>0:
            num_ind= num%10 #extracts individual numbers
            num_rev= num_rev*10+ num_ind #Reverses the number by adding individual digits
            num=num//10 # Removes the last digit from the number
            
        return num_rev

        
# test it
sol = Solution()
print(sol.reverse(1234))


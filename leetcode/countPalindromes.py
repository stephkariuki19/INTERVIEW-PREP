class Solution:  
    def countAllPali(self,s):
        palindromes = 0
        for i in range(len(s)):
            left = right = i  #for odd n.o palindromes
            palindromes += self.countPalindromes(s,left,right)
            
            left = i #for even n.o palindromes
            right = i + 1
            palindromes += self.countPalindromes(s,left,right)
        return palindromes
    def countPalindromes(sef,s,left,right):
        palindromes = 0
        while left >=0 and right < len(s) and s[left] == s[right]:
            palindromes +=1
            left -=1
            right +=1
        return palindromes
        
m = Solution()
print(m.countAllPali('abba'))

class Solution(object):
    def maxProfit(self, prices):
     
        max_diff = 0
        for i in range(len(prices)-1,-1,-1):
            for j in range(i-1,-1,-1):
                diff = prices[i]- prices[j] 
                if (diff > max_diff):
                    max_diff = diff
               
            
        return max_diff
Solution().maxProfit([7,1,5,3,6,4])

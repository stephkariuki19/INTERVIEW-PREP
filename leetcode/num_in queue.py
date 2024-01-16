#There are n people standing in a queue, and they numbered from 0 to n - 1 
#in left to right order. You are given an array heights of distinct integers where heights[i] represents the height of the ith person.
class Solution(object):
    def canSeePersonsCount(self, heights):
        stack = []
        n = len(heights)
        ans = [0] * len(heights)
        for i in range(n-1,-1,-1):
            total_seen =0
            while stack and heights[i]>stack[-1]:
                stack.pop()
                total_seen +=1
            #atm we were popping smaller values but we might need to look at a val larger than the current one so that we can see if it has a smaller val beneath it 
            if stack:
                total_seen +=1
            stack.append(heights[i])
            ans[i] =total_seen
        return ans
       
        

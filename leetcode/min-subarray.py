#MINIMUM SIZE SUB ARRAY
class Solution(object):
    def minSubArrayLen(self, target, nums):
        '''
        at each idex, have a sliding window,keep tranck of how many n.o are needed to get to target, choose smallest
        '''
        if not nums:
            return 0
        
        min_length = float('inf')
        window_sum = 0
        window_start = 0
        
        for window_end in range(len(nums)):
            window_sum += nums[window_end]
            
            while window_sum >= target:
                min_length = min(min_length, window_end - window_start + 1)
                window_sum -= nums[window_start]
                window_start += 1
        
        return min_length if min_length != float('inf') else 0
#OR
class Solution(object):
    def minSubArrayLen(self, target, nums):
        if not nums:
            return 0
        
        min_length = float('inf')
        window_sum = 0
        window_start = 0
        
        for start_index in range(len(nums)):
            window_start = start_index  # Set the starting point

            min_length = float('inf')
            window_sum = 0
            
            for window_end in range(start_index, len(nums)):
                window_sum += nums[window_end]
                
                while window_sum >= target:
                    min_length = min(min_length, window_end - window_start + 1)
                    window_sum -= nums[window_start]
                    window_start += 1
                    
        return min_length if min_length != float('inf') else 0

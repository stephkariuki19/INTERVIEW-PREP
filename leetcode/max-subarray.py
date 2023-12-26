MAXIMUM SUBARRAY
class Solution(object):
    def maxSubArray(self, nums):
'''
was to get the sub array with highest sum, went through all window sizes at each index
'''
        window_size = len(nums)
        greatest_sum = 0
        full_sum = 0

        # Calculate the sum of the entire array
        for k in range(len(nums)):
            full_sum += nums[k]

        # Iterate to find the greatest sum of a subarray
        for i in range(window_size):
            for j in range(len(nums)):
                test_sum = 0  # Initialize test_sum before using it
                for m in range(j, i): # wb large window size at the end?
                    test_sum += nums[m]
                
                # Compare the greatest subarray sum with the sum of the whole array
                greatest_sum = max(greatest_sum, test_sum, full_sum)

        return greatest_sum  # Move this line outside of the loop

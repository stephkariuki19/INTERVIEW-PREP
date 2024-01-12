#Given an integer array nums, find the 
subarray
 with the largest sum, and return its sum.
class Solution(object):
    def maxSubArray(self, nums):
        max_so_far = nums[0]
        curr_max = nums[0]
        for i in range(1,len(nums)): #thr curr max and max so far already have values
            curr_max = max(nums[i],nums[i]+curr_max)
            max_so_far = max(curr_max,max_so_far)
        return max_so_far

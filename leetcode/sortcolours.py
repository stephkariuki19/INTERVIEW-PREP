#should not return anything
class Solution(object):
    def sortColors(self, nums):
        counts = [0, 0, 0]  # Count occurrences of 0, 1, and 2
        for num in nums:
            counts[num] += 1
        
        index = 0
        for color in range(3):  # 0, 1, 2 representing colors
            for i in range(counts[color]):
                nums[index] = color
                index += 1
        #could put return nums 
    #m = Solution()
#print(m.sort(nums))

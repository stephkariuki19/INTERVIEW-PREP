#WRONG!!!!
class Solution(object):
    def productExceptSelf(self, nums):
        output = []
        for i in range(len(nums)):
            skip_index = i
            product = 1  # Reset product for each i
            for j, num in enumerate(nums):  # Use j instead of i to avoid conflict
                if j != skip_index:
                    product *= num
            output.append(product)
        return output

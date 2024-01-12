class Solution(object):
    def maxProfit(self, nums):
        min_price = float("inf")
        profit = 0

        for i in range(len(nums)):
            if nums[i] < min_price:
                min_price = nums[i]
            elif profit < nums[i] - min_price:
                profit = nums[i] - min_price

        return profit

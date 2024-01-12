#given a target give the indices of items that add up to the target
class Solution:
    def twoSum(self, nums,target):
        prevMap = {}
        for i, n in enumerate(nums):
            diff = target - n
            if diff in prevMap:
                return [prevMap[diff], i]
            prevMap[n] = i
        return

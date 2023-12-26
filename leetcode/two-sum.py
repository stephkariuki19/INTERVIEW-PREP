#twoSum(self,nums,target): brute force - T O(N^2), S O(1)
class Solution:
    def twoSum(self,nums:list[int],target:int) -> list[int]:
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i] + nums[j] == target:
                    return[i,j]
        return []       
m = Solution()
print(m.twoSum([1,2,3,5],8))

#MY SOLUTION
class Solution(object):
    def twoSum(self, nums, target):
        """
for every item at an index add it to other items and see if the sum matches the target.Return the indices
        """
        for i in range (len(nums)):
            for k in range (1,len(nums)):
                sum_numbers = nums[i] + nums[k]
                if sum_numbers == target:
                    result_array = [i,k]
                    return result_array
        print("no numbers amount to the target")        
                  
Solution().twoSum([2,3,4],7)

#print(m.twoSum([1,2,3,5],8)) optimized - T O(N), S O(N)
class Soution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        numToIndex = {}
        for i in range(len(nums)):
            print(f"newer{numToIndex}")
            if target - nums[i] in numToIndex:
                return [numToIndex[target - nums[i]], i]
                print("second")
                print(f"before [numToIndex[target - nums[i]], i]")
            numToIndex[nums[i]] = i
            print("secod")
            print(f"new {numToIndex[nums[i]]}")
        return []
V = Soution()
print(V.twoSum([1,2,3,5],8))

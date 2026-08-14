class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        lengthNums = len(nums)
        numsDict = dict(zip(nums, range(lengthNums)))
        for i in range(len(nums)):
            if (numsDict.get(target - nums[i]) is not None 
            and i != numsDict.get(target - nums[i])):
                return sorted([i, numsDict.get(target - nums[i])])

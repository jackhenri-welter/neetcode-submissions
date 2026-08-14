class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        numsDict = {}
        for num in nums:
            if(numsDict.get(num) != None): 
                return True
            numsDict[num] = 0
        return False

        
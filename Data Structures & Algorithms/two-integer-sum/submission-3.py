class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        vals = { nums[i]: i for i in range(len(nums)) }

        for i in range(len(nums)):
            num = nums[i]
            if target-num in vals and i != vals[target-num]:
                return [i, vals[target-num]]
        
        return []
        
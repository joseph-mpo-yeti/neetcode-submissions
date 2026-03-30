class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        vals = { nums[i]: i for i in range(len(nums)) }

        for num in nums:
            if target-num in vals:
                return [vals[num], vals[target-num]]
        
        return []
        
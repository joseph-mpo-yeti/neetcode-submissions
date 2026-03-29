class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        indices = set(nums)
        max_count = 1
        index = 0
        seen = set()
        
        while len(seen) < len(nums) and index < len(nums):
            curr_count = 1
            val = nums[index]
            if val in seen:
                index += 1
                continue

            seen.add(val)

            while val+1 in indices and val+1 not in seen:
                curr_count += 1
                val += 1
                seen.add(val)

            index += 1

            max_count = max(max_count, curr_count)
    

        return max_count